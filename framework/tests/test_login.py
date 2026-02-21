def test_invalid_login_api_simulation():
    simulated_status_code = 401
    assert simulated_status_code == 200

def test_valid_login_simulation():
    simulated_status_code = 200
    assert simulated_status_code == 200