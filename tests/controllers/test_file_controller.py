import pytest
from unittest import TestCase
import requests
import json
import re


class TestFilesFromDirectory(TestCase):

    @pytest.fixture
    def url(self):
        return "http://localhost:5000/api/v1/"
    
    def get(self, pattern):
        pattern = r"\.js$"
        #TODO
        # FIle list