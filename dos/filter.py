def filter_text(text):
    rules = {}
    for l in text.split("\n"):
        if l.startswith("#"):
            key, val = map(str.strip, l[1:].split("="))
            rules[key] = val

    for key in rules:
        for value in rules.values():
            if key in value:
                return False
    
    return True