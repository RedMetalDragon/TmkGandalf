import requests
from abc import ABC, abstractmethod
from config import Config
import json


class AzureBaseService(ABC):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        """
        The function is a singleton implementation in Python that ensures only one instance of a class
        is created and initializes class attributes with configuration values.

        :param cls: The `cls` parameter in the code snippet refers to the class itself. When a class is
        instantiated, the `cls` parameter represents the class being instantiated. In this case, it is
        used within the `__new__` method to check if an instance of the class already exists in the `_
        :return: The `__new__` method is returning an instance of the class `cls` if it is not already
        present in the `_instances` dictionary of the class. The `__init__` method is not explicitly
        returning anything as it is an initializer method and does not return any value.
        """
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self):
        """
        The function initializes attributes for an Azure AI service using configuration values.
        """
        if not hasattr(self, "initialized"):  # Ensure __init__ is called only once
            self.api_key = Config.AZURE_AI_API_KEY
            self.azure_api_version = Config.AZURE_AI_API_VERSION
            self.endpoint = Config.AZURE_OPENAI_ENDPOINT
            self.initialized = True

    @abstractmethod
    def send_to_ai_service(self, data: str) -> any:
        pass

    def make_request(self, payload) -> dict:
        """
        The `make_request` function sends a POST request with a JSON payload using the provided API key
        and returns the response as a dictionary.

        :param payload: The `payload` parameter in the `make_request` method is the data that will be
        sent in the request body as JSON when making a POST request to the specified endpoint. It
        typically contains the information or data that the server needs to process the request
        :return: The `make_request` method returns a dictionary. If the request is successful, it
        returns the JSON response from the API. If there is an exception (such as a
        `requests.exceptions.RequestException`), it returns a dictionary with an "error" key containing
        the exception.
        """
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }
        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": e}
