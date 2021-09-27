"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 23:20
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 23:20
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
    
    def test_Email_ID_True(self):
        """
        Description: 
            In this test case when given a email should return true.
        """        
        self.assertTrue(Validation.validate_email("mfjkd7795@gmail.com"))
        self.assertTrue(Validation.validate_email("abc.xyz@bl.co.in"))
    
    def test_Email_ID_False(self):
        """
        Description: 
            In this test case when given a email should return flase.
        """        
        self.assertFalse(Validation.validate_email("mfjkd7795gmail.com"))
        self.assertFalse(Validation.validate_email("abc.xyzbl.co.in"))

    def test_phone_number_true(self):
        """
        Description: 
            In this test case when given a email should return true.
        """        
        self.assertTrue(Validation.validate_phone_number("91 8217485224"))
        self.assertTrue(Validation.validate_phone_number("91 9073623476"))
    
    def test_phone_number_false(self):
        """
        Description: 
            In this test case when given a email should return false.
        """        
        self.assertFalse(Validation.validate_phone_number("8217485224"))
        self.assertFalse(Validation.validate_phone_number("919073623476"))
    
    def test_phone_password_true(self):
        """
        Description: 
            In this test case when given a email should return false.
        """        
        self.assertTrue(Validation.validate_passwaord("fathajkd"))
        self.assertTrue(Validation.validate_passwaord("mohammadfatha"))

if __name__ == '__main__':
    unittest.main()