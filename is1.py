import re

n = int(input("enter a number: "))
emails = []
for x in range(n):
    emails.append(input())

def fun(s):
    return bool(re.match("^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-z0-9]{1,3}$", s))

def filter_mail(emails):
    return list(filter(fun, emails))

filtered_emails = filter_mail(emails)
filtered_emails.sort()
for x in filtered_emails:
    print(x)
