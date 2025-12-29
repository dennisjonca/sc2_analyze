# sc2_analyze

StarCraft 2 game log analyzer - Extract times and build commands from game logs.

## Overview

This tool provides regex-based utilities to extract times and build commands from StarCraft 2 game logs.

## Example Usage

Extract time and build command from a log line:

```python
from sc2_extract import extract_time_and_build

line = "At 13:48, HeroMarine used BuildFactoryTechLab"
result = extract_time_and_build(line)
# Returns: {'time': '13:48', 'build_command': 'BuildFactoryTechLab'}
```

Extract only time:

```python
from sc2_extract import extract_time

time = extract_time("At 13:48, HeroMarine used BuildFactoryTechLab")
# Returns: '13:48'
```

Extract only build command:

```python
from sc2_extract import extract_build_command

command = extract_build_command("At 13:48, HeroMarine used BuildFactoryTechLab")
# Returns: 'BuildFactoryTechLab'
```

## Running the Example

```bash
python example.py
```

## Running Tests

```bash
python -m unittest test_sc2_extract.py -v
```

## Regex Pattern

The regex pattern used is:
```
At\s+(\d{1,2}:\d{2}),\s+\w+\s+used\s+(\w+)
```

This matches lines in the format:
- `At` followed by whitespace
- Time in format `H:MM` or `HH:MM` (captured)
- Comma and whitespace
- Player name (one or more word characters)
- ` used ` (with surrounding whitespace)
- Build command (captured)