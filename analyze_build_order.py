#!/usr/bin/env python
"""
SC2 Build Order Analyzer

This script analyzes a text file containing StarCraft 2 game log lines
and extracts the complete build order to an output file.

Usage:
    python analyze_build_order.py <input_file> <output_file>
    
Example:
    python analyze_build_order.py game_log.txt build_order.txt
"""

import sys
from sc2_extract import extract_time_and_build


def analyze_file(input_path, output_path):
    """
    Analyze a log file and extract build order to output file.
    Separates build orders by player.
    
    Args:
        input_path (str): Path to the input text file with game logs
        output_path (str): Path to the output text file for build order
    """
    build_orders = []
    
    # Read and parse the input file
    try:
        with open(input_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                    
                result = extract_time_and_build(line)
                if result:
                    build_orders.append(result)
                else:
                    print(f"Warning: Could not parse line {line_num}: {line}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Group by player
    players_builds = {}
    for item in build_orders:
        player = item['player']
        if player not in players_builds:
            players_builds[player] = []
        players_builds[player].append(item)
    
    # Sort each player's builds by time
    for player in players_builds:
        players_builds[player].sort(key=lambda x: x['time'])
    
    # Write to output file
    try:
        with open(output_path, 'w') as f:
            f.write("Build Order Analysis\n")
            f.write("=" * 50 + "\n\n")
            
            # Write build order for each player
            for player in sorted(players_builds.keys()):
                builds = players_builds[player]
                f.write(f"Player: {player}\n")
                f.write("-" * 50 + "\n")
                
                for item in builds:
                    f.write(f"Time {item['time']} - Build command: {item['build_command']}\n")
                
                f.write("-" * 50 + "\n")
                f.write(f"Total builds: {len(builds)}\n\n")
            
            f.write("=" * 50 + "\n")
            f.write(f"Total players: {len(players_builds)}\n")
            f.write(f"Total builds: {len(build_orders)}\n")
        
        print(f"Successfully analyzed {len(build_orders)} build commands from {len(players_builds)} player(s)")
        print(f"Output written to: {output_path}")
        
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 3:
        print("Usage: python analyze_build_order.py <input_file> <output_file>")
        print("\nExample:")
        print("  python analyze_build_order.py game_log.txt build_order.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    analyze_file(input_file, output_file)


if __name__ == '__main__':
    main()
