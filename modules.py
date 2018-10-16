# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime

today = datetime.date.today()
print(today)

from datetime import date    # imports part of module

import time

timestamp = time.time()


# Pip modules
import camelcase

camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))


# Custom modules
import validator

email = 'test@test.com'

if validator.validate_email(email):
    print('Email is valid')
else:
    print('Not an email')

# or
from validator import validate_email

if validate_email(email):
    print('Email is valid')
else:
    print('Not an email')
