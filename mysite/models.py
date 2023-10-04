from django.db import models

# Create your models here.
class Post(models.Model):
    #屬性
    title=models.CharField(max_length=200) #models.CharField 指定資料型態
    slug=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True) #(自動取得時間)
    
    class Mate:
        ordering=('-pub_date', ) #欄位ordering
    
    #複寫
    def __str__(self) -> str:
        return self.title