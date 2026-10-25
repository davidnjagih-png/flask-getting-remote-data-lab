import requests
import json
 
 
class GetRequester:
    """A reusable helper for fetching data from a remote URL via HTTP GET.
 
    Initialise it with an endpoint URL, then call get_response_body() for the
    raw response, or load_json() to receive the response parsed into Python
    data structures (lists, dicts, strings, numbers).
    """
 
    def __init__(self, url):
        # Store the endpoint so every request made by this instance targets it.
        self.url = url
 
    def get_response_body(self):
        """Send a GET request to self.url and return the raw response body as bytes."""
        response = requests.get(self.url)
        # Fail loudly on 4xx/5xx responses instead of returning an error page as data.
        response.raise_for_status()
        return response.content
 
    def load_json(self):
        """Fetch the response body and parse it from JSON into Python objects."""
        return json.loads(self.get_response_body())
 