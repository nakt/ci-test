#!/usr/bin/env python

class SampleClass:

    def __init__(self):
        self.num = 0

    def add(self):
        self.num += 1

    def get(self):
        return self.num


def test_add():

    c = SampleClass()

    assert c.get() == 0

    c.add()
    assert c.get() == 1

    c.add()
    assert c.get() == 2

test_add()

