class ScraperException(Exception):
    def __init__(self, message):
        """
        """
        self.message = message
        super().__init__(message)

    def __str__(self):
        """
        """
        return "Scrapers exception: {}".format(self.message)


class WebsiteNotImplementedError(ScraperException):
    def __init__(self, domain):
        """
        """
        message = "Website {} not supported".format(domain)
        super().__init__(message)


class NoSchemaFound(ScraperException):
    def __init__(self, url):
        """
        """
        message = "No recipe schema found at {}".format(url)
        super().__init__(message)


class ElementNotFound(ScraperException):
    def __init__(self, element):
        """
        """
        message = "Element {} not found in schema".format(url)
        super().__init__(message)
