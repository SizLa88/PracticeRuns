import pytest
import requests
from APIAutomation.Base.Base_Test import BaseTest
from APIAutomation.Endpoints.EndPoints import EndPoints

class TestGetUsers(BaseTest):

    @pytest.mark.order(2)  # Executes immediately following the creation phase
    def test_verify_get_users(self):
        # Maps query parameters cleanly matching the target URL path: EndPoints.USERS + "?page=2"
        params = {"page": 2}

        response = requests.get(EndPoints.USERS, params=params, headers=self.headers)

        # Asserts response success code status validation constraints
        assert response.status_code == 200, f"Expected status code <200> but was <{response.status_code}>."

        print("\nUsers Retrieved")
