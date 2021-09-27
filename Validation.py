"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 23:20
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 20:20 
* @Title: : Python program for User Registration
"""

import re
from LoggerHandler import logger

class Validation():

    def validate_name(name):
        """
        Description:
            This function is to validate first and last name.
            Condition: Name should start with Capital letter and should have min 3 letters.
        Args:
            firstName: First and last name to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^[A-Z]{1}[a-z]{2,}$", name))
        except Exception as e:
            logger.error(e)
    
    def validate_email(email):
        """
        Description:
            E.g. abc.xyz@bl.co.in - Email has 3 mandatory parts (abc, bl & co) and 2 optional
             (xyz & in) with precise @ and . positions
        Args:
            Email : Email ID to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email))
        except Exception as e:
            logger.error(e)
    
    def validate_phone_number(number):
        """
        Description:
                E.g. 91 9919819801 - Country code follow by space and 10 digit number
        Args:
            Number: Phone number to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("91\\s[0-9]{10}", number))
        except Exception as e:
            logger.error(e)

    def validate_passwaord(passwd):
        """
        Description:
                As a User need to follow pre-defined Password rules. 
                Rule1– minimum 8 Characters - NOTE – All rules must be passed
        Args:
            Number: Password to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("[a-z]{8,}", passwd))
        except Exception as e:
            logger.error(e)
    
    def validate_passwaord1(passwd):
        """
        Description:
                As a User need to follow pre-defined Password rules. 
                Rule2– minimum 8 Characters min 1 upper case - NOTE – All rules must be passed
        Args:
            Number: Password to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match(r"^(?=[^A-Z]*[A-Z]).{8,}", passwd))
        except Exception as e:
            logger.error(e)
    
    def validate_passwaord2(passwd):
        """
        Description:
                As a User need to follow pre-defined Password rules. 
                Rule3– minimum 8 Characters min 1 upper case 1 numerical number
                NOTE – All rules must be passed
        Args:
            Number: Password to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match(r"^(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9]).{8,}", passwd))
        except Exception as e:
            logger.error(e)


