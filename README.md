# python-design-system-exporter

A prototype of Sketch style exporter. Script extracts styles from the internal structure of a Sketch file. Works best with a structured file where all text styles are located on the same page called "Typography".

#### Usage:

There are two scripts in this project:
1. `export.py` generates easy to read and parse JSON files from Sketch internal JSONs
2. `converter.py` runs `export.py` and converts its output to platform-specific code

`./exporter.py example.sketch`  prints a JSON like this:
```json
{
    "text-styles": [
        {
            "background": null,
            "border-color": {
                "blue": 6,
                "green": 179,
                "red": 141
            },
            "border-thickness": 1,
            "font-family": "OpenSans-CondensedBold",
            "font-size": 48.0,
            "gravity": "center",
            "shadows": null,
            "style-name": "text/h1/black",
            "text-color": {
                "blue": 58,
                "green": 52,
                "red": 59
            }
        },
        {
            "background": null,
            "font-family": "OpenSans-CondensedBold",
            "font-size": 48.0,
            "gravity": "center",
            "shadows": null,
            "style-name": "text/h1/white",
            "text-color": {
                "blue": 251,
                "green": 251,
                "red": 251
            }
        }
    ]
}
```

`./converter.py example.sketch android` prints a list of Android XML styles:
```xml
<?xml version="1.0" ?>
<resources>
  <style name="text_h1_black">
    <item name="android:fontFamily">OpenSans-CondensedBold</item>
    <item name="android:textSize">48.0sp</item>
    <item name="android:gravity">center</item>
    <item name="android:textColor">#3b343a</item>
  </style>
  <style name="text_h1_white">
    <item name="android:fontFamily">OpenSans-CondensedBold</item>
    <item name="android:textSize">48.0sp</item>
    <item name="android:gravity">center</item>
    <item name="android:textColor">#fbfbfb</item>
  </style>
</resources>
```

This script can generate Android styles XML file. Other converters should be added to `converters` directory and registered in `converter.py`.

#### Requirements

* Python 3, `req.txt` of [python_sketch_api](https://github.com/aednlaxer/python_sketch_api) module
* Supported Sketch format: Sketch 50+
