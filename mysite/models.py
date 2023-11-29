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

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
class Product(models.Model):
    SIZES = (
        ('S', 'Smaill'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    result =models.BooleanField()
   