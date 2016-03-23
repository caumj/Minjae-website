# 2주 마일스톤

## 목표
서버 로직 완성시키기

## 설명
자주풀이 정상적인 서비스를 제공해줄 수 있는 모든 기능들을 다 구현해야 합니다. 다음 기능들을 완성시킬겁니다.

- 회원가입 (수업시간에 완료)
- 로그인
- 로그아웃
- 주문하기
- 유저페이지에서 주문 내역 보기

## 로그인
`signup.html`에 했던것처럼 `signin.html`도 변경해줍니다.

### `home/templates/signin.html`
- `form`에 `method="post"`를 추가해주세요.
- `form`안에 `{% csrf_token $}`을 추가해주세요.
- 여기 [링크](http://bootstrapk.com/css/#forms)를 참조해서 자신이 원하는 방식의 폼을 만들어보세요!

### `home/view.py`
- `views.py`에서 `def signin(request):`를 `def signup(request):`처럼 바꿉니다.
- 똑같이 `request.method`가 `POST`인지 `if`로 확인합니다.
- 유저네임과 이메일만 가져오면 됩니다.
- 자, 로그인을 하기전에 유저 인증을 해야하는데요, 지름길이 있습니다.

```python
from django.contrib.auth import authenticate

user = authenticate(username=username, password=password)
```

- 여기서 유저 인증이 완료되면 user를 불러오고 아니면 None을 불러옵니다. `if user is not None:`을 이용해서 로그인을 할지 에러메세지를 보낼지 결정해줍니다.
- 로그인은 이렇게 합니다.

```python
from django.contrib.auth import login

login(request, user)
```

- 로그인이 끝나면 `user`뷰로 `redirect`를 해줍니다.

## 로그아웃
로그인을 해줬으면 로그아웃도 해줄 수 있어야 합니다. 따로 html을 만들필욘 없어요.

### `home/views.py`
- 밑에 로그아웃 뷰를 만들어줍니다.
- 로그아웃은 이렇게 하면 됩니다.

```python
from django.contrib.auth import logout

logout(request)
```

- 로그아웃이 끝나면 `index`뷰로 redirect해줍니다.

### `home/urls.py`
- `/signout`으로 가면 로그아웃을 진행하게끔 만들어주세요.

## 로그인 테스트
- 로그인을 하면 상태가 어떻게 바뀌냐고요? index뷰에 `print request.user`을 하고 브라우저로 index페이지로 간 후 콘솔에 있는 로그를 확인해보세요.
- 로그인을 하고 다시 index로 가서 어떤 값인지 확인해보세요.
- 주소창에 `localhost:8000/signout`이라고 친 후 다시 index로 가서 어떤 값인지 확인해보세요.
- 이걸 이용해서 로그인/로그아웃 상태를 표시할 수 있습니다.

## 주문하기
주문 내역이 민재의 데이터가 될거에요. 먼저 주문이라는 모델부터 만들러 갑시다.

### `home/models.py`
자 여기서 민재의 주문 모델을 만들어봅니다. 아래를 참조하세요.

```python
from django.db import models
from django.utils import timezone


class Question(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    answer = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
```

아마 민재가 필요한 것은 주문을 한 사람(user), 이메일, 주문 디테일 등등 데이터일거에요. Question대신 Order로 이름을 지어주세요.

### `home/admin.py`
방금 만든 모델을 어드민에 등록해주니다.

```python
from .models import Order
admin.site.register(Order)
```

### 주문 모델이 만들여졌는지 확인하기
`python manage.py migrate`을 치면 마이그레이션이 완성됩니다. 완성 후 어드민으로 들어가서 User말고 Order도 추가됬는지 확인해보세요.

### `home/templates/order.html`, `home/views.py`
회원가입과 로그인때 했던것처럼 `order.html`에서 폼을 만들고 보내서 `views.py`에서 데이터를 받고 주문을 만들어 주면 됩니다. `input`말고 `textarea`을 쓰면 더 많은 내용을 입력할 수 있습니다. [링크](http://bootstrapk.com/css/#forms)를 다시 참조해서 자신이 원하는 방식의 폼을 만들어보세요!

`views.py`에서 받은 데이털르 처리하는 방식입니다.

```python
from .models import Order

# user를 request.user로 주면 현재 로그인한 사람이 주문한 사람이 됩니다.
order = Order(
  user=request.user,
  ...)

# 여기 ...은 민재가 받아온 데이터를 넣어주세요.
order.save()
```

주문이 완료되면 유저페이지로 redirect하면 좋겠네요!

> 어렵고 도중에 막히는 부분이 많더라도 도중에 물어보면서 해결해보세요!
