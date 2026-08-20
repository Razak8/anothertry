import requests



def check_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    return response.status_code == 200

def test_octocat():
    assert check_user("octocat") == True

def test_google():
    assert check_user("google") == True

def test_razak8():
    assert check_user("razak8") == True

def test_razak15():
    assert check_user("razak15") == False

def test_defunkt():
    assert check_user("defunkt") == True

def test_unknown():
    assert check_user("qwertyuiop") == False