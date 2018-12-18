from django.contrib import admin
from .models import Post,PostFile,PostImage,PostType
# Register your models here.
#models.py 임포트 및 admin.site.register() 로 관리자 사이트에 등록
admin.site.register(Post)
admin.site.register(PostFile)
admin.site.register(PostImage)
admin.site.register(PostType)





    