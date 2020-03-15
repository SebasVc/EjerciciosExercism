def abbreviate(input_str: str) -> str:
    import re
    l = re.findall(r"[[A-Z]*[a-z]*|\W]", input_str)
    return ''.join([chunk[0] for chunk in l if chunk]).upper()