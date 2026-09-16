import pytest
import requests
from APIAutomation.Base.Base_Test import BaseTest
from APIAutomation.Endpoints.EndPoints import EndPoints
from APIAutomation.Utils.Test_Data import TestData

class TestDeleteUser(BaseTest):

    @pytest.mark.order(3)  # Executes sequentially as the cleanup check
    def test_verify_user_deletion(self):
        # Fallback parameters target standard client entry index 2 if running in an isolated context block
        target_id = TestData.user_id if TestData.user_id else "2"

        # Builds the full path string natively matching: EndPoints.USERS + "/2"
        delete_url = f"{EndPoints.USERS}/{target_id}"

        response = requests.delete(delete_url, headers=self.headers)

        # Asserts status code 204 No Content, confirming successful resource erasure from host databases
        assert response.status_code == 204, f"Expected status code <204> but was <{response.status_code}>. Response: {response.text}"

        print("\nUser Deleted")
