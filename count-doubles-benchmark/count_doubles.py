#!/usr/bin/env python
###############################################################
#####  Coding   : utf-8
#####  Summary  : Comparing performance of rust and python with counting-doubles problem using benchmark tools.
#####  @Date    : 2021-04-05 15:00:29
#####  @Author  : Purvesh Patel (@purveshpatel511)
#####  @Link    : 
#####  @Version : 1.0.0
###############################################################

import re, string, random
import doubles ## rust package for counting doubles

def count_doubles_zip(value):
    # count doubles using ZIP method
    total = 0
    for s1, s2 in zip(value, value[1:]):
        if s1 == s2:
            total += 1
    return total

# regex for find doubles
double_regex = re.compile(r'(?=(.)\1)')

def count_doubles_regex(value):
    # count doubles using regex
    return len(double_regex.findall(value))

# Benchmark Code
iters = 10000
value = "".join(random.choice(string.ascii_letters) for i in range(iters))

def test_count_doubles_zip(benchmark):
    benchmark(count_doubles_zip, value)

def test_count_doubles_regex(benchmark):
    benchmark(count_doubles_regex, value)

def test_count_doubles_rust(benchmark):
    benchmark(doubles.countdoubles, value)
