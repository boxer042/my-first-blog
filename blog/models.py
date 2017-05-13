from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# 모델(object)을 정의 - 특별한 키워드로 객체를 정의
# models.Model 은 Post가 장고 모델임을 의미 이코드 때문에
# 장고는 Post가 데이터베이스에 저장되야한다고 알게됌

# title, text, create_date, published_date, author
# 속성을 정의하기 위해, 각 필드마다 어떤 종류의 데이터 타입을 가지는지를 정함
# models.CharField : 글자수가 제한된 텍스트를 정의할떄 사용. 글 제목같이 대부분의 짧은 문자열 정보를 저장할 때 사용
# models.TextField : 글자 수가 제한이 없는 긴 텍스트를 위한 속성. 블로그 콘텐츠 담기
# models.DateTimeField : 날짜와 시간의미
# models.ForeignKey : 다른 모델이 대한 링크를 의미