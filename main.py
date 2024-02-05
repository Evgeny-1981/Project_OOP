import os

value = os.getenv('API_LAYER')
print(value)
# или
value = os.environ.get('API_LAYER')
print(value)