import typing

class Param:
    def __init__(self, name: str, mandatory: bool = False, default:typing.Any = None):
        self.m_name = name
        self.m_mandatory = mandatory
        self.m_default = default

    @staticmethod
    def merge_args(params: typing.List['Param'], **kwargs):
        for param in params:
            if param.m_name not in kwargs:
                if param.m_default is not None:
                    kwargs[param.m_name] = param.m_default
                elif param.m_mandatory:
                    raise InvalidParam('missing param. "%s"' % (param.m_name))
        return kwargs

class InvalidParam(Exception):
    pass



