import logging
import sys
import pprint
import enum
import collections
import typing

class Spec:
    def __init__(self, name: str, mandatory: bool = False, default:typing.Any = None):
        self.m_name = name
        self.m_mandatory = mandatory
        self.m_default = default

class SpecError(Exception):
    pass

def merge_and_verify(specs: typing.List[Spec], **kwargs):
    for spec in specs:
        if spec.m_name not in kwargs:
            if spec.m_default is not None:
                kwargs[spec.m_name] = spec.m_default
            elif spec.m_mandatory:
                raise SpecError('missing param. "%s"' % (spec.m_name))
    return kwargs