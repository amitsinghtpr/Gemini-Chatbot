import re

def validate_input(user_input):
    """
    Validates that the user input is a non-empty string.
    Raises ValueError if invalid.
    """
    if not user_input or not isinstance(user_input, str):
        raise ValueError("Input must be a non-empty string.")
    return user_input.strip()

def format_response(response):
    """
    Extracts the answer from a Gemini response string of the form:
    content='The answer' additional_kwargs={} ...
    Handles single/double wrapping and extra metadata.
    """
    if not isinstance(response, str):
        return str(response)
    # Try to extract the innermost content='...' up to 2 times (for double-wrapped)
    for _ in range(2):
        match = re.search(r"content=['\"](.*?)['\"]", response)
        if match:
            response = match.group(1).strip()
        else:
            break
    # Final cleanup: remove any stray quotes
    return response.strip("'\" ")