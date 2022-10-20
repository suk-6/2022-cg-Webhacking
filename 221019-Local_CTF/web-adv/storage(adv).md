# Storage (Adv)
일반 Storage 문제와 별로 다를 바 없어 보이지만, 훨씬 어렵다.

web-root 폴더에 있는 flag.py는 Fake Flag이다.

flag는 Liunx 어딘가에 있겠지만 소스코드를 보았을 때 read 페이지에서는 디렉토리를 조회할 수 없다.

그 얘기는 flag가 들어있는 파일 명을 알 수 없다는 얘기다.

그러다 소스코드에서 아래 부분을 발견했다.

```python
@APP.route('/')
def index():
    files = os.listdir(UPLOAD_DIR)
    return render_template('index.html', files=files)

@APP.route('/<path:path>')
def list_memo(path):
    files = os.listdir(path)
    return render_template('index.html', files=files)
```

`/`로 접속하면 `UPLOAD_DIR`의 `listdir`을 반환하지만 `/{path}`로 접근하면 그 path의 `listdir`을 조회해준다는 코드였다.

이 코드와 Burp Suite를 활용해 최상위 폴더의 디렉토리를 조회했다.

```
~~
flagggggggg_1q1q1q1q1q1q1q1q1q1q1q
```

이렇게 flag의 파일명을 찾았고, read 페이지를 통해 flag를 얻었다.

## Flag
flag{my_frutiy_sweety_flag}