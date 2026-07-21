import sys  # Built-in module used to get detailed information about exceptions


# Function to create a detailed error message
def error_message_detail(error, error_detail: sys):

    # sys.exc_info() returns:
    # (exception_type, exception_value, traceback)
    # We only need the traceback, so we ignore the first two values using '_'
    _, _, exc_tb = error_detail.exc_info()

    # Get the name of the Python file where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a custom error message with:
    # - File name
    # - Line number
    # - Original error message
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    # Return the complete error message
    return error_message


# Create our own custom exception class
# It inherits all the features of Python's built-in Exception class
class CustomException(Exception):

    # Constructor
    def __init__(self, error_message, error_detail: sys):

        # Call the parent (Exception) constructor
        # This makes our custom exception behave like a normal Python exception
        super().__init__(error_message)

        # Store the detailed error message
        # Calls the function above to include:
        # file name + line number + actual error
        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )

    # Whenever we print the exception,
    # Python automatically calls this method
    def __str__(self):

        # Return our custom formatted error message
        return self.error_message
    
