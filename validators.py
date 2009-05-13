import re, settings

def validate_url(url):
    if re.search(settings.URL_VALIDATOR, url): raise ValueError("The URL contains invalid characters - only alphanumerics and hyphens allowed.")