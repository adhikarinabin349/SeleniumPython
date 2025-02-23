# pip install requests
import requests
import json

class HttpHelper:
    def __init__(self, base_url=None, headers=None):
        """
        Initializes the HttpHelper with optional base URL and headers.
        :param base_url: Optional base URL for all requests.
        :param headers: Optional headers for the requests.
        """
        self.base_url = base_url
        self.headers = headers if headers else {}

    def set_base_url(self, base_url):
        """
        Set the base URL for the helper.
        :param base_url: The base URL to use for the requests.
        """
        self.base_url = base_url

    def set_headers(self, headers):
        """
        Set custom headers for the requests.
        :param headers: Dictionary of headers.
        """
        self.headers = headers

    def get(self, endpoint, params=None):
        """
        Make a GET request.
        :param endpoint: The endpoint to make the request to.
        :param params: Optional dictionary of query parameters.
        :return: Response object.
        """
        url = self.base_url + endpoint if self.base_url else endpoint
        response = requests.get(url, params=params, headers=self.headers)
        return response

    def post(self, endpoint, data=None, json_data=None):
        """
        Make a POST request.
        :param endpoint: The endpoint to make the request to.
        :param data: Optional dictionary of form data (for non-JSON bodies).
        :param json_data: Optional dictionary to send as JSON body.
        :return: Response object.
        """
        url = self.base_url + endpoint if self.base_url else endpoint
        response = requests.post(url, data=data, json=json_data, headers=self.headers)
        return response

    def put(self, endpoint, data=None, json_data=None):
        """
        Make a PUT request.
        :param endpoint: The endpoint to make the request to.
        :param data: Optional dictionary of form data.
        :param json_data: Optional dictionary to send as JSON body.
        :return: Response object.
        """
        url = self.base_url + endpoint if self.base_url else endpoint
        response = requests.put(url, data=data, json=json_data, headers=self.headers)
        return response

    def delete(self, endpoint, params=None):
        """
        Make a DELETE request.
        :param endpoint: The endpoint to make the request to.
        :param params: Optional dictionary of query parameters.
        :return: Response object.
        """
        url = self.base_url + endpoint if self.base_url else endpoint
        response = requests.delete(url, params=params, headers=self.headers)
        return response

    def set_auth(self, auth_token):
        """
        Set the authorization token for the request headers.
        :param auth_token: Authorization token (e.g., JWT).
        """
        self.headers['Authorization'] = f"Bearer {auth_token}"

# Example usage
if __name__ == "__main__":
    # Initialize the helper
    http_helper = HttpHelper(base_url="https://jsonplaceholder.typicode.com")
    
    # Set authentication token (if needed)
    # http_helper.set_auth("your-jwt-token")

    # Example GET request
    response = http_helper.get("/posts")
    print(response.json())

    # Example POST request
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    response = http_helper.post("/posts", json_data=new_post)
    print(response.json())

    # Example PUT request
    updated_post = {"id": 1, "title": "foo updated", "body": "bar updated", "userId": 1}
    response = http_helper.put("/posts/1", json_data=updated_post)
    print(response.json())

    # Example DELETE request
    response = http_helper.delete("/posts/1")
    print(response.status_code)