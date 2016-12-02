# -*- coding: UTF-8 -*-
import re, os

def init(self, base):
    return os.path.join(base)

def config(self, base):
    return self.base
