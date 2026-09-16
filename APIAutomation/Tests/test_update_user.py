import pytest
import requests
from APIAutomation.Base.Base_Test import BaseTest
from APIAutomation.Endpoints.EndPoints import EndPoints
from APIAutomation.Utils.Test_Data import TestData

class TestUpdateUser(BaseTest):

    @pytest.mark.order(3)  # Loops sequentially directly following the login token check
    def test_verify_user_update(self):
        payload = {
            "name": "Sizwe",
            "job": "Senior Automation Tester"
        }

        # Fallback values prioritize your dynamic user_id token before checking base entries
        target_id = TestData.user_id if TestData.user_id else "2"
        update_url = f"{EndPoints.USERS}/{target_id}"

        response = requests.put(update_url, json=payload, headers=self.headers)

        # Replaces: .then().statusCode(200);
        assert response.status_code == 200, f"Expected status code <200> but was <{response.status_code}>. Response: {response.text}"

        # Replaces: System.out.println("User Updated");
        print("\nUser Updated")
