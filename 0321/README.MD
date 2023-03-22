Static File
- 변하지 않는 파일

Media File
- 미디어파일
- 사용자가 웹에서 업로드하는 정적 

장고에서는 Static File과 Media File을 구분해서 관리한다.

<hr>

## 웹서버와 정적파일

클라이언트가 서버에 요청할때 url로 요청한다. 서버가 자신의 경로를 그대로 반환하면 옳은 response가 아님. 서버는 이미지에 접근 가능한 url을 줘야함. 

`STATIC_URL`
- `INSTALLED_APPS`에 `django.contrib.staticfiles` 포함되어있는지 확인하기
- settings.py에 `STATIC_URL`에 적용하기
- 앱의 static 폴더에 정적파일을 위치하기
- 탬플릿에서 static 템플릿태그 `{% load static %}` 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기
- 부트스트랩은 CDN을 이용해서 그냥 되었던것

Static files 관련 Settings
1. STATIC_ROOT: 배포할때 스태틱 파일을 한곳에 모아두기 위해서 설정 굳이 필요 x
2. STATICFILES_DIRS: 앱 안쪽이 아닌 다른곳에 스태틱 파일을 두고 싶을때 경로 설정 굳이 필요 x
3. STATIC_URL: 스태틱파일들에 대해서 URL 맵핑 할 때 URL 에서 사용할 경로 지정
   
