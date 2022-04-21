from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from accounts.views import *
from django.contrib.auth.models import User
from .form import ImageForm
import json


def home(request):
    form=ImageForm()
    if request.user.is_authenticated:
        user=request.user
    context={
        'n':Category.objects.count(),
        'categories':Category.objects.filter(authors=user),
        'categoryImage':Category.objects.all(),
        'form':form,
        'quizCategory':Category.objects.exclude(authors=user),
        
        }
    

    return render(request,'miniquiz/home.html',context)

def quiz(request,uuid_check):
    categoryImg=Category.objects.filter(uid=uuid_check).values('categoryImage').first()
    categoryUrl="http://127.0.0.1:8000/media/" + categoryImg['categoryImage']
    context={
    'category':Questions.objects.filter(category_id=uuid_check),
    'id':uuid_check,
    'categoryImage':categoryUrl,
    'categoryName':Category.objects.get(uid=uuid_check)
    }
    return render(request,'miniquiz/test.html',context)


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


def home_view(request,hi,uuid_check):
    try:

        print(Questions.objects.get(questionid=hi).delete())
        

    except:
        print("a")
    return render(request,'miniquiz/test.html')

def add(request,uuid_check):

    if request.method == 'POST':
        post_data=json.loads(request.body.decode("UTF-8"))


        name=post_data['title']
        option1=post_data['opt1']
        option2=post_data['opt2']
        option3=post_data['opt3']
        option4=post_data['opt4']

        quest=Questions(question=name,category_id=uuid_check)
        quest.save()
        questionid=Questions.objects.filter(question=name).values('questionid')
        Answer1=Answer(answer=option1,question_id=questionid)
        Answer2=Answer(answer=option2,question_id=questionid)
        Answer3=Answer(answer=option3,question_id=questionid)
        Answer4=Answer(answer=option4,question_id=questionid)
        Answer1.save()
        Answer2.save()
        Answer3.save()
        Answer4.save()


    return render(request,'miniquiz/quiz.html')


def update(request,uuid_check,questionsid):
        if request.method == 'POST':
            post_data=json.loads(request.body.decode("UTF-8"))


            name=post_data['title']
            option1=post_data['opt1']
            option2=post_data['opt2']
            option3=post_data['opt3']
            option4=post_data['opt4']
            questio=Questions(question=name,category_id=uuid_check,questionid=questionsid)
            questio.save()
            quest=Questions.objects.get(questionid=questionsid,question=name)
            questionids=Answer.objects.filter(question=quest).values('answer_id')
            Answer1=Answer(answer=option1,answer_id=questionids[0]['answer_id'],question_id=questionsid)
            Answer2=Answer(answer=option2,answer_id=questionids[1]['answer_id'],question_id=questionsid)
            Answer3=Answer(answer=option3,answer_id=questionids[2]['answer_id'],question_id=questionsid)
            Answer4=Answer(answer=option4,answer_id=questionids[3]['answer_id'],question_id=questionsid)
            Answer1.save()
            Answer2.save()
            Answer3.save()
            Answer4.save()
        return render(request,'miniquiz/quiz.html')

def detail(request,uuid_check):

    if request.user.is_authenticated:

        # username=str(request.user).upper()
        authorid=Category.objects.filter(uid=uuid_check).values('authors').first()
        print(authorid['authors'])
        a=Account.objects.filter(id=authorid['authors']).values('username').first()
        username=a['username']
        profileImage=Account.objects.filter(username=username).values('profile_image').first()
        profile_image="http://127.0.0.1:8000/media/"+profileImage['profile_image']
        print("http://127.0.0.1:8000/media/"+profileImage['profile_image'])
        # username=Account.objects.filter(id=authorid).values()
        # print(username)




    context={
        'categoryCount':Category.objects.filter(authors=authorid['authors']).count(),
        'name':username,
        'image':profile_image
        
        
    }
   
   
    return render(request,'miniquiz/userDetail.html',context)


    
