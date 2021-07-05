# coding=utf-8

import traceback
import typing
from functools import wraps


class DataFormat(object):
    """
    接口统一返回结果格式
    """
    code: int
    status: bool
    message: object
    data: object

    def set(self, code=200, status=True, message='ok', data=None):
        self.code = code
        self.status = status
        self.message = message
        self.data = data
        return self

    def __str__(self):
        return f'{self.code}\n {self.status}\n {self.message}\n {self.data}'
