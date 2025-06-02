from dotenv import load_dotenv
from auth import get_oura_client

# Load environment variables from .env file
load_dotenv()

# Create an OuraClient instance
client = get_oura_client()

# Fetch and print personal info
personal_info = client.get_personal_info()
print("Personal Info:", personal_info) 