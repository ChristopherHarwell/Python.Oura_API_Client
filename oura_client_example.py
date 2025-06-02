import os
from dotenv import load_dotenv
from oura_ring import OuraClient

# Load environment variables from .env file
load_dotenv()

# Get the personal access token from environment
pat = os.getenv("PERSONAL_ACCESS_TOKEN")

if not pat:
    raise ValueError("PERSONAL_ACCESS_TOKEN not found in environment. Please set it in your .env file.")

# Create an OuraClient instance
client = OuraClient(pat)

# Fetch and print personal info
personal_info = client.get_personal_info()
print("Personal Info:", personal_info) 