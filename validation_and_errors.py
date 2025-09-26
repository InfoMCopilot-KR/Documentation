import re


class DataValidationError(Exception):
    def __init__(self, message, field_name=None):
        self.message = message
        self.field_name = field_name
        super().__init__(self.message)


class ConfigurationError(Exception):
    pass


def validate_email(email):
    if not email or "@" not in email:
        raise DataValidationError("Invalid email format", "email")
    return True


def validate_age(age):
    try:
        age_int = int(age)
        if age_int < 0 or age_int > 150:
            raise DataValidationError("Age must be between 0 and 150", "age")
        return age_int
    except ValueError:
        raise DataValidationError("Age must be a number", "age")


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        raise DataValidationError("Arguments must be numbers")


if __name__ == "__main__":
    # Basic demo
    try:
        validate_email("test@example.com")
        print("Email is valid!")

        age = validate_age("25")
        print(f"Age is valid: {age}")

        result = safe_divide(10, 2)
        print(f"Division result: {result}")

    except DataValidationError as e:
        print(f"Validation error: {e.message}")
