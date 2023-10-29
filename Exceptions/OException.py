class OException(Exception):
    def __init__(self, operation: object, message: str | None = None):
        if message:
            super().__init__(f"Operation {operation} is not supported {message}")
        super().__init__(f"Operation {operation} is not supported")
