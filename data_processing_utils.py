import json


def process_user_data(users, filters=None, sort_by="name", ascending=True):
    # Function implementation here
    pass


def validate_email_list(email_addresses):
    if not email_addresses:
        raise ValueError("Email list cannot be empty")

    for email in email_addresses:
        if "@" not in email:
            raise ValueError(f"Invalid email format: {email}")

    return True


def merge_dictionaries(dict1, dict2, overwrite=False):
    """Merge two dictionaries with optional overwrite behavior."""
    # Implementation here
    pass


def transform_nested_data(data, transformers, default_value=None):
    """Apply transformation functions to nested dictionary data."""
    # Implementation
    pass


def read_config_file(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Handle file not found
        pass
    except json.JSONDecodeError:
        # Handle invalid JSON
        pass


if __name__ == "__main__":
    # Basic demo
    emails = ["test@example.com", "user@domain.org"]
    try:
        validate_email_list(emails)
        print("All emails are valid!")
    except ValueError as e:
        print(f"Email validation error: {e}")
    emails = ["alice@example.com", "bob@test.com", "valid@domain.org"]
    try:
        validate_email_list(emails)
        print(f"\nAll {len(emails)} emails are valid!")
    except ValueError as e:
        print(f"Email validation error: {e}")

    # Dictionary merging example
    dict1 = {"name": "John", "age": 25, "city": "NYC"}
    dict2 = {"age": 30, "country": "USA"}
    merged = merge_dictionaries(dict1, dict2, overwrite=True)
    print(f"\nMerged dictionaries: {merged}")
