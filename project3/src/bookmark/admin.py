from django.contrib import admin
#현재 폴더에 있는 models.py에 BookMark 클래스를 임포트
from .models import BookMark 
#from bookmark.models import BookMark


#관리자 사이트에서 해당 어플리케이션의 모델클래스를 추가/수정/삭제 할 수 있도록 등록하는 파일
#admin.site.register(클래스명) 형태로 추가함

admin.site.register(BookMark)
