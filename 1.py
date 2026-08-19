import requests 
username = "razak8"  #строка с вводом имени пользователя GitHub
response = requests.get(f'https://api.github.com/users/{username}') #данные из запроса к API GitHub

if response.status_code == 200: #если статус ответа 200 то-
    data = response.json() #ответ преобразуется в JSON
    if 'login' in data: #если в данных есть username, то-
        print(f"✅ Тест пройден, найден {data['login']}  и пойман за руку как дешевка!")  #выводим что тест пройден
else:
    print(f"❌ Ошибка: статус {response.status_code}")  #в ином случае выводим ошибку с кодом статуса