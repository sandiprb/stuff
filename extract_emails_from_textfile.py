"""
A CLI utility to extract and print all matching email addresses from a give text file.
"""

import re
import sys
from pathlib import Path


def extract_emails_from_text(text):
    email_reg_ex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_reg_ex, text)


def find_emails(filename):
    emails = []
    with open(filename) as f:
        extracted_emails = extract_emails_from_text(f.read())
        emails.extend(extracted_emails)
    return ', '.join(sorted(emails)) if len(emails) else None


if __name__ == "__main__":
    # Validate if input provided
    try:
        file_path_inputs = sys.argv[1] #  0
    except IndexError as e:
        print ('Please provide file path input.')
        sys.exit()

    # Validate input if file exists
    file = Path(file_path_inputs)
    if not file.is_file():
        print('Provide file does no exist on location, please make sure file path is correct.')
        sys.exit()
    
    print(find_emails(file))
