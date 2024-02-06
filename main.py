import os

value = os.getenv('API_GITHUB')
print(value)
# или
value = os.environ.get('EXCHANGE_RATE_API_KEY')
print(value)

