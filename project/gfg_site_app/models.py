from django.db import models
import uuid   # universally unique identifiers
import random
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models


# Creation of BaseModel
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    class Meta:
        abstract = True
   
   
# Creation of Topics class using BaseModel     
class Topic(BaseModel):
    gfg_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.gfg_name
    
    

# Creatig new model StudyModel - to store the quizzes
class StudyModel(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField(max_length = 500)
    link = models.TextField(max_length=500, blank=True, default='') # --> Links to the quiz

    # tags works with JSONField to store a list
    tags = models.JSONField(default=list)

    # This allows arranging the regular and advanced quiz for each topic to appear sisde by side.
    pair_id = models.PositiveSmallIntegerField(default=0)   # same number = same topic
    
    # is_advanced is a boolean field. When True, the relevant link connects to an advanced quiz.
    is_advanced = models.BooleanField(default=False)

    # This ensures the actual title of the model appears on Django admin
    def __str__(self):
        return self.title
    
    topic = models.OneToOneField(Topic, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name="study")




# Creation of Question Model from BaseModel
class Question(BaseModel):
    gfg = models.ForeignKey(Topic, related_name='gfg',on_delete= models.CASCADE)
    question = models.TextField(max_length=400)  # Textfield allows line breaks
    question_image = models.ImageField(upload_to='question_images/', blank=True, null=True)
    # tags works with JSONField to store a list of linked skills
    tags = models.JSONField(default = list) 
    explanation = models.TextField(blank=True, null=True)
    explanation_image = models.ImageField(upload_to='explanation_images/', blank=True, null=True)

    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs =  list(Answer.objects.filter(question= self))
        data = []
        random.shuffle(answer_objs)
        
        for  answer_obj in answer_objs:
            data.append({
                'answer' :answer_obj.answer, 
                'is_correct' : answer_obj.is_correct
            })
        return data
    
# Creation of answer model from base model
class Answer(BaseModel):
    question = models.ForeignKey(Question,related_name='question_answer',  on_delete =models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.answer
    
# Code to make quiz attempts be recorded automatically
class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attempts")
    gfg = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="attempts")
    score = models.IntegerField()
    total = models.IntegerField()
    seconds_taken = models.FloatField(default=0)      
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
    @property
    def percent(self):
        return round(100 * self.score / self.total, 1) if self.total else 0
    def __str__(self):
        return f"{self.user} - {self.gfg} ({self.score}/{self.total})"


class AnswerRecord(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, related_name="records")
    is_correct = models.BooleanField()
    seconds_taken = models.FloatField(default=0)


# Code to allow users to choose a font
class Profile(models.Model):
    FONT_CHOICES = [
        ("system", "Standard"),
        ("lexend", "Lexend (easy to read)"),
        ("opendyslexic", "OpenDyslexic"),
        ("comic", "Comic Sans"),
        ("serif", "Serif"),
        ("nunito", "Nunito"),
        ("roboto", "Roboto"),
        ("opensans", "Open Sans"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    font = models.CharField(max_length=20, choices=FONT_CHOICES, default="system")