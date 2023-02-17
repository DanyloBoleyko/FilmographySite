import re


def url_friendly(string):
    formatted_string = re.sub(r'[^\w\s-]', '', string).strip().lower()
    formatted_string = re.sub(r'\s+', '-', formatted_string)
    return formatted_string
