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

    title = models.CharField(
        verbose_name="标题",
        max_length=45,
        null=False)
    context = models.CharField(
        verbose_name="内容",
        null=False,
        max_length=500
    )
    owner = models.ForeignKey(
        UserProfile,
        verbose_name="所有者",
        related_name="ownerNum",
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
        verbose_name='发布日期'
    )
    likesNum = models.IntegerField(
        verbose_name="点赞数",
        null=False,
        default=0
    )


    class Meta:
        db_table = "Posts"
        verbose_name = 'post'
        verbose_name_plural = "post"


class PostImage(models.Model):
    owner = models.ForeignKey(Post,
                                related_name='postImages',
                                verbose_name='帖子图片',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Photos/PostsPhoto',
                              blank=True,
                              verbose_name='帖子图片')

    class Meta:
        verbose_name = 'postIMG'
        verbose_name_plural = 'postIMG'


class Commit(models.Model):
    userOwner = models.ForeignKey(UserProfile,
                                  related_name='userOwner',
                                  verbose_name='帖子所有者',
                                  null=False,
                                  on_delete=models.CASCADE)
    postOwner = models.ForeignKey(Post,
                                related_name='postConmmits',
                                verbose_name='主帖子',
                                null=True,
                                on_delete=models.CASCADE)
    commitOwner = models.ForeignKey('self',
                                related_name='commitConmmits',
                                verbose_name='主评论',
                                null=True,
                                on_delete=models.CASCADE)
    context = models.CharField(
                                verbose_name="内容",
                                max_length=500,
                                default="",
                                null=False)

    class Meta:
        verbose_name = 'Commit'
        verbose_name_plural = 'Commit'


class PostLike(models.Model):
    user = models.ForeignKey(
        UserProfile,
        related_name="user",
        verbose_name="点赞者",
        null=False,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="post",
        verbose_name="帖子",
        null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'postLike'
        verbose_name_plural = 'postLike'