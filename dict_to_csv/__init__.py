# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import collections
import functools
import six

from contextlib import closing

from dotmap import DotMap


def empty_str(_):
    return ""


DotMap.__str__ = empty_str


def recursive_mapping_iterator(nested_mapping):
    for key, value in six.iteritems(nested_mapping):
        if isinstance(value, collections.Mapping):
            for inner_key, inner_value in recursive_mapping_iterator(value):
                yield key + '.' + inner_key, inner_value
        else:
            yield key, value


def recursive_getattr(obj, attributes):
    return functools.reduce(getattr, [obj] + attributes.split('.'))


def nested_mapping_to_line(nested_mapping, keys):
    dotted = DotMap(nested_mapping)

    return ','.join([str(recursive_getattr(dotted, key)) for key in keys])


def transform(data):
    keys = set()

    for nested_mapping in data:
        for key in sorted([tpl[0] for tpl in recursive_mapping_iterator(DotMap(nested_mapping))]):
            keys.add(key)

    sorted_keys = sorted(keys)

    with closing(six.StringIO()) as buff:
        buff.write(','.join(sorted_keys))
        buff.write('\n')

        for nested_mapping in data:
            buff.write(nested_mapping_to_line(nested_mapping, sorted_keys))
            buff.write('\n')

        return buff.getvalue()
