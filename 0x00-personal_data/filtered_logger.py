#!/usr/bin/env python3
"""script for regex-ing"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """function that returns the log message obfuscated"""
    return separator.join([f"{key}={redaction if key in fields else value}"
                           for key, value in (pair.split('=', 1) for pair in
                                              message.strip(separator).split(
                                                      separator))])
