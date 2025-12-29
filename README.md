# sc2_analyze

StarCraft 2 game log analyzer - Extract times and build commands from game logs.

## Overview

This tool provides regex-based utilities to extract times and build commands from StarCraft 2 game logs.

## Analyzing Build Orders from Files

To analyze a complete build order from a text file:

```bash
python analyze_build_order.py input_file.txt output_file.txt
```

**Example:**

```bash
python analyze_build_order.py sample_input.txt build_order.txt
```

**Input file format** (one line per build command):
```
At 0:12, Maru used BuildSupplyDepot
At 0:18, Serral used BuildHatchery
At 0:45, Maru used BuildBarracks
At 1:00, Serral used BuildSpawningPool
```

**Output file format** (separated by player):
```
Build Order Analysis
==================================================

Player: Maru
--------------------------------------------------
Time 0:12 - Build command: BuildSupplyDepot
Time 0:45 - Build command: BuildBarracks
--------------------------------------------------
Total builds: 2

Player: Serral
--------------------------------------------------
Time 0:18 - Build command: BuildHatchery
Time 1:00 - Build command: BuildSpawningPool
--------------------------------------------------
Total builds: 2

==================================================
Total players: 2
Total builds: 4
```

The analyzer automatically:
- Separates build orders by player
- Sorts each player's builds chronologically
- Provides individual counts per player and total counts

## API Usage

Extract time, player, and build command from a log line:

```python
from sc2_extract import extract_time_and_build

line = "At 13:48, HeroMarine used BuildFactoryTechLab"
result = extract_time_and_build(line)
# Returns: {'time': '13:48', 'player': 'HeroMarine', 'build_command': 'BuildFactoryTechLab'}
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
At\s+(\d{1,2}:\d{2}),\s+\w+\s+used\s+(Build\w+)
```

This matches lines in the format:
- `At` followed by whitespace
- Time in format `H:MM` or `HH:MM` (captured)
- Comma and whitespace
- Player name (one or more word characters)
- ` used ` (with surrounding whitespace)
- Build command starting with "Build" (captured)

**Note:** Only commands starting with "Build" are extracted (e.g., BuildSupplyDepot, BuildExtractor). Commands like Gather, Train, Morph, etc. are filtered out.