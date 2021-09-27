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

    def setUp(self):
        pass

    def test_First_Name_True(self):
        """
        Description: 
            In this test case when given a valid first name should return true.
        """        
        self.assertTrue(Validation.validate_name("Mohammad"))
        self.assertTrue(Validation.validate_name("Fat"))


    def test_First_Name_False(self):
        """
        Description: 
            In this test case when given a invalid first name should return false.
        """        
        self.assertFalse(Validation.validate_name("fatha"))
        self.assertFalse(Validation.validate_name("F@tha"))
    
    def test_Last_Name_True(self):
        """
        Description: 
            In this test case when given a valid last name should return true.
        """        
        self.assertTrue(Validation.validate_name("Jamkhandi"))
        self.assertTrue(Validation.validate_name("Jam"))
    
    def test_Last_Name_False(self):
        """
        Description: 
            In this test case when given a invalid last name should return false.
        """        
        self.assertFalse(Validation.validate_name("jamkhandi"))
        self.assertFalse(Validation.validate_name("j@am"))

if __name__ == '__main__':
    unittest.main()
    