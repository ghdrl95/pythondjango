from django.shortcuts import render

#View : 사용자의 요청에 따라 처리하고, HTML 문서나 새로운 URL 주소를 전송 역할

#View 정의 시 클래스/함수 형태로 정의

#View 함수 정의 시 첫번째 매개변수로 request를 반드시 사용함
# request : 사용자의 요청 정보, <form>으로 넘겨준 데이터, 로그인정보, 세션정보, 요청방식(GET,POST)

#HTML 전송하는 메인페이지
def index(request):
    #render(request, HTML문서의 경로, HTML문서에 전달할 값(사전형) )
    #현재 요청을 한 웹 클라이언트에게 HTML 파일을 전달하는 함수
    #HTML 문서에게 값을 전달하고 싶은 경우 3번째 매개변수에 사전형으로 값을 전달할 수 있음
    #사전형에서 사용한 '키'값은 HTML문서 내에서 변수이름처럼 사용 가능 
    
    return render(request, 'bookmark/index.html',{ 'a' : 'Hello Django',
                                                  'b' : [1,2,3] })
#해당 모델클래스에 저장된 객체들을 추출하기 위해서 임포트
from .models import BookMark

#북마크 모델클래스에 저장된 객체를 HTML 문서에 전달하는 기능
def booklist(request):
    #모델클래스명.objects.all() : 데이터베이스에 해당 모델클래스로 저장된 모든 객체를 리스트 형태 추출
    #모델클래스명.objects.get() : 해당 모델클래스에 객체 중 특정 조건을 만족하는 객체 1개를 추출 
    #모델클래스명.objects.filter() : 특정 조건을 만족하는 다수의 객체를 리스트형태로 추출
    #                 .exclude() : 특정 조건을 만족하지않는 다수의 객체를 리스트형태로 추출
    
    objs = BookMark.objects.all() #데이터베이스에 저장된 BookMark 모델클래스의 객체를 모두 추출
    
    return render(request,'bookmark/booklist.html', {'list' : objs })

#북마크 객체에 저장된 값 하나를 출력하는 뷰 기능
#뷰함수에서 URL에 특정 영역을 매개변수로 활용할 수 있음
def bookdetail(request, book_id ):
    #get : 객체 한개를 추출
    #get함수의 인자값은 해당 모델클래스의 변수명을 사용
    #객체들을 식별하기 위한 id변수가 자동으로 생성되 특정객체를 추출할 때 사용할 수 있음
    #조건을 만족하는 객체가 한개도 없는 경우, 서버에러가 발생함
    
    #북마크 객체중 한개를 추출
    #북마크 객체들 중 id변수에 book_id값과 동일한 객체 한개를 추출
    obj = BookMark.objects.get(id=book_id)
    #HTML 문서에 추출한 객체를 넘겨줌
    return render(request, 'bookmark/bookdetail.html', {'obj' : obj })








