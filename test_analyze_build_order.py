"""
Tests for analyze_build_order module
"""

import unittest
import os
import tempfile
from analyze_build_order import analyze_file


class TestAnalyzeBuildOrder(unittest.TestCase):
    
    def setUp(self):
        """Create temporary files for testing"""
        self.temp_dir = tempfile.mkdtemp()
        self.input_file = os.path.join(self.temp_dir, 'test_input.txt')
        self.output_file = os.path.join(self.temp_dir, 'test_output.txt')
    
    def tearDown(self):
        """Clean up temporary files"""
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        os.rmdir(self.temp_dir)
    
    def test_analyze_file_basic(self):
        """Test analyzing a basic file with multiple build commands"""
        # Create input file
        with open(self.input_file, 'w') as f:
            f.write("At 0:12, Maru used BuildSupplyDepot\n")
            f.write("At 0:45, Maru used BuildBarracks\n")
            f.write("At 1:30, Maru used BuildRefinery\n")
        
        # Analyze file
        analyze_file(self.input_file, self.output_file)
        
        # Check output file exists
        self.assertTrue(os.path.exists(self.output_file))
        
        # Check output content
        with open(self.output_file, 'r') as f:
            content = f.read()
            self.assertIn("Build Order", content)
            self.assertIn("Time 0:12 - Build command: BuildSupplyDepot", content)
            self.assertIn("Time 0:45 - Build command: BuildBarracks", content)
            self.assertIn("Time 1:30 - Build command: BuildRefinery", content)
            self.assertIn("Total builds: 3", content)
    
    def test_analyze_file_with_empty_lines(self):
        """Test analyzing a file with empty lines"""
        # Create input file
        with open(self.input_file, 'w') as f:
            f.write("At 0:12, Maru used BuildSupplyDepot\n")
            f.write("\n")
            f.write("At 0:45, Maru used BuildBarracks\n")
            f.write("\n")
        
        # Analyze file
        analyze_file(self.input_file, self.output_file)
        
        # Check output file
        with open(self.output_file, 'r') as f:
            content = f.read()
            self.assertIn("Total builds: 2", content)
    
    def test_analyze_file_sorts_by_time(self):
        """Test that output is sorted chronologically"""
        # Create input file with unsorted times
        with open(self.input_file, 'w') as f:
            f.write("At 5:30, Maru used BuildFactory\n")
            f.write("At 0:45, Maru used BuildBarracks\n")
            f.write("At 2:15, Maru used BuildRefinery\n")
        
        # Analyze file
        analyze_file(self.input_file, self.output_file)
        
        # Check output is sorted
        with open(self.output_file, 'r') as f:
            lines = f.readlines()
            # Find the lines with build commands
            build_lines = [l for l in lines if l.startswith("Time")]
            self.assertEqual(len(build_lines), 3)
            self.assertIn("0:45", build_lines[0])
            self.assertIn("2:15", build_lines[1])
            self.assertIn("5:30", build_lines[2])


if __name__ == '__main__':
    unittest.main()
