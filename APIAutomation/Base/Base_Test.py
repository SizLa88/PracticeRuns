class BaseTest:
    # Replaces RequestSpecBuilder setup() content-type configurations natively
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
