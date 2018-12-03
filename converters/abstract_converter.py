#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class AbstractConverter(ABC):
    @abstractmethod
    def process_text_styles(self, nodes):
        pass


def clamp(x):
    return max(0, min(x, 255))


def rgb_to_hex(color_triplet):
    return "#{0:02x}{1:02x}{2:02x}".format(
        clamp(color_triplet['red']),
        clamp(color_triplet['green']),
        clamp(color_triplet['blue']))


def is_color_triplet(node):
    return isinstance(node, dict) and 'red' in node and 'green' in node and 'blue' in node
