#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Напечатать в обратном порядке последовательность чисел, признаком конца которой
# является 0.

def prt():
    n = int(input())
    if n == 0:
        return
    prt()
    print(n)


prt()