
def deep_update(source, overrides):
    """
    Update a nested dictionary.
    Modify ``source`` in place.
    """
    for key, value in overrides.items():
        if isinstance(value, dict) and value:
            returned = deep_update(source.get(key, {}), value)
            source[key] = returned
        else:
            source[key] = overrides[key]
    return source