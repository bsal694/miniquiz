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
        if request.method=='POST':
            print(request.POST)
            print(Category.objects.all().values())
            categoryImage="categoryImage/"+request.POST['categoryImage']
            categoryName=request.POST['categoryName']
            categoryDescription=request.POST['description']
            categoryAuthor=request.POST['authors']
            new_category=Category(categoryImage=categoryImage,categoryName=categoryName,description=categoryDescription,authors_id=categoryAuthor)
            new_category.save()
            print("hi")


    

            # form.save()
        else:
            print("hello")

    form=ImageForm()
    context={
        'n':Category.objects.count(),
        'categories':Category.objects.filter(authors=user).order_by('update_at')[0:5],
        'categoryImage':Category.objects.all(),
        'form':form,
        'quizCategory':Category.objects.exclude(authors=user)[0:4],
        'CategoryOwner':Account.objects.get(username=user),
        'form':form
        
        }
    print(Category.objects.exclude(authors=user).values())

    

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

def detail(request):
    request.GET.get('quizid')
   

    if request.user.is_authenticated:
        currentuser=request.user.username 
        uuid_check=request.GET.get('quizid')
        uid_check_url="/getquestion/get?quizid="+uuid_check
        username=str(request.user).upper()
        
        authorid=Category.objects.filter(uid=uuid_check).values('authors').first()
        a=Account.objects.filter(id=authorid['authors']).values('username').first()
        username=a['username']
        profileImage=Account.objects.filter(username=username).values('profile_image').first()
        profile_image="http://127.0.0.1:8000/media/"+profileImage['profile_image']
        print(username)


        # username=Account.objects.filter(id=authorid).values()
        # print(username)
        if request.method=='POST':
            values=request.POST['value']
            user=request.POST['user']
            followerss=request.POST['follower']
            if values == 'follow':
                followers_count=follower(follower=followerss,user=user)
                followers_count.save()
            if values == 'unfollow':
                a=follower.objects.filter(user=user).values('id').first()
                id=a['id']
                followers_count=follower(follower=followerss,user=user,id=id)
                followers_count.delete()

            




        user_followers=len(follower.objects.filter(user=username))
        user_following=len(follower.objects.filter(follower=username))
        user_follower_list=follower.objects.filter(user=username)
        print(user_follower_list)
        user_follower_list1=[]
        for i in user_follower_list:
            user_follower_list0=i.follower
            user_follower_list1.append(user_follower_list0)
        if currentuser in user_follower_list1:
            follow_button_value="unfollow"
            print("hi")

        else:
            print(currentuser)
            follow_button_value="follow"


        


        





    context={
        'categoryCount':Category.objects.filter(authors=authorid['authors']).count(),
        'name':username,
        'image':profile_image,
        'follower':user_followers,
        'following':user_following,
        'follow_button_value':follow_button_value,
        'next_btn':uid_check_url,
        
        
        
    }
   
   
    return render(request,'miniquiz/userDetail.html',context)

def miniquiz(request):
    uuid_check=request.GET.get('quizid')
    a=Category.objects.all().values()
    print(a)
    context={
        'id': uuid_check,
    }

    return render(request,'miniquiz/miniquiz.html',context)


def admin(request):
    context={
        'UserCount':Account.objects.all().count(),
        'CategoryList':Account.objects.all(),
        'CategoryCount':Category.objects.all().count(),
        'ReportCount':Category.objects.filter(report__gte=20).count(),      
        'QuestionCount':Questions.objects.all().count(),   
    }
    print(Account.objects.all().values())
  
    return render(request,'miniquiz/admin.html',context)

def categorylist(request):
    user=request.user
    context={'categories':Category.objects.filter(authors=user).order_by('update_at')}
    return render(request,'miniquiz/categoryDetail.html',context)
