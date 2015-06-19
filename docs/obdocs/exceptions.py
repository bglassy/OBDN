from click import ClickException


class obdocsException(ClickException):
    """Base exceptions for all obdocs Exceptions"""


class ConfigurationError(obdocsException):
    """Error in configuration"""


class MarkdownNotFound(obdocsException):
    """A linked local Markdown file isn't found in the table of contents."""
