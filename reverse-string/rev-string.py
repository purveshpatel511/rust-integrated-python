#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-04-11 21:47:53
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os, string, random
import revstring # rust lib

def reverse_string_python(value):
    return value[::-1]

# Benchmark Code
iters = 1000000
value = "".join(random.choice(string.ascii_letters) for i in range(iters))

def test_reverse_string_python(benchmark):
    benchmark(reverse_string_python, value)

def test_reverse_string_rust(benchmark):
    benchmark(revstring.reverse_string_rust, value)

# def test_count_doubles_zip(benchmark):
#     benchmark(count_doubles_zip, value)