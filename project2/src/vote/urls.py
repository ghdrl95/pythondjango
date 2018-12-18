'''
Created on 2018. 10. 21.

@author: user
'''

from django.urls import path
from .views import index, detail, vote, result
#app_name : 하위 URL 파일의 그룹이름
app_name = 'vote'
#urlpatterns : path함수를 이용해 url 등록
#도메인 주소 : 127.0.0.1:8000/vote/
urlpatterns = [
    #127.0.0.1:8000/vote/   
    path('', index, name = 'index'),
    path('<int:q_id>/',detail,name='detail'),
    path('vote/',vote, name='vote'),
    path('result/<int:q_id>/', result,name='result')
]





