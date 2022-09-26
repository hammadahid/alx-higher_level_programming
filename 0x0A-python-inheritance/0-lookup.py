#!/usr/bin/env python3
def lookup(obj):
    """Returns list of avialable attribute and methods"""
    return list(dir(obj))
