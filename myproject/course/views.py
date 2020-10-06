from django.shortcuts import render
from .models import Answer
from .forms import AnswerForm
# Create your views here.
def index(request):
    if request.method=="POST":
        fm=AnswerForm(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm=AnswerForm()
    return render(request,'course/index.html',{'form':fm})