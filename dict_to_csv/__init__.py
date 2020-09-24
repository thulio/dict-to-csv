import collections.abc
import functools
import typing  # noqa: F401
from contextlib import closing
from io import StringIO

from dotmap import DotMap


def empty_str(args: typing.Any) -> typing.Text:
    return ""


DotMap.__str__ = empty_str


def recursive_mapping_iterator(
    nested_mapping: typing.Mapping,
) -> typing.Generator[typing.Tuple[typing.Text, typing.Any], None, None]:  # noqa: E501
    for key, value in nested_mapping.items():
        if isinstance(value, collections.abc.Mapping):
            for inner_key, inner_value in recursive_mapping_iterator(value):
                yield key + "." + inner_key, inner_value
        else:
            yield key, value


def recursive_getattr(obj: typing.Any, attributes: typing.Text) -> typing.Any:
    return functools.reduce(getattr, [obj] + attributes.split("."))


def nested_mapping_to_line(
    nested_mapping: typing.Mapping, keys: typing.Sequence[typing.Text]
) -> typing.Text:
    dotted = DotMap(nested_mapping)

    return ",".join([str(recursive_getattr(dotted, key)) for key in keys])


def extract_header(
    data: typing.Sequence[typing.Mapping], stop_after: int = 5
) -> typing.List[typing.Text]:
    keys: typing.Set[typing.Text] = set()

    for nested_mapping in data:
        for key, value in recursive_mapping_iterator(DotMap(nested_mapping)):
            old_length = len(keys)
            keys.add(key)
            new_length = len(keys)

            if old_length != new_length:
                stop_after += 1
            else:
                stop_after -= 1

            if stop_after == 0:
                break

    sorted_keys = sorted(keys)

    return sorted_keys


def transform(
    data: typing.Sequence[typing.Mapping],
    include_headers: bool = True,
    keys: typing.Sequence[typing.Text] = None,
):
    keys = keys or extract_header(data)

    with closing(StringIO()) as buff:
        if include_headers:
            buff.write(",".join(keys))
            buff.write("\n")

        for nested_mapping in data:
            buff.write(nested_mapping_to_line(nested_mapping, keys))
            buff.write("\n")

        return buff.getvalue()
