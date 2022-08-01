from django.db import models
from django.utils import timezone

# Create your models here.



    
    
class chief(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام ')
    family=models.CharField(max_length=50,verbose_name='نام خانوادگی ')
    SCORE_RATE=[
        ('senior','senior'),
        ('midlle','midlle'),
        ('junior','junior')
    ]
    score=models.CharField(max_length=50,choices=SCORE_RATE,verbose_name='جایگاه')

    def __str__(self) -> str:
        return f'{self.name}\t{self.family}'
    
    class Meta:
        db_table = 'chief_db'
        managed = True
        verbose_name = 'سر دبیر'
        verbose_name_plural = 'سر دبیران'
    
    
    
class publish(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام نشر')
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    chief=models.OneToOneField(chief,on_delete=models.CASCADE,verbose_name='سر دبیر')
    
    class Meta:
        db_table = 'publish_db'
        managed = True
        verbose_name = 'نشر '
        verbose_name_plural = 'ناشر '
    


class author(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام')
    family=models.CharField(max_length=50,verbose_name=' نام خانوادگی')
    age=models.IntegerField(default=30,verbose_name='سن')
    image_name=models.CharField(max_length=100,null=True,blank=True,verbose_name='تصویر')
    slug=models.SlugField(max_length=50)
    
    
    def __str__(self) -> str:
        return f'{self.name}\t{self.family}\t{self.age}'
    
    class Meta:
        db_table = 'author_db'
        managed = True
        verbose_name = 'نویسنده '
        verbose_name_plural = 'نویسندگان '
    
    
class article(models.Model):
    name_article=models.CharField(max_length=50,verbose_name="نام مقاله")
    text_article=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیر فعال')
    update=models.DateTimeField(default=timezone.now)
    STATUS_FIELD=[
        ('draft','draft'),
        ('publish','publish')
    ]
    status=models.CharField(max_length=50,choices=STATUS_FIELD,verbose_name='وضعیت')
    author=models.ForeignKey(author,on_delete=models.CASCADE,verbose_name='نویسنده')
    publish=models.ManyToManyField(publish,verbose_name='انتشارات')
    
    def __str__(self) -> str:
        return f'{self.name_article}\t{self.text_article}'
    
    class Meta:
        db_table = 'article_db'
        managed = True
        verbose_name = 'مقاله '
        verbose_name_plural = 'مقالات '
    

    

