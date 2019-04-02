class Error(Exception):
    """Base Class for exceptions in this module."""
    pass
class InputError(Error):
  
   """Exception raised for errors in the input.

        Attributes:
            expression --input expression in which error occured
            message -- explanation of the error
"""
    
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
        ''' I don't think that it is important if you want to 
        know learn from https://docs.python.org/3/tutorial/errors.html
        '''
