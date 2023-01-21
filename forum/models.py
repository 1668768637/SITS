from django.db import models
from home.models import UserProfile
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    POST_TYPE = (
        ('lostAndFound','lostAndFound'),
        ('anecdoteForum','anecdoteForum'),
        ('driftBottle','driftBottle'),
        ('eventInformation','eventInformation'),
        ('loveWall','loveWall')
        )

    id = models.IntegerField(
        unique=True,
        primary_key=True,
        verbose_name="id")
    title = models.CharField(
        verbose_name="标题",
        max_length=45,
        null=False)
    context = models.TextField(
        verbose_name="内容",
    )
    ownerNum = models.ForeignKey(
        UserProfile,
        verbose_name="所有者",
        on_delete=models.CASCADE,
        null=False)
    postType = models.CharField(
        choices=POST_TYPE,
        verbose_name="类型",
        max_length= 50
        )
    publishDate = models.DateField(
        max_length=20,
        default=timezone.now,
        verbose_name='发布时间'
    )


    class Meta:
        db_table = "Posts"
        verbose_name = 'post'
        verbose_name_plural = "post"


class PostImage(models.Model):
    product = models.ForeignKey(Post,
                                related_name='productImgs',
                                verbose_name='帖子',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Photos/PostsPhoto',
                              blank=True,
                              verbose_name='帖子图片')

    class Meta:
        verbose_name = 'postIMG'
        verbose_name_plural = 'postIMG'
