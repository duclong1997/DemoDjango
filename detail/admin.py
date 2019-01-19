from django.contrib import admin
from .models import post

# Register your models here.
# manage models in admin 
class PostAdmin(admin.ModelAdmin):
    # show colum in table post
    list_display = ('id','title','numberPost','datetime','body')
    #  show by filter with numberPost
    list_filter =['numberPost']
    #  search by title or id 
    search_fields =["title",'id']
    
admin.site.register(post, PostAdmin)
