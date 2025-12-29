"""
Tests for sc2_extract module
"""

import unittest
from sc2_extract import extract_time_and_build, extract_time, extract_build_command


class TestSC2Extract(unittest.TestCase):
    
    def test_extract_time_and_build_basic(self):
        """Test extraction from the example line"""
        line = "At 13:48, HeroMarine used BuildFactoryTechLab"
        result = extract_time_and_build(line)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['time'], '13:48')
        self.assertEqual(result['build_command'], 'BuildFactoryTechLab')
    
    def test_extract_time_and_build_different_time(self):
        """Test with different time format"""
        line = "At 5:30, Player1 used BuildBarracks"
        result = extract_time_and_build(line)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['time'], '5:30')
        self.assertEqual(result['build_command'], 'BuildBarracks')
    
    def test_extract_time_and_build_different_player(self):
        """Test with different player names"""
        line = "At 22:15, Serral used BuildHatchery"
        result = extract_time_and_build(line)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['time'], '22:15')
        self.assertEqual(result['build_command'], 'BuildHatchery')
    
    def test_extract_time_only(self):
        """Test extracting only time"""
        line = "At 13:48, HeroMarine used BuildFactoryTechLab"
        time = extract_time(line)
        
        self.assertEqual(time, '13:48')
    
    def test_extract_build_command_only(self):
        """Test extracting only build command"""
        line = "At 13:48, HeroMarine used BuildFactoryTechLab"
        build_command = extract_build_command(line)
        
        self.assertEqual(build_command, 'BuildFactoryTechLab')
    
    def test_no_match(self):
        """Test with line that doesn't match the pattern"""
        line = "This is a different format"
        result = extract_time_and_build(line)
        
        self.assertIsNone(result)
    
    def test_no_match_time_only(self):
        """Test time extraction with no match"""
        line = "No match here"
        time = extract_time(line)
        
        self.assertIsNone(time)
    
    def test_no_match_build_command_only(self):
        """Test build command extraction with no match"""
        line = "No match here"
        build_command = extract_build_command(line)
        
        self.assertIsNone(build_command)


if __name__ == '__main__':
    unittest.main()
