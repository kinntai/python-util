#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

def progressbar(percent):
    bar_unit = "#"
    max_bar_unit_num = 50
    bar_unit_num = int(float(percent)/100 * max_bar_unit_num)
    bar = (bar_unit * bar_unit_num) + (" " * (max_bar_unit_num - bar_unit_num))
    print "\r[{0}] {1}/{2}".format(bar, int(percent), 100),
    if percent == 100:
        print ""
