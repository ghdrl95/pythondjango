'''
Created on 2018. 10. 21.

@author: user
'''
from django.shortcuts import render
from django.template import RequestContext

#404 에러페이지 처리 뷰
def handler404(request, *args,**argv):
    return render(request,"404.html",status = 404 )

#500 에러페이지 처리 뷰
def handler500(request, *args,**argv):
    return render(request,"500.html",status = 500 )





