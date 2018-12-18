'''
Created on 2018. 10. 28.

@author: user
'''
from django.forms import ModelForm
#User 모델클래스 임포트(django/contrib/auth 폴더에 있는 models.py에 User 클래스 임포트)
from django.contrib.auth.models import User 
from django.forms.widgets import PasswordInput
from django import forms
#회원가입에 사용할 모델 폼 클래스
class SignupForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password_check'].label = "비밀번호 확인"
    #패스워드 확인 <input>태그 변수 선언
    #폼 클래스에 추가적인 <input>을 선언하려면 forms.XXXField 객체를 변수에 저장
    password_check = forms.CharField(max_length=200,widget=PasswordInput())
    #<input> 의 순서를 지정하는 변수
    field_order = ['username','password','password_check','email','last_name',
                   'first_name']
    class Meta:
        model = User
        #input 태그에 특정한 type을 지정할때 사용
        #필드이름을 키값으로 사용하고 저장할 값은 XXXInput 클래스의 객체를 지정 
        widgets={
            'password': PasswordInput() #password 필드에 비밀번호 type을 지정
            }
        #ID,패스워드, 성, 이름, 이메일
        fields=['username', 'password', 'last_name', 'first_name','email']

#로그인에 사용할 모델 폼 클래스 
class SigninForm(ModelForm):
    class Meta:
        model = User
        fields= ['username', 'password']








