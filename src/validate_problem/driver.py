from src.validate_problem.utils import *
emails = ['user@example.com','user@domain.co.in','user.name@example','user123@website','invalid_email','user@','@domain.com']
for x in emails:
    if validate_email(x):
        print(x)