import requests
users = ["octocat", "google", "defunkt", "razak8", "razak9"]
for username in users: 
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        print(f"✅ Тест пройден, найден {username} !")
    else:
     print(f"❌ Ошибка: статус {response.status_code}")