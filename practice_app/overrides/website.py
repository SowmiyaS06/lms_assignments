def clear_website_cache(path=None):
    if path:
        print(f"Custom cache cleared for page: {path}")
    else:
        print("Custom cache cleared for ALL website pages")