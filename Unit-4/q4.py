import re

def is_valid_url(url):
    regex = r'^https?://[^\s/$.?#].[^\s]*$'
    match = re.match(regex, url)
    return bool(match)

# Example usage
url = input("Enter a URL: ")
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")
