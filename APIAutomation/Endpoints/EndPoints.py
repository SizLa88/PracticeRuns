from APIAutomation.Utils.Config_Reader import ConfigReader

class EndPoints:

    base_url = ConfigReader.get_property("base.url")

    # Fallback if nothing is found in config
    if not base_url:
        base_url = "https://reqres.in/api"

    # Ensure URL ends with /api
    if not base_url.endswith("/api"):
        base_url = f"{base_url}/api"

    BASE_URL = base_url

    USERS = f"{BASE_URL}/users"
    LOGIN = f"{BASE_URL}/login"