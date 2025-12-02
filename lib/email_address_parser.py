import re

class EmailAddressParser:

    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # find all valid email patterns
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+", self.email_string)

        # return sorted unique list
        return sorted(set(emails))
