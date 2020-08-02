# kenkenjr

kenkenjr은 슈텔로의 관리를 위해 새로운 봇을 개발하는 프로젝트이다.

## 기록

기록의 각 행은 특수한 의미를 갖는 문자로 시작하며 한 문장으로 간결히 서술한다.

* `+`: 기능 추가
* `-`: 기능 제거
* `~`: 기능 수정
* `!`: 오류 발견
* `@`: 오류 수정
* `#`: 주석
* `\t`: 세부사항

repository를 만들기 이전의 기록은 다음과 같다. 

### 2020-07-15

```
# 프로젝트를 시작했다.
# kenken_the_bot 프로젝트에서 기본적인 기능을 복제했다.
+ 문자열 상수를 파일로부터 불러오는 literal 모듈을 추가했다.
+ after_ready, is_complete 등의 메소드를 정의하는 CustomCog 클래스를 추가했다.
~ BaseCog 클래스를 수정했다.
~ LogCog 클래스를 수정했다.
    # 오류 관련 로그 이외의 로그는 파일로 출력하지 않는다.
~ ProtocolCog 클래스를 수정했다.
~ Kenken 클래스를 수정했다.
```

### 2020-07-19

```
+ ControlCog 클래스를 추가했다.
+ ChainedEmbed 클래스를 추가했다.
+ 몇 개의 디랙토리에 __init__.py를 추가했다.
```

### 2020-07-20

```
+ HelpCog 클래스를 추가했다.
    + '검색' 명령어를 추가했다.
    + '도움말' 명령어를 추가했다.
    + '명령어' 명령어를 추가했다.
+ GameCog 클래스를 추가했다.
    ~ '왕' 명령어를 GameCog 클래스로 옮겼다.
~ '왕' 명령어가 문자열 대신 Embed를 전송하도록 수정했다.
```

### 2020-07-24

```
+ ShteloCog 클래스를 추가했다.
    + '가입신청서' 명령어를 추가했다.
    + '가입신청서 전체' 명령어를 추가했다.
```

### 2020-07-25

```
+ ShteloCog에 '가입신청서 원본' 명령어를 추가했다.
+ ShteloCog에 '가입신청서 원본 전체' 명령어를 추가했다.
```

### 2020-07-26

```
+ ShteloCog에 '회칙' 명령어를 추가했다.
+ ShteloCog에 '회칙 전체' 명령어를 추가했다.
```
