"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 00:44
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 00:44 
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
    



