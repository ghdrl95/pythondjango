from django.db import models

#카테고리
class PostType(models.Model):
    name = models.CharField('카테고리', max_length=20)
    def __str__(self):
        return self.name
    
from django.conf import settings
#글(제목,글쓴이, 글내용, 작성일, 카테고리)
class Post(models.Model):
    type = models.ForeignKey(PostType, on_delete = models.PROTECT)
    #models.CASCADE : 연결된 객체가 삭제되면 다같이 삭제됨
    #models.PROTECT : 연결된 객체가 삭제되는것을 막아줌
    #models.SET_NULL : 연결된 객체가 삭제되면 null 값을 가짐
    #models.SET_DEFAULT : 연결된 객체가 삭제되면 기본 객체와 연결됨
    #models.SET(연결할 객체) : 연결된 객체가 삭제되면 매개변수로 지정된 객체로 값이 변경
    headline = models.CharField('제목', max_length=200)
    #TextField : 글자수 제한이 없는 문자열을 저장하는 공간
    #null : 데이터베이스에 저장할 때 해당 변수 값이 비어있어도 생성되도록 허용
    #blank : 폼객체.is_valid(), 폼객체.as_p 을 사용할 때 빈칸을 허용
    content = models.TextField('내용', null=True, blank=True)
    #settings.AUTH_USER_MODEL : 현재 웹서버가 회원을 관리할 때 사용하는 모델클래스를 의미
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #DateTimeField의 매개변수 auto_now_add : 객체가 생성될때 자동으로 서버의 현재시간을 저장할 수 있도록 허용
    pub_date = models.DateTimeField('작성일', auto_now_add=True)
    
    class Meta:
        #ordering : 데이터베이스에 저장된 객체를 정렬하는 방식을 저장
        #변수이름 앞에 '-'를 붙인 경우 내림차순으로 정렬
        ordering = ['-id'];

#이미지
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField('이미지파일', upload_to = 'images/%Y/%m/%d')
    #ImageField: 이미지 경로를 저장하는 저장공간
    #upload_to : 실제 이미지를 저장할때 사용할 경로
    #%Y : 해당 서버의 년도 %m : 해당 서버의 월 %d : 해당 서버의 일
    
    #객체 삭제 시 호출되는 함수. 여기에 실제 이미지를 지우는 과정을 코딩
    def delete(self, using=None, keep_parents=False):
        self.image.delete() #image 변수에 저장된 경로에 파일을 삭제
        return models.Model.delete(self, using=using, keep_parents=keep_parents)
    
#파일
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField('첨부파일', upload_to = 'files/%Y/%m/%d')
    #FileField : 파일(이미지,실행파일,액셀,워드, 등) 의 경로를 저장하는 공간
    
    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)











