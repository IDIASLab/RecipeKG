class IngredientException(Exception):
    def __init__(self, message):
        """
        """
        self.message = message
        super().__init__(message)

    def __str__(self):
        """
        """
        return "Ingredient Exception: {}".format(self.message)


class IngredientNotFoundException(IngredientException):
    def __init__(self, line):
        super().__init__(message)


class LowConfidenceException(IngredientException):
    def __init__(self, line, confidence):
        message = "{} parsed with confidence level {}".format(line, confidence)
        super().__init__(message)
