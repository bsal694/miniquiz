from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from accounts.views import *
from django.contrib.auth.models import User
from .form import question_form


import json

# Create your views here.
def home(request):
    
    context={'categories':Category.objects.all()}
    return render(request,'miniquiz/home.html',context)

def quiz(request,uuid_check):
    context={'category':Questions.objects.filter(category_id=uuid_check),'id':uuid_check }
    return render(request,'miniquiz/test.html',context)


# def category(request,uuid_check):

#     context={'category':Category.objects.filter(uid=uuid_check)}
#     return render(request,'miniquiz/test.html',context)

    
    

    


def getquiz(request,uuid_check):
    try:
        question_obj=Questions.objects.filter(category_id=uuid_check)        
        data=[]
      

        for question_objs in question_obj:
            categories=str(question_objs.category.categoryName)
            data.append({
                "question":question_objs.question,
                "answer":question_objs.get_answer(),
                'questionid':question_objs.questionid,
            })
            payload={'status':True,'category':categories,'data':data,}
            

        return JsonResponse(payload)

            
        
        
        

    except Exception as e:
        print(e)
        return HttpResponse("something went wrong")



def get_answer(self):
    answer_object=list(Answer.objects.filter(question=self))
    data=[]
        
    for answer_objects in answer_object:
        data.append({
            'answer':answer_objects.answer,
            'is_correct':answer_objects.is_correct
            
        })
    return data


# def home_view(request,*args,**kwargs):
#     myform=question_form(request.POST)
#     print(myform)
#     if request.method == 'DELETE':
#         print(myform.is_valid())
#         myform.delete()
        
      
          
        

    

#     return render(request,'miniquiz/form.html',)

def home_view(request,hi,uuid_check):
    try:

        print(Questions.objects.get(questionid=hi).delete())
        

    except:
        print("a")
    return render(request,'miniquiz/test.html')

def add(request,uuid_check):
    if request.method =='POST':

        post_data=json.loads(request.body.decode("UTF-8"))
        a=post_data.get("title")
        Questions.question=a
        Questions.save()



         
    return render(request,'miniquiz/quiz.html')

    
