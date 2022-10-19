# locks
이 서버는 GET, POST, UNLOCK, MOVE method를 받는데, POST 메소드로 /buy에 id를 담아서 전송하면 locks에 id가 추가된다.

그 후 UNLOCK 메소드로 "/:id"에 접근하면, id가 unlock 된다. 그리고 MOVE 메소드로 "/:id"에 접근하면, Flag가 나온다.

# Flag
flag{beep_beep_beep_beep_beep_beep}