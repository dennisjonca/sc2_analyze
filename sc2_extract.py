"""
SC2 Build Command Extractor

This module provides regex-based utilities to extract times and build commands
from StarCraft 2 game logs.

Example input format:
    "At 13:48, HeroMarine used BuildFactoryTechLab"

Usage:
    from sc2_extract import extract_time_and_build
    
    line = "At 13:48, HeroMarine used BuildFactoryTechLab"
    result = extract_time_and_build(line)
    # Returns: {'time': '13:48', 'player': 'HeroMarine', 'build_command': 'BuildFactoryTechLab'}
"""

import re


def extract_time_and_build(line):
    """
    Extract time, player, and build command from a game log line.
    
    Parses lines in the format:
        "At HH:MM, [player] used [BuildCommand]"
    
    Args:
        line (str): A line from the game log
        
    Returns:
        dict: A dictionary with 'time', 'player', and 'build_command' keys, or None if no match
        
    Example:
        >>> extract_time_and_build("At 13:48, HeroMarine used BuildFactoryTechLab")
        {'time': '13:48', 'player': 'HeroMarine', 'build_command': 'BuildFactoryTechLab'}
    """
    # Pattern explanation:
    # At\s+           - matches "At" followed by one or more whitespace
    # (\d{1,2}:\d{2}) - captures time in format H:MM or HH:MM
    # ,\s+            - matches comma and whitespace
    # (\w+)           - captures player name (one or more word characters)
    # \s+used\s+      - matches " used " with surrounding whitespace
    # (Build\w+)      - captures only commands starting with "Build" (e.g., BuildExtractor, BuildSupplyDepot)
    pattern = r'At\s+(\d{1,2}:\d{2}),\s+(\w+)\s+used\s+(Build\w+)'
    
    match = re.search(pattern, line)
    
    if match:
        return {
            'time': match.group(1),
            'player': match.group(2),
            'build_command': match.group(3)
        }
    return None


def extract_time(line):
    """
    Extract only the time from a game log line.
    
    Args:
        line (str): A line from the game log
        
    Returns:
        str: The time in HH:MM format, or None if no match
        
    Example:
        >>> extract_time("At 13:48, HeroMarine used BuildFactoryTechLab")
        '13:48'
    """
    result = extract_time_and_build(line)
    return result['time'] if result else None


def extract_build_command(line):
    """
    Extract only the build command from a game log line.
    
    Args:
        line (str): A line from the game log
        
    Returns:
        str: The build command, or None if no match
        
    Example:
        >>> extract_build_command("At 13:48, HeroMarine used BuildFactoryTechLab")
        'BuildFactoryTechLab'
    """
    result = extract_time_and_build(line)
    return result['build_command'] if result else None
