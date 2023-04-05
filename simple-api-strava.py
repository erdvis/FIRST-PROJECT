from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_url = "https://erdvis.github.io/FIRST-PROJECT/"

session = OAuth2Session(client_id, redirect_url)

auth_base_url = "https://www.strava.com/oauth/authorize"
session.scope ("activity:read_all")
auth_link = session.authorization_url(auth_base_url)

print(f"Click Here!!! {auth_link[0]}")

reddirect_response = input(f"Paste reirect url: ")

token_url = "https://www.strava.com/api/v3/oauth/token"
session.fetch_token(
    token_url=token_url,
    client_id=client_id,
    client_secret=client_secret,  # check spelling here
    authorization_response=reddirect_response,
    include_client_id=True
)



response = session.get("https://www.strava.com/api/v3/athlete")

print("\n")
print(f"response Status: {response.status_code}")
print(f"response Reason: {response.reason}")
print(f"response Text: {response.text}")