from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'htmlEditor.html')


#自定义编辑器
def rich_content(request):
    html = request.POST['hcontent']
    text = RichText()
    text.content = html
    text.save()
    for i in locals():
        print(i)
    return render(request,'htmlShow.html',locals())