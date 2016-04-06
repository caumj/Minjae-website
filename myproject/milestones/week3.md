# 3주 마일스톤

## 목표
웹사이트 완성시키기

## 설명
자, 이제 자주풀의 코어 기능들을 한번 더 다듬고 이제 마무리를 지어줍니다.

## 랜딩페이지
아직 예전 탬플렛에 사용했던 이미지들과 색깔들이 남아있으니 민재 만의 웹사이트로 만들어줍니다.

- `home/static/css/creative.css`의 153번줄에 header안에 있는 `../img/header.jpg`를 민재가 원하는 사진으로 변경해서 배경사진을 바꿔줍니다. 이거 어떻게 하는지 아버님한테 물어보세요.
- `home/templates/index.html`의 71줄에 있는 `section#portfolio`를 민재 서비스와 관련있는 스크린샷으로 변경해줍니다. 꼭 저 방식으로 스크린샷을 6개 보여줄 필요 없고 민재가 예전에 했던 숙제들을 참조해서 자주풀에서 어떤 모양의 시간표를 받을 수 있을지 사진으로 보여주세요.
  + 아니면 민재 사이트가 서비스를 제공하는 단계를 스크린샷으로 담으면 어떨까요? 예를 들면 주문하기 페이지에서 내용을 넣는 스크린샷(1), 예제 이메일 받는 스크린 샷(2), 시간표 스크린샷 (3).
- 크롬에서 F12를 누르고 맨 왼쪽 위에 있는 상자에 마우스가 들어간 아이콘을 누르고 웹사이트에 마우스를 올리면 영역을 선택할 수 있습니다. 그걸 선택해서 민재가 원하는 색깔로 바꿔주세요. 색깔이 css에서 어디 위치해있는지는 F12나온 공간에서 오른쪽에 있는 구간에서 확인해주세요.
- 민재가 만족할만큼 꾸며주세요.

## 로그인 페이지
로그인 인풋이 너무 위에 붙어 있고 너무 길게 생겼네요. 조정해줍니다.

- Sign in 한글로 번역해줍니다.
- `home/static/css/signin.css`를 변경해줍니다.
  + `form`에 padding-top을 이용해서 위와 거리를 둡니다.
  + `.container`의 width바꾸면 너비도 조정 가능 해요.
- 한번 로그인 실패해보세요. 에러메세지가 보입니다. 에러메세지도 스타일을 p.error를 이용해서 주세요.
- 버튼도 좀 예쁘게 바꿔주세요. 가입하기 페이지랑 같은 버튼으로 보이게!

## 어바웃 페이지
어바웃 페이지가 너무 비어있네요. 민재 자기소개와 사이트 만들게 된 동기들을 입력해줍니다.

## 주문하기 페이지
오더라고 부르지 말고 주문이라고 해주세요 ㅋㅋㅋ. 그리고 오더 폼에 인풋들의 placeholder를 좀 더 개선해주세요. `설명. 예제) XX` 이런 식으로 해야 유저가 뭘 입력해야 하는지 이해할꺼에요.

## 내 페이지
내 페이지에 주문 내역을 입력해야겠죠? 우선 `views.py`에서 주문들을 넘겨주도록 해요.

- `def user(request)`에서 다음처럼 유저의 주문들을 불러와서 넘겨줍니다.

```python
orders = Order.objects.filter(user=request.user).all()
return render(request, "user.html", { "orders": orders })
```

- `order.html`에서 `{{ request.user.username }}`옆에 유저 네임, `{{ request.user.email }}`옆에 이메일이라고 적어줍니다.
- 밑에 h3로 주문 내역을 추가하고 다음 처럼 받아온 주문들을 나열해줍니다.

```html
<ul class="list-group">
  {% for order in orders %}
  <li class="list-group-item">
    {{ order.purpose }}
  </li>
  {% endfor %}
</ul>
```

- 한번 민재가 직접 주문을 해보고 어떻게 보이는지 직접 확인해보세요.
- 자, 목적만 보이면 좀 그렇죠? order에는 다음과 같은 정보들이 있습니다.

```python
class Order(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.TextField()
    purpose = models.TextField()
    period = models.TextField()
    schedule = models.TextField()
    email = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)
```

- 여기서 다 이용할 필요는 없고 몇개만 (purpose, email, is_complete)만 뽑아서 span에 넣어줍니다.

```html
<!-- 예제 -->
<li class="list-group-item">
  <span class="purpose">{{ order.purpose }}</span>
  <span class="email">{{ order.email }}</span>
  <!-- 등등 -->
</li>
```

- 자 이제 `order.html`에서 list-group-item 안에 있는 span에 display inline-block과 width를 %로 적용해서 좀 정리되게 보여드립니다.

## 마음껏 꾸미기
이제 까지 배워본 css를 이용해서 최소 **3가지** 이상의 디자인 변경을 해주세요. 이미지를 넣든 사진을 넣든 지금 너무 심심해 보이니 좀 더 예쁘게 만들어봅시다.
