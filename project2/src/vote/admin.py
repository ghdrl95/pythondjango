from django.contrib import admin
from .models import Question, Choice
#Question 모델클래스의 관리자사이트에서 보여지는 설정
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name','date')
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'votes', 'question')
    search_fields = ('name','id')
    exclude = ('votes',)
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)