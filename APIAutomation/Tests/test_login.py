import pytest
import requests
import json
from APIAutomation.Base.Base_Test import BaseTest
from APIAutomation.Endpoints.EndPoints import EndPoints
from APIAutomation.Utils.Test_Data import TestData


class TestLogin(BaseTest):

    @pytest.mark.order(2)  # Injects this directly after the user creation sequence block
    def test_verify_user_login(self):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        # REPLACES given().log().all(): Explicitly prints request payload metadata beforehand
        print("\n=================================")
        print("REQUEST LOGS")
        print("=================================")
        print(f"URL Target: {EndPoints.LOGIN}")
        print(f"Headers Specification: {json.dumps(self.headers, indent=4)}")
        print(f"Payload Body Content: {json.dumps(payload, indent=4)}")

        response = requests.post(EndPoints.LOGIN, json=payload, headers=self.headers)

        # REPLACES your Java System.out.println trace blocks exactly
        print("=================================")
        print("LOGIN RESPONSE")
        print("=================================")
        print(f"Status Code: {response.status_code}")
        print("Response Body:")
        try:
            # Replaces: response.getBody().asPrettyString() using indentation parameters
            print(json.dumps(response.json(), indent=4))
        except Exception:
            print(response.text)
        print("=================================")

        # Asserts authentication success code metrics validation parameters cleanly
        assert response.status_code == 200, f"Authentication block failed with response error string: {response.text}"

        # Capture token dynamically to store inside shared memory class properties if required
        json_data = response.json()
        if "token" in json_data:
            TestData.auth_token = json_data["token"]
