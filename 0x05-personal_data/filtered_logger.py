import re

def filter_datum(fields, redaction, message, separator):
    pattern = r'\b(' + '|'.join(fields) + r')\b'
    return re.sub(pattern, redaction, message)
