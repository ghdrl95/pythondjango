'''
Created on 2018. 10. 27.

@author: user
'''
from django.forms.models import ModelForm

#form : HTML 코드에서 사용할 입력양식(<input>)을 모델클래스에 맞게(또는 커스텀) 자동으로
#만들어주는 기능

#class 클래스명(ModelForm 또는 Form)
#ModelForm : 모델클래스를 기반으로 입력양식을 생성할 때 상속받는 클래스
#Form : 커스텀 입력양식을 생성할 때 상속받는 클래스

#HTML 코드로 변환 시 <p>, <table>, <li> 에 포함된 HTML 문법을 제공함
from .models import Choice, Question #폼 클래스와 연동하기위해 임포트

#Question 모델클래스와 연동된 모델폼클래스 정의
class QuestionForm(ModelForm):
    class Meta: #Meta 클래스 정의를 통해서 모델 클래스에 관한 정보를 입력
        #model : 어떤 모델클래스와 연동되는지 작성
        #fields : 모델클래스의 어떤 변수를 입력양식으로 만들것인지 지정하는 변수(iterable)
        #exclude : 모델클래스의 어떤 변수를 입력양식에서 제외할 것인지 지정하는 변수(iterable)
        #fields, exclude 변수 중 한개만 사용해야함
        
        model = Question #해당 모델폼이 Question 모델클래스와 연결하도록 설정
        fields = ['name']#Question 모델클래스에서 name변수만 입력양식으로 제공
        #exclude = ['date'] #Question 모델클래스에서 date변수를 제외하고 입력양식을 제공

#Choice 모델클래스와 연동된 모델폼클래스 정의 
class ChoiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        #ModelForm 클래스의 생성자를 호출해 모델폼의 기능을 할 수 있도록 초기화
        super().__init__(*args,**kwargs)
        #question 라벨 이름을 한글로 수정
        self.fields['question'].label = "질문지"
        
    class Meta:
        #Choice 모델클래스와 연동
        #name, question 변수를 입력양식으로 제공할 수 있도록 설정
        model = Choice
        fields = ['question','name']
        #exclude = ['votes']












