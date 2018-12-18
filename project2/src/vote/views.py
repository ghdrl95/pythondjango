from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

from django.http.response import HttpResponseRedirect
from django.urls import reverse
#return HttpResponseRedirect(URL 문자열) : URL 문자열을 리다이렉트 해주는 클래스
#ex) return HttpResponseRedirect('127.0.0.1:8000/vote/')
#-> 웹클라이언트는 HTML문서가 아닌 '127.0.0.1:8000/vote/' 주소를 받음. 받은 주소로 서버에 재요청함

#reverse(별칭 문자열) : 해당별칭을 가진 URL을 반환함
#ex) reverse('vote:index') -> '127.0.0.1:8000/vote/' 를 반환

#return HttpResponseRedirect( reverse( '별칭 문자열' ) )

#index(질문 리스트)
def index(request):
    #Question 객체들을 추출
    objs = Question.objects.all()
    #render 호출 및 수정된 html 문서 반환
    return render(request, 'vote/index.html', { 'a' : objs })

#detail(질문 선택 시 답변항목 제공)
def detail(request, q_id):
    obj = get_object_or_404(Question, id = q_id) #id와 pk는 동일한 의미 #pk=q_id
    return render(request,'vote/detail.html', {'q' : obj } )

#vote(웹 클라이언트의 요청에 따라 투표수 증가)
def vote(request):
    if request.method == "POST": #사용자 요청이 post방식인 경우에 투표 처리를 함
        #request.POST : POST방식으로 요청하면서 넘어온 데이터의 집합
        #request.POST.get(키값) : 키값은 입력양식의  name 속성에 문자열과 동일하게 작성
        c_id = request.POST.get('select')
        #Choice 객체 중 id 변수값이 c_id와 동일한 객체를 찾아 추출
        c = get_object_or_404(Choice, id = c_id)
        c.votes += 1 #해당 객체의 votes 변수값을 1증가
        c.save()     #변동사항을 데이터베이스에 반영
        #결과 뷰의 URL을 반환
        return HttpResponseRedirect( 
               reverse('vote:result', args=(c.question.id,))  )
    else: #잘못된 클라이언트 접근 처리
        # 'vote:index' 별칭을 가진 URL을 찾아 웹 클라이언트에게 전달
        return HttpResponseRedirect( reverse('vote:index')  )

#result(투표 결과 화면)
def result(request, q_id):
    obj = get_object_or_404(Question, id = q_id)
    return render(request, 'vote/result.html', {'q' : obj})












