# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import collections
import functools
import typing
from contextlib import closing

import six
from dotmap import DotMap


def empty_str(_):
    # type: (typing.Any) -> typing.Text
    return ""


DotMap.__str__ = empty_str


def recursive_mapping_iterator(nested_mapping):
    # type: (typing.Mapping) -> typing.Generator[typing.Tuple[typing.Text, typing.Any], None, None]
    for key, value in six.iteritems(nested_mapping):
        if isinstance(value, collections.Mapping):
            for inner_key, inner_value in recursive_mapping_iterator(value):
                yield key + '.' + inner_key, inner_value
        else:
            yield key, value


def recursive_getattr(obj, attributes):
    # type: (typing.Any, typing.Text) -> typing.Any
    return functools.reduce(getattr, [obj] + attributes.split('.'))


def nested_mapping_to_line(nested_mapping, keys):
    # type: (typing.Mapping, typing.Sequence[typing.Text]) -> typing.Text
    dotted = DotMap(nested_mapping)

    return ','.join([str(recursive_getattr(dotted, key)) for key in keys])


def extract_header(data, stop_after=5):
    # type: (typing.Sequence[typing.Mapping], int) -> typing.List
    keys = set()  # type: typing.Set[typing.Text]

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


def transform(data, include_headers=True, keys=None):
    # type: (typing.Sequence[typing.Mapping], bool, typing.Sequence[typing.Text]) -> typing.Text
    keys = keys or extract_header(data)

    with closing(six.StringIO()) as buff:
        if include_headers:
            buff.write(','.join(keys))
            buff.write('\n')

        for nested_mapping in data:
            buff.write(nested_mapping_to_line(nested_mapping, keys))
            buff.write('\n')

        return buff.getvalue()
