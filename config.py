import os

# this looks for an environment variable called SECRET_KEY and sets a variable of the same name
# in the class configuration. If the variable doesn't exist, a default is used
# This means it is possible to change the key without changing the code
# This is an example of separation of concerns
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'a total secret'
