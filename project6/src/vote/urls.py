'''
Created on 2018. 10. 21.

@author: user
'''

from django.urls import path
from .views import index, detail, vote, result, questionregister, questionUpdate, questionDelete, choiceDelete, choiceRegiste,choiceUpdate
#app_name : 하위 URL 파일의 그룹이름
app_name = 'vote'
#urlpatterns : path함수를 이용해 url 등록
#도메인 주소 : 127.0.0.1:8000/vote/
urlpatterns = [
    #127.0.0.1:8000/vote/   
    path('', index, name = 'index'),
    path('<int:q_id>/',detail,name='detail'),
    path('vote/',vote, name='vote'),
    path('result/<int:q_id>/', result,name='result'),
    path('questionr/', questionregister, name='qr'),
    path('questionu/<int:question_id>/',questionUpdate, name='qu'),
    #questionDelete 함수 등록하기 별칭 'qd'로 지정하기
    path('questiond/<int:q_id>/', questionDelete,name='qd'),
    path('choided/<int:c_id>/', choiceDelete, name= 'cd'),
    path('choicer/', choiceRegiste, name='cr'),
    path('choiceu/<int:c_id>/', choiceUpdate, name='cu'),
]





