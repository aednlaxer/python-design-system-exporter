# python-design-system-exporter

A prototype of Sketch style exporter.

Usage:

```bash
./exporter.py example.sketch
``` 

prints a JSON like this:
```json
[
    {
        "background": null,
        "font-family": "OpenSans-CondensedBold",
        "font-size": 16.0,
        "gravity": "center",
        "shadows": null,
        "style-name": "text/button/primary/desktop",
        "text-color": {
            "blue": 251,
            "green": 251,
            "red": 251
        }
    },
    {
        "background": null,
        "font-family": "OpenSans-CondensedBold",
        "font-size": 13.0,
        "gravity": "center",
        "shadows": null,
        "style-name": "text/button/primary/mobile",
        "text-color": {
            "blue": 251,
            "green": 251,
            "red": 251
        }
    }
]
```

Supported Sketch format: Sketch 50+

Requirements: `req.txt` of [python_sketch_api](https://github.com/aednlaxer/python_sketch_api) module
