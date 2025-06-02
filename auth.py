import os
from dotenv import load_dotenv
from oura_ring import OuraClient

# Load environment variables from .env file
load_dotenv()

def get_oura_client():
    pat = os.getenv("PERSONAL_ACCESS_TOKEN")
    if not pat:
        raise ValueError(
            "PERSONAL_ACCESS_TOKEN not found in environment. Please set it in your .env file."
        )
    return OuraClient(pat)
