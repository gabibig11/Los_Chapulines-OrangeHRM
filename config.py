import string
import random


system_url = "https://api-sandbox.orangehrm.com"
client_id = "api-client"
client_secret = "942d36a36d6bf422a36f5871f905b6e5"
grant_type = "client_credentials"
random_token = ''.join(random.choices(string.ascii_lowercase + string.digits, k=40))
expired_token = 'Bearer 71626b41e6f139449ba4d5277ffb01448eb70d26'
