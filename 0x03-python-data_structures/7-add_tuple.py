#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tone = resolve(tuple_a)
    ttwo = resolve(tuple_b)
    return (tone[0] + ttwo[0], tone[1] + ttwo[1])

def resolve(t=()):
    t_len = len(t)
    if t_len == 0:
        t_new = 0, 0
    elif t_len == 1:
        t_new = t[0], 0
    else:
        t_new = t[0], t[1]
    return t_new
