#!/usr/bin/env python3
"""script for regex-ing"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """function that returns the log message obfuscated"""
    pairs = message.strip(';').split(';')
    res = []
    for pair in pairs:
        if pair.split('=')[0] in fields:
            pair = re.sub(r'=' + re.escape(
                pair.split('=')[1]), '=' + redaction, pair)
        res.append(pair)
    return separator.join(res)
