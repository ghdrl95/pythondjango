from django.db import models

#질문
#질문제목, 생성일
class Question(models.Model):
    name = models.CharField('설문지 제목',max_length=200)
    date = models.DateTimeField()
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['-date']
        verbose_name = '질문지'
        verbose_name_plural = '질문지'
#답변항목
#답변내용, 투표수, 어떤질문에 연결되있는지?(외래키)
class Choice(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    def __str__(self):
        return self.name + '/' + self.question.name
    class Meta:
        ordering = ['question']
        verbose_name = '답변항목'
        verbose_name_plural = '답변항목'




