#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ElementTree
from xml.dom import minidom

from converters.abstract_converter import AbstractConverter, is_color_triplet, rgb_to_hex


class AndroidConverter(AbstractConverter):
    def process_text_styles(self, nodes):
        root = ElementTree.Element('resources')

        for node in nodes:
            style_element = ElementTree.Element('style')
            style_element.set("name", node['style-name'].replace("/", "_").replace(" ", "_"))

            for attr in node:
                attr_name = get_android_attr(attr)
                if attr_name is not None:
                    e = ElementTree.Element('item')
                    e.set('name', attr_name)

                    if is_color_triplet(node[attr]):
                        node_text = rgb_to_hex(node[attr])
                    else:
                        unit = get_unit(attr) or ""
                        node_text = '{value}{unit}'.format(
                            value=str(node[attr]),
                            unit=unit
                        )

                    e.text = node_text
                    style_element.append(e)

            root.append(style_element)

        print(prettify(root))


def get_android_attr(node_name):
    if node_name == 'font-family':
        return "android:fontFamily"
    elif node_name == 'font-size':
        return "android:textSize"
    elif node_name == 'gravity':
        return "android:gravity"
    elif node_name == 'text-color':
        return "android:textColor"
    elif node_name == 'background-color':
        return "android:background"
    return None


def get_unit(node_name):
    if 'font-size' == node_name:
        return "sp"
    return None


def prettify(element):
    rough_string = ElementTree.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
