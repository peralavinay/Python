import re

n = int(input("enter a number: "))
emails = []
for x in range(n):
    emails.append(input())

valid = re.compile("^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-z0-9]{1,3}$")
emails = filter(valid.match, emails)
filter_emails = sorted(emails)
for x in filter_emails:
    print(x)
