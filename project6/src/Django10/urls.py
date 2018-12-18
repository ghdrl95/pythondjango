"""Django10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404,handler500

from bookmark.views import *

#404에러 발생시 호출할 뷰 함수
handler404 = 'Django10.views.handler404'
handler500 = 'Django10.views.handler500'

#handler404 = 'Django10.views.handler404'
#urlpatterns : URL과 뷰함수를 등록 및 관리하는 변수
#URL 등록 시 path함수를 이용해 urlpatterns의 요소를 추가
#path(URL주소(문자열), 뷰함수/클래스 이름) : 등록한 문자열로 클라이언트가 요청시, 뷰함수/클래스가 호출됨
#웹 서버 실행 시 나오는 도메인 주소(127.0.0.1:8000)은 기본값이므로 생략됨
urlpatterns = [
    #127.0.0.1:8000/hello
    path('hello/', admin.site.urls),
    #127.0.0.1:8000 으로 요청시 북마크에 있는 index함수가 호출됨
    path('', index, name='index'),
    #127.0.0.1:8000/booklist/
    path('booklist/',booklist, name='booklist'),
    #127.0.0.1:8000/booklist/1
    #127.0.0.1:8000/booklist/2
    #127.0.0.1:8000/booklist/3
    #URL의 숫자데이터는 'book_id' 매개변수에 저장됨 
    path('booklist/<int:book_id>/', bookdetail, name='bookdetail'),
    #127.0.0.1:8000/vote/ 로 요청하는 모든 URL은 vote폴더안에 있는 urls가 처리함
    path('vote/', include('vote.urls')),
    path('cl/', include('customlogin.urls', namespace='cl' )),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('blog/', include('blog.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
#URL 주소와 실제 저장된 파일 경로를 매칭 및 등록
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)











