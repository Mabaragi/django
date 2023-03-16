from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    
    # 데이터가 만들어질 때 현재 시간이 자동으로 설정됨
    created_at = models.DateTimeField(auto_now_add=True)

    # 데이터가 저장될 때 마다
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at.month}/{self.created_at.date}에 생성된 {self.id}번글 - {self.title} : {self.content}'
    
    """
    출력 
    print(articles)
    <QuerySet [<Article: 3/<built-in method date of datetime.datetime object at 0x000002963C4D7030>에 생성된 1번글 - first : django!>]>
    """
    