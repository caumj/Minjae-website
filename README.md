# 민재의 시간표 만들어주는 웹사이트 프로젝트

## 가이드

* [히로쿠/장고로 새롭게 프로젝트를 시작하는 방법](/docs/heroku-django-start-guide.md)
* [장고로 프로젝트를 시작하는 방법](/docs/django-start-guide.md)
* [히로쿠로 출시하는 방법](/docs/heroku-deploy-guide.md)

## 참고자료

- [부트스트랩](http://bootstrapk.com/)

## 3주 완성 마일스톤

민재의 웹사이트는 정보를 보여주고 회원가입을 하고 데이터를 올리는 웹사이트입니다. 사이트에는 다음과 같은 페이지들이 있습니다.
- 랜딩페이지: 서비스 이름과 간단한 소개가 있는 페이지
- 회원가입 페이지: 회원가입을 할 수 있는 페이지
- 로그인 페이지: 로그인을 할 수 있는 페이지
- 사용방법/주문 페이지: 주문을 할 수 있는 페이지
- 유저 페이지: 유저의 주문 내역을 볼 수 있는 페이지
- 소개 페이지: 민재의 개인 소개가 들어간 페이지

### 1주
목표: HTML 내용 완성시키기

아직은 디자인은 신경쓰지 말고 내용부터 입력하면서 만들기로 할께요. 총 6페이지에 있는 모든 내용을 다 채워야 하니 분량이 많습니다. 각오하세요!

- 우선 민재는 여러 페이지를 만들꺼니 `template`폴더안에 `base.html`을 만들어봅시다. `base.html`은 다음 과 같이 작성해주세요.

```html
<!-- base.html -->
{% load staticfiles %}

<!DOCTYPE html>
<html lang="en">
  <head>
    (이 안에 있는 모든 내용)
  </head>
  <body id="page-top">
    <nav id="mainNav" class="navbar navbar-default navbar-fixed-top">
      (이 안에 있는 모든 내용)
    </nav>
    {% block content %}
    {% endblock %}
    <script ... /> (script로 불러오는 부분은 공통적으로 할꺼니 여기 남김니다.)
  </body>
</html>
```

- 그리고 `index.html`을 다음 과 같이 바꿔줍니다.

```html
{% extends "home/base.html" %}

{% block content %}
(아까 nav와 script사이에 있었던 모든 코드)
{% endblock %}
```

- 그렇게 해서 다음 과 같은 여러개 `html`들을 만들어줍니다.
  + signup.html (회원가입)
  + signin.html (로그인)
  + order.html (주문)
  + user.html (유저)
  + about.html (소개)
  + 위 페이지들은 다음과 같이만 채워주세요.

```html
<!-- signup.html, signin.html, order.html, user.html, about.html -->
{% extends "home/base.html" %}

{% block content %}
(여기는 비워두세요. 앞으로 내용을 채울꺼에요.)
{% endblock %}
```

- 자 이제 랜딩페이지 내용을 채우기 시작할께요.
  + `header`는 냅두세요.
  + `section#about`엔 민재 웹사이트에서 정확이 어떤것을 할 수 있는지 적어주세요.
    * 예제) 구글 스프레드시트를 이용해서 당신만의 시간표를 만들어드립니다!
  + `section#services`에선 민재 스케쥴을 씀으로서 오는 장점 3-4가지를 넣어주세요.
    * 4가지면 `col-md-3`, 3가지면 `col-md-4`인건 알고있죠?
  + `section#portfolio`에선 기존 사진 지우고 민재가 구글 스프래드 시트로 만든 예제 시간표 3가지를 스크린샷을 찍어서 올리면 좋겠네요. 콘텐츠는 많으면 많을수록 웹사이트는 더 완성되보입니다!
  + `aside`는 민재 서비스를 이용해달라고 한번 더 상기해주세요.
    * 예제) 지금 당장 당신만의 스케쥴표를 만들어보세요! (시작하기)
  + `section#contact`는 없애거나 아니면 민재의 연락처 정보를 넣어주세요.

- 회원가입 페이지는 가입 `form`만 넣겠습니다. 물론 {% block content %}와 {% endblock %}사이에 넣으면 됩니다.
  + 필요하면 `h1`으로 타이틀을 적어주세요.
  + 폼은 7번째 숙제에서 한번 접했을꺼에요. 다음 과 같습니다.

```html
<form>
  <div class="form-group">
    <label for="username">아이디</label> <!-- 같은 form-group내의 for하고 id는 일치해야합니다. -->
    <input type="text" class="form-control" id="username">
  </div>
  <div class="form-group">
    <label for="email">이메일</label>
    <input type="email" class="form-control" id="email">
  </div>
  <div class="form-group">
    <label for="password">비밀번호</label>
    <input type="password" class="form-control" id="password">
  </div>
  <div class="form-group">
    <label for="password2">비밀번호 확인</label>
    <input type="password" class="form-control" id="password2">
  </div>
  (더 추가하고 싶으면 민재가 넣어주세요.)
  <button type="submit" class="btn">가입하기</button>
</form>
```
- `form`에 관련된 내용은 [부트스트랩 페이지](http://bootstrapk.com/css/#forms)에서 확인하세요.

- 로그인 페이지도 회원가입 페이지처럼 `form` 넣지만 아이디하고 비밀번호하고 버튼만 있으면 됩니다.

- 주문 페이지은 내용과 `form`과 함께 들어갈겁니다. 우선 사용방법을 글과 스크린샷을 이용해서 최대한 이해하기 쉽게 표현해보세요.
  + 예제) 우선 저희 서비스를 이용하려면 구글 계정이 필요합니다. 다음 링크를 클릭해서 시간표 템플릿을 확인해주세요. 그리고 그 페이지에서 메뉴를 눌러 사본을 만든 후 자신의 스케쥴을 넣고 주문시 입력해주시길 바랍니다. 어쩌구 저쩌구...
  + 시간 많이 걸리는 작업입니다. 그 이유는 민재 웹사이트의 메인 서비스 내용이 여기 다 담겨져 있어서 그렇습니다.
  + `form`도 기획한데로 작성해주세요.

- 유저 페이지는 아직 데이터를 서버에서 보내주진 않지만 마치 받았다는 듯이 생각하고 작성해주세요. 아마 요청 내역들도 리스트로 보여야겠죠? 스타일은 [부트스트랩](http://bootstrapk.com/)을 참조해주세요.

- 자기 소개 페이지도 여러가지 태그를 이용해서 간략하게 적어주세요.

### 2주
목표: 서버 완성시키기

### 3주
목표: 나만의 스타일을 적용하고 완성시키기
