import requests
import pytest

# Улучшенная функция проверки пользователя
def check_user(username):
    """
    Проверяет существование пользователя на GitHub.
    Возвращает:
      True  - если пользователь найден
      False - если пользователь не найден (статус 404)
    Выбрасывает исключение, если произошла ошибка сети или сервера.
    """
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        else:
            # Любой другой статус (500, 503, 403 и т.д.) считаем ошибкой
            raise Exception(f"Сервер вернул неожиданный статус: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        # Ошибка соединения, таймаут и т.п.
        raise Exception(f"Ошибка сети при проверке пользователя {username}: {e}")

# ---------- Тесты ----------

def test_octocat():
    assert check_user("octocat") == True, "❌ Ошибка: octocat должен существовать"

def test_google():
    assert check_user("google") == True, "❌ Ошибка: google должен существовать"

def test_razak8():
    assert check_user("razak8") == True, "❌ Ошибка: razak8 должен существовать"

def test_razak15():
    # Ожидаем, что пользователь НЕ существует
    assert check_user("razak15") == False, "❌ Ошибка: razak15 не должен существовать"

def test_defunkt():
    # Ожидаем, что пользователь существует
    assert check_user("defunkt") == True, "❌ Ошибка: defunkt должен существовать"

def test_unknown():
    # Ожидаем, что пользователь НЕ существует
    assert check_user("qwertyuiop") == False, "❌ Ошибка: qwertyuiop не должен существовать"

