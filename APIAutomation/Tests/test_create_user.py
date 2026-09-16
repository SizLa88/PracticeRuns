import pytest
import requests
from APIAutomation.Base.Base_Test import BaseTest
from APIAutomation.Endpoints.EndPoints import EndPoints
from APIAutomation.Utils.Test_Data import TestData


class TestCreateUser(BaseTest):

    @pytest.mark.order(1)  # Replaces TestNG xml positioning to force this test to execute first
    def test_verify_user_registration_pipeline(self):
        # Translates your Java multiline Text Block payload string exactly into a clean Python dictionary map
        payload = {
            "name": "Sizwe",
            "job": "Automation Tester"
        }

        # Sends the payload body using requests, explicitly inheriting self.headers from BaseTest
        response = requests.post(EndPoints.USERS, json=payload, headers=self.headers)

        # Asserts a clean 201 Created status code match
        assert response.status_code == 201, f"Expected status code <201> but was <{response.status_code}>. Response: {response.text}"

        json_data = response.json()

        # Replaces: .body("id", notNullValue())
        assert json_data.get("id") is not None, "API Response validation failure: 'id' parameter is null or missing."

        # Dynamically caches the generated server tracking identifier to share with downstream verification steps
        TestData.user_id = str(json_data["id"])

        # Replaces: System.out.println("User Created");
        print("\nUser Created")
