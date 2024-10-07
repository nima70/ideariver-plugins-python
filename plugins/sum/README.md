# Sum Plugin

**Version:** 1.0  
**Author:** [Your Name]

## Overview

The **Sum Plugin** is a simple plugin that accepts a JSON object with two keys, `a` and `b`, and returns the sum of these two values in the form of a JSON response. This plugin can be dynamically loaded, initialized, and executed using the `PluginLoader`.

## Features

- Accepts input in JSON format: `{ "a": <int>, "b": <int> }`
- Returns the sum of `a` and `b` as: `{ "sum": <int> }`
- Can be integrated into a plugin system with dynamic loading and initialization.

## Installation

1. Ensure that the `sum_plugin.py` file is placed in the `plugins/` folder.
2. Add the corresponding `plugin_sum_metadata.json` file to the same folder.

### Example `plugin_sum_metadata.json`:

```json
{
  "nameTag": "sum_plugin",
  "title": "Sum Plugin",
  "description": "Calculates the sum of two numbers (a and b).",
  "executableFile": "plugins/sum_plugin.py",
  "iconURL": "path/to/icon.png",
  "readme": "plugins/sum_plugin/README.mdx"
}
```
