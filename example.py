#!/usr/bin/env python
"""
Example usage of the SC2 Build Command Extractor

This script demonstrates how to use the sc2_extract module to extract
times and build commands from StarCraft 2 game log lines.
"""

from sc2_extract import extract_time_and_build, extract_time, extract_build_command


def main():
    # Example line from the problem statement
    line = "At 13:48, HeroMarine used BuildFactoryTechLab"
    
    print("Example Line:")
    print(f"  {line}")
    print()
    
    # Extract both time and build command
    result = extract_time_and_build(line)
    if result:
        print("Extracted data:")
        print(f"  Time: {result['time']}")
        print(f"  Build Command: {result['build_command']}")
    print()
    
    # Extract only time
    time = extract_time(line)
    print(f"Time only: {time}")
    
    # Extract only build command
    build_command = extract_build_command(line)
    print(f"Build command only: {build_command}")
    print()
    
    # More examples
    print("Additional Examples:")
    print("-" * 50)
    
    examples = [
        "At 5:30, Player1 used BuildBarracks",
        "At 22:15, Serral used BuildHatchery",
        "At 0:45, Maru used BuildSupplyDepot",
    ]
    
    for example in examples:
        result = extract_time_and_build(example)
        if result:
            print(f"Line: {example}")
            print(f"  -> Time: {result['time']}, Command: {result['build_command']}")
            print()


if __name__ == '__main__':
    main()
