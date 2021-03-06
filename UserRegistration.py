"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 23:50
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 23:50
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
    
    def test_password_true(self):
        """
        Description: 
            In this test case when given a password rule 1 should return true.
        """        
        self.assertTrue(Validation.validate_passwaord("fathajkd"))
        self.assertTrue(Validation.validate_passwaord("mohammadfatha"))
    
    def test_password_false(self):
        """
        Description: 
            In this test case when given a password rule 1 should return false.
        """        
        self.assertFalse(Validation.validate_passwaord("fatha"))
        self.assertFalse(Validation.validate_passwaord("12345678"))
    
    def test_password_1_true(self):
        """
        Description: 
            In this test case when given a password rule 2 should return true.
        """        
        self.assertTrue(Validation.validate_passwaord1("Fathajkd"))
        self.assertTrue(Validation.validate_passwaord1("mohammadFatha"))
    
    def test_password_1_false(self):
        """
        Description: 
            In this test case when given a password rule 2 should return false.
        """        
        self.assertFalse(Validation.validate_passwaord1("fatha"))
        self.assertFalse(Validation.validate_passwaord1("mohammadfatha"))

    def test_password_2_true(self):
        """
        Description: 
            In this test case when given a password rule 3 should return True.
        """        
        self.assertTrue(Validation.validate_passwaord2("Fathajkd12"))
        self.assertTrue(Validation.validate_passwaord2("mohammadFatha98"))
    
    def test_password_2_false(self):
        """
        Description: 
            In this test case when given a password rule 3 should return false.
        """        
        self.assertFalse(Validation.validate_passwaord2("Fathajkd"))
        self.assertFalse(Validation.validate_passwaord2("mohammadfatha98"))

    def test_password_3_true(self):
        """
        Description: 
            In this test case when given a password rule 4 should return true.
        """        
        self.assertTrue(Validation.validate_passwaord3("Fathajkd12@"))
        self.assertTrue(Validation.validate_passwaord3("mohammadFatha98$"))

    def test_password_3_false(self):
        """
        Description: 
            In this test case when given a password rule 4 should return false.
        """        
        self.assertFalse(Validation.validate_passwaord3("Fathajkd12"))
        self.assertFalse(Validation.validate_passwaord3("mohammadfatha98&"))

if __name__ == '__main__':
    unittest.main()