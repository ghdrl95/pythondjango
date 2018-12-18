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

from django.contrib.auth.decorators import login_required



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

from .forms import QuestionForm, ChoiceForm #모델폼클래스를 사용하기 위해서 임포트
from _datetime import datetime #현재 날짜/시간을 불러오는 파이썬 모듈

#질문 등록 뷰
@login_required
def questionregister(request):
    if request.method == "GET":#클라이언트가 해당 뷰를 처음 호출했을 경우
        #폼클래스의 객체 생성. 인자값을 전달하지 않은경우 입력양식에 값이 비어있는 형태의 객체를 생성 
        form1 = QuestionForm()  
        print( form1.as_p() )
        
        return render(request, 'vote/qr.html', {'a' : form1 })
    elif request.method == "POST":#클라이언트가 해당 뷰로 데이터를 보낸 경우
        #request.POST : POST방식으로 요청한 클라이언트의 데이터가 들어있는 변수
        #사용자 입력을 해당 폼객체 생성시 넣을 수 있음
        form1 = QuestionForm( request.POST )
        if form1.is_valid(): #사용자가 입력한 값이 유효한 값인지 확인
            #폼객체.cleaned_data : is_valid() 함수로 유효한 값인지 확인한 후 True가 반환됬을 때,
            #사용자의 입력정보를 확인할 수 있는 사전형 변수 
            print ('등록하려는 설문지 제목',  form1.cleaned_data['name'])
            #폼객체.save() : 사용자가 입력한 데이터를 기반으로 연결된 모델클래스의 객체를 데이터베이스에 생성
            #form1.save() -> 사용자가 입력한 데이터로 Question 객체 생성/반환 및 데이터베이스에 저장
            #form1.save(commit = False) -> 사용자가 입력한 데이터로 Question 객체 생성 및 반환
            
            #Question 객체는 date 변수에 값이 비어있으면 안되므로, 파이썬 코드로 변수값을 채워준 뒤에 저장해야함
            q = form1.save(commit = False) #QuestionForm 객체로 Question객체를 생성(데이터베이스저장X)     
            print('생성된 Question 객체', q)
            q.date = datetime.now() #파이썬 모듈을 이용해서 현재시간을 Question객체의 date변수에 저장
            q.save()                #생성된 새로운 Question 객체를 데이터베이스에 저장
            
            #객체 생성이 끝난 후 vote그룹의 index 별칭의 URL을 클라이언트에게 전달
            return HttpResponseRedirect( reverse('vote:index') )
        else: #사용자가 입력한 값이 유효한 값이 아닌경우에 대한 처리
            #사용자가 입력한 데이터를 바탕으로 입력양식을 제공하는 HTML 문서 전달
            return render(request, 'vote/qr.html', {'a' : form1,
                                                    'error' : "유효하지않은 값을 작성했습니다." })
#질문 수정 뷰
#어떤 Question 객체를 수정 요청했는지 알아야하므로 매개변수 추가
@login_required
def questionUpdate(request, question_id):
    obj = get_object_or_404(Question, id = question_id)
    if request.method == "GET":
        #데이터베이스에 저장된 Question객체의 정보를 기반으로 모델폼 객체를 생성
        form1 = QuestionForm(instance = obj)
        return render(request, "vote/qu.html", {'b' : form1})
    elif request.method == "POST":
        #기존 객체에 저장된 정보를 사용자의 입력 데이터로 변경한 모델폼 객체를 생성
        form1 = QuestionForm(request.POST, instance = obj)
        if form1.is_valid():#수정한 값이 유효한 값인지 확인
            #모델 폼 객체와 연결된 모델 객체의 데이터를 변경해 데이터베이스에 저장
            b = form1.save() #변경할 사항이 없으므로 save함수 호출해 데이터베이스에 저장
            print(obj)
            print(b)
            return HttpResponseRedirect( reverse('vote:detail', args=(b.id,) ) )
        else:
            return render(request, 'vote/qu.html', {'b': form1})
#질문 삭제 뷰
@login_required
def questionDelete(request, q_id):
    #삭제할 객체 찾기
    obj = get_object_or_404(Question, id = q_id)
    obj.delete() #해당 객체를 데이터베이스에서 삭제함. 객체를 활용할 수 있음
    
    return HttpResponseRedirect( reverse('vote:index') )

#답변 등록 
#매개변수가 필요없음
@login_required
def choiceRegiste(request): #Template 추가, URL 등록, Form 수정
#GET/POST 분리
    if request.method == "GET":
        #GET-> 비어있는 ChoiceForm 객체 생성 -> HTML 전달
        a = ChoiceForm()
        return render(request, 'vote/cr.html', {'a' : a })
    elif request.method == "POST":
        #POST-> 사용자 입력데이터를 기반으로 ChoiceForm 객체 생성 
        #    -> 유효한 값인지 확인 -> 객체 변환 및 데이터베이스에 저장 -> index 또는 detail URL을 반환
        a = ChoiceForm(request.POST)
        if a.is_valid():
            b = a.save()
            #return HttpResponseRedirect( reverse('vote:index')) #index
            return HttpResponseRedirect( reverse('vote:detail' , args=(b.question.id ,) ))
        else:
            return render(request, 'vote/cr.html', {'a' : b })
#답변 삭제
#1)매개 변수를 추가(어떤 답변항목을 삭제할 것인가?)
@login_required
def choiceDelete(request, c_id):
#2)매개 변수로 Choice 객체 찾기
    c = get_object_or_404(Choice, id = c_id)
#3)해당 객체를 삭제
    c.delete()
#4)index 또는 detail의 URL을 반환
    #return HttpResponseRedirect( reverse('vote:index')) #index
    return HttpResponseRedirect( reverse('vote:detail', args=(c.question.id ,)))  #detail


#답변 수정 (내일)
#매개변수 추가(어떤 답변항목을 수정할 것인가?)
@login_required
def choiceUpdate(request, c_id):
    #Choice 객체 찾기
    c = get_object_or_404(Choice, id = c_id)
    #GET/ POST 분리
    if request.method == "GET":
        #GET -> Choice 객체를 기반으로 ChoiceForm 생성 -> HTML 전달
        cf = ChoiceForm(instance = c)
        return render(request, 'vote/cr.html', {'a': cf})
    elif request.method == "POST":
        #POST -> 사용자 입력데이터 + Choice 객체를 기반으로 ChoiceForm 생성 -> 유효한 값인지 확인 -> 객체저장->URL반환
        cf = ChoiceForm(request.POST, instance= c)
        if cf.is_valid():
            cf.save()
            return HttpResponseRedirect( reverse( 'vote:detail', args=(c.question.id,) ) )
        else:
            return render(request, 'vote/cr.html', {'a' : cf, 'error' : '유효한 값이 아닙니다.'})


















