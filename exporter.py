#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

from python_sketch_api.sketch_api import SketchFile
from python_sketch_api.sketch_types import SJTextLayer, SJSymbolMaster, TextAlignmentEnum


def colour(color_component):
    return {
        "red": round(color_component.red * 255),
        "green": round(color_component.green * 255),
        "blue": round(color_component.blue * 255)
    }


def gravity(alignment):
    if alignment == TextAlignmentEnum.Left:
        return "left"
    elif alignment == TextAlignmentEnum.Right:
        return "right"
    elif alignment == TextAlignmentEnum.Center:
        return "center"
    elif alignment == TextAlignmentEnum.Justified:
        return "justified"
    else:
        return None


def shadows(shadowsList):
    if shadowsList is None:
        return None

    s = []
    for shadow in shadowsList:
        if shadow.isEnabled:
            s.append({
                "blur-radius": shadow.blurRadius,
                "color": shadow.color,
                "offset-x": shadow.offsetX,
                "offset-y": shadow.offsetY
            })

    return s


def export(sketch_filename):
    file = SketchFile.from_file(sketch_filename)

    for page in file.sketch_pages:

        # Typography page contains all text styles
        if page.name == "Typography":
            styles = {'text-styles': []}

            for layer in page.layers:
                style = {}

                if type(layer) is SJSymbolMaster:
                    style['style-name'] = layer.name

                    for subLayer in layer.layers:
                        if type(subLayer) is SJTextLayer:
                            style['background'] = subLayer.backgroundColor

                            if subLayer.style.borders is not None:
                                for border in subLayer.style.borders:
                                    if border.isEnabled:
                                        style['border-color'] = colour(border.color)
                                        style['border-thickness'] = border.thickness

                            style['shadows'] = shadows(subLayer.style.shadows)

                            for attr in subLayer.attributedString.attributes:
                                font = attr.attributes.MSAttributedStringFontAttribute.attributes
                                color = attr.attributes.MSAttributedStringColorAttribute
                                style['font-family'] = font.name
                                style['font-size'] = font.size
                                style['gravity'] = gravity(attr.attributes.paragraphStyle.alignment)
                                style['text-color'] = colour(color)

                        styles['text-styles'].append(style)

            return styles


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./exporter.py file.sketch")
    else:
        filename = sys.argv[1]
        print(json.dumps(export(filename), sort_keys=True, indent=4))
