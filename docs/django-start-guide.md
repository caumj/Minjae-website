# 장고로 프로젝트를 시작하는 방법

장고로 프로젝트를 만드는 방법을 다음 가이드입니다. [히로쿠/장고로 새롭게 프로젝트를 시작하는 방법](./heroku-django-start-guide.md)을 보고 이어서 하셔도 됩니다. 만약 에러가 생기면 스크린샷으로 캡쳐해서 jeong1135@gmail.com로 물어보시길 바랍니다.

- 장고 프로젝트를 만들 곳으로 `Console`를 이용해서 갑니다.

- 장고 프로젝트를 만들어줍니다.
  + (히로쿠로 할꺼면 히로쿠 가이드 참조)
  + myproject 말고 다른 이름으로 해도 괜찮음

```bash
django-admin startproject myproject
```

- 만들어진 폴더 안으로 들어갑니다.

- 기본 장고앱을 하나 만들어줍니다.
  + home 말고 다른 이름으로 해도 괜찮음

```bash
python manage.py createapp home
```

- `myproject/myproject/settings.py`에 `home` app을 다음과 같이 추가해줍니다.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]
```

- `myproject/myproject/urls.py`에 다음처럼 변경해줍니다.

```python
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls')),
]
```

- `myproject/home/views.py`에서 예제 뷰를 하나 추가해줍니다.

```python
from django.shortcuts import render


def index(request):
    return render(request, "index.html")
```

- `myproject/home/templates/index.html`을 추가하고 다음 기본 html을 추가해줍니다.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Starter Template for Bootstrap</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  </head>
  <body>
  </body>
</html>
```

- 이제 `myproject/home/urls.py`를 만들어서 다음을 입력해줍니다.

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

- 자 이제 `Console`로 `manage.py`가 있는 폴더로 가서 서버를 실행시킵니다.

```bash
python manage.py runserver
```

- `http://127.0.0.1:8000`를 입력해서 서버가 잘 돌아가는지 확인해 줍니다.
