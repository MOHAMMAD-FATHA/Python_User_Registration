"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 00:44
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 00:44 
* @Title: :Python program for User Registartion
"""
from Validation import Validation
import unittest

class UserValidationTest(unittest.TestCase):

    def test_ValidFirstName(self):
        """
        Description: 
            In this test case when given a valid first name should return true.
        """        
        self.assertTrue(Validation.validate_name("Mohammad"))
        self.assertTrue(Validation.validate_name("Fat"))


    def test_InvalidFirstName(self):
        """
        Description: 
            In this test case when given a invalid first name should return false.
        """        
        self.assertFalse(Validation.validate_name("fatha"))
        self.assertFalse(Validation.validate_name("F@tha"))

if __name__ == '__main__':
    unittest.main()
    