from django.db import models
from django.contrib.auth import get_user_model
import uuid,random



# from django.contrib.auth import get_user_model
username =get_user_model()

# Create your models here.e
#Base class
class BaseModel(models.Model):
    update_at=models.DateField(auto_now_add=True)
    created_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True

class Category(BaseModel):
    uid=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    categoryName=models.CharField(max_length=100)
    description = models.TextField()
    authors = models.ForeignKey(username,on_delete=models.CASCADE)

    def __str__(self):
        return self.categoryName

class Questions(models.Model):
    questionid = models.AutoField(primary_key=True)
    category=models.ForeignKey(Category,related_name="category",on_delete=models.CASCADE)
    update_at=models.DateField(auto_now_add=True)
    created_at=models.DateField(auto_now=True)
    question=models.CharField(max_length=100)
    def __str__(self)->str:
        return self.question
    def get_answer(self):
        answer_object=list(Answer.objects.filter(question=self))
        data=[]
        
        for answer_objects in answer_object:
            data.append({
                'answer':answer_objects.answer,
                'is_correct':answer_objects.is_correct
            })
        return data

class Answer(BaseModel):
    answer_id = models.AutoField(primary_key=True)
    question=models.ForeignKey(Questions,related_name="question_answer",on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)

    def __str__(self):
        return self.answer
    



    