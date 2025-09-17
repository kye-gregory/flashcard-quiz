class LoggingConfigError(Exception):
    """Raised when logging configuration fails."""

    def __init__(self, exception: Exception):
        error_msg = f"{exception} ({type(exception).__name__})"
        super().__init__(f"Failed to configure logging during setup: {error_msg}")
        self.exception = exception
