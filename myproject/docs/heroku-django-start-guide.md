# 히로쿠/장고로 새롭게 프로젝트를 시작하는 방법

히로쿠 출시용으로 웹사이트를 만들고 싶다고요? 다음과 같이 따라해주세요. 이 과정은 프로젝트를 시작할때 단 한번만 하면 됩니다. 만약 에러가 생기면 스크린샷으로 캡쳐해서 jeong1135@gmail.com로 물어보시길 바랍니다.

- Github에서 Repository만들기
  + 필수 사항은 아니지만 왠만한 프로젝트는 클라우드에 저장하는게 좋습니다.
  + [Github](https://github.com/)에 들어가서 로그인 한 후 녹색 `+ New Repository`를 클릭해서 기본 정보를 입력한 후 레포를 만들어주세요.
  + 만들고나면 복사할 수 있는 주소가 있습니다. SourceTree를 이용해서 Clone/클론을 눌러 주소를 붙여넣고 레포를 컴퓨터에 생성해주세요.
  + 이 과정이 기억이 안나면 이메일로 물어보세요!

- 만일 컴퓨터에 히로쿠 툴벨트가 설치되지 않으면 [여기](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)를 클릭해서 설치해주시길 바랍니다.

- 클론된 폴더안에 `Console`로 접근해서 다음 과 같은 코맨드를 입력합니다.

```bash
django-admin startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile myproject
```

- `startproject`이후의 단계는 [장고로 프로젝트를 시작하는 방법](./django-start-guide.md)을 참조하시길 바랍니다.

- 이제 코맨드를 이용해 히로쿠 로그인을 합니다.

```bash
heroku login
# 그 이후 이메일과 비밀번호 입력
```

- SourceTree를 이용해서 생성된 파일 모두 `Commit`과 `Push`를 합니다.

- 히로쿠를 셋업합니다.

```bash
heroku create
```

- 나머지 단계는 [히로쿠로 출시하는 방법](./heroku-deploy-guide.md)를 참조해주세요.
