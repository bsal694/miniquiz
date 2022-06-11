from django.shortcuts import render
from miniquiz.models import *

from accounts.models import *
from django.db.models import Sum
from miniquiz.form  import * 

# Create your views here.
def admin(request):
    print(Account.objects.all().values())
    context={
        'totalCategory':Category.objects.filter(category__isnull=False).count(),
        'totalReport':Category.objects.filter(report__gte=20).count(),
        'totalAccount':Account.objects.all().count(),
        'Account':Account.objects.all().values().order_by('-date_joined')[0:4],
        'checkbox':Category.objects.filter(is_verified=False),
        'reportedCategory':Category.objects.filter(report__gte=20,is_verified=True),
    }
    print(Category.objects.filter(is_verified=False))


    return render(request,'admins/admin.html',context)



def leaders(request):
    userlist=leaderboards.objects.select_related('authorsID').values('authorsID__username','authorsID__email','authorsID__profile_image').annotate(Sum('score'))[0:10]

    context={
        'userlist':userlist,
    }
    print(leaderboards.objects.select_related('authorsID').values('authorsID__username','authorsID__profile_image','authorsID__email').annotate(Sum('score')))
    return render(request,'admins/leaders.html',context)


def users(request):
    context={
        'Account':Account.objects.all().values().order_by('-date_joined'),
    }
    
    return render(request,'admins/users.html',context)

def question(request):
    image=ImageForm()
    if request.user.is_admin:
        user=request.user
        if request.method=='POST':
            form = ImageForm(request.POST)
            print(request.POST)
            author_id=Account.objects.filter(username=user).values('id')
            categoryImage="/categoryImage/"+request.POST['categoryImage']
            print(categoryImage)
            print(author_id)
            if form.is_valid():
                dweet = form.save(commit=False)
                dweet.authors_id = author_id
                dweet.categoryImage=categoryImage
                dweet.save()
            


    # if request.POST:

    #     categoruUID=request.POST['id']
    #     questions=request.POST['question']
    #     opt1=request.POST['choice1']
    #     opt2=request.POST['choice2']
    #     opt3=request.POST['choice3']
    #     opt4=request.POST['choice4']
        
    #     quest=Questions(question=questions,category_id=categoruUID)
    #     quest.save()
    #     questionid=Questions.objects.filter(question=questions).values('questionid')

    #     print(request.POST)
    #     if 'answer1' in request.POST:
    #         Answer1=Answer(answer=opt1,question_id=questionid,is_correct=True)
    #         Answer2=Answer(answer=opt2,question_id=questionid)
    #         Answer3=Answer(answer=opt3,question_id=questionid)
    #         Answer4=Answer(answer=opt4,question_id=questionid)
    #     elif 'answer2' in request.POST:
    #         Answer1=Answer(answer=opt1,question_id=questionid)
    #         Answer2=Answer(answer=opt2,question_id=questionid,is_correct=True)
    #         Answer3=Answer(answer=opt3,question_id=questionid)
    #         Answer4=Answer(answer=opt4,question_id=questionid)
    #     elif 'answer3' in request.POST:
    #         Answer1=Answer(answer=opt1,question_id=questionid)
    #         Answer2=Answer(answer=opt2,question_id=questionid)
    #         Answer3=Answer(answer=opt3,question_id=questionid,is_correct=True)
    #         Answer4=Answer(answer=opt4,question_id=questionid)
    #     else:
    #         Answer1=Answer(answer=opt1,question_id=questionid)
    #         Answer2=Answer(answer=opt2,question_id=questionid)
    #         Answer3=Answer(answer=opt3,question_id=questionid)
    #         Answer4=Answer(answer=opt4,question_id=questionid,is_correct=True)
                
                
    #     Answer1.save()
    #     Answer2.save()
    #     Answer3.save()
    #     Answer4.save()
    context={
        'categories':Category.objects.filter(authors=request.user),
        'questionDetail':Questions.objects.select_related('question','category').values('category__categoryName','question','question_answer'),
        'form':image
        
    }



    #  [{'category__categoryName': 'bisal', 'question': 'what is your name ?', 'question_answer': 166}, {'category__categoryName': 'bisal', 'question': 'what is your name ?', 'question_answer': 167}, {'category__categoryName': 'bisal', 'question': 'what is your name ?', 'question_answer': 168}, {'category__categoryName': 'bisal', 'question': 'what is your name ?', 'question_answer': 169}]>


    a=Questions.objects.select_related('question','category').values('category__categoryName','question','question_answer').distinct()
    print(a.values())
    print(a.values('category__categoryName','question'))





    
    return render(request,'admins/categories.html',context)

