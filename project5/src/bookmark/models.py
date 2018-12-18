from django.db import models
#모델 : 데이터베이스에 데이터를 저장할 때, 어떤 형식으로 저장할지 관리 및 정의 부분
#Model 상속받으면서 클래스를 정의

#Model 클래스 정의 후, makemigrations 를 통해 migration 파일을 생성
#생성한 파일로 migrate 를 통해 데이터베이스에 저장공간 생성 됨
# 클래스 정의 -> makemigrations -> migrate 순으로 진행됨


#북마크 모델 클래스
#이름 및 URL 저장
class BookMark(models.Model):
    #해당 모델클래스에 저장할 값을 정의할 때, 클래스 내의 변수를 정의
    #models.py에 있는 XXXField 클래스의 객체를 변수에 저장하는 것으로 정의할 수 있음
    #이름 저장
    #CharField : 글자수 제한이 있는 문자열을 저장하는 공간 정의
    bookname = models.CharField(max_length=200)
    #URL 저장
    #URLField : 인터넷 주소(URL)을 저장하는 공간 정의
    bookurl = models.URLField()
    #__str__ : 객체를 출력할 때 표현방식을 처리하는 파이썬 함수
    #print(북마크객체) -> 해당 객체의 bookname 변수에 저장된 문자열 출력
    def __str__(self):
        return self.bookname
    # 모델클래스를 정렬, 보여지는 이름을 변경할 때 Meta 클래스를 정의해 사용할 수 있음
    class Meta:
        ordering = ('bookname',) #정렬방식을 bookname변수의 값을 오름차순으로 정렬
        #내림차순으로 정렬 하고 싶은 경우 변수명 앞에 '-' 붙이기
    
    
    
    
    
    
    
    
    
    