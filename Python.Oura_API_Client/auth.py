import os

class OuraAuth:
    """
    Handles Oura API Key authentication for making authorized requests.
    """
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('OURA_API_KEY')
        if not self.api_key:
            raise ValueError("Oura API key must be provided either as an argument or in the OURA_API_KEY environment variable.")

    def get_headers(self) -> dict:
        """
        Returns the headers required for authenticating with the Oura API.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
