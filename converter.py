#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from converters.android_style_converter import AndroidConverter
from exporter import export

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./converter.py input.sketch <platform>")
    else:
        styles = export(sys.argv[1])
        supported_platforms = {
            "android": AndroidConverter(),
        }
        for arg in range(2, len(sys.argv)):
            platform = sys.argv[arg].lower()
            if platform in supported_platforms:
                supported_platforms[platform].process_text_styles(styles['text-styles'])
            else:
                print("Platform {platform} no supported".format(platform=platform))
