"""
Created on Sat Sept 12 22:41:09 2018
frozen dir
@author: Rico
"""
#coding=utf-8
import sys
import os


def app_path():
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


class AppPath():
    app_path()
