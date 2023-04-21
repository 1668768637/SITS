from django.db import models
from user.models import UserProfile
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
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
    create_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)


    class Meta:
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
    create_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

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
    create_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'postLike'
        verbose_name_plural = 'postLike'


@receiver(pre_delete, sender=Post)
def delete_image(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    for img in instance.postImages.all():
        img.photo.delete(False)



class userCollection(models.Model):
    userOwner = models.ForeignKey(UserProfile,
                            related_name="userowner",
                            verbose_name='用户',
                            null=False,
                            on_delete=models.CASCADE)
    postOwner = models.ForeignKey(Post,
                            related_name="postowner",
                            verbose_name='帖子',
                            null=False,
                            on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'userCollection'
        verbose_name_plural = "userCollection"



class Message(models.Model):
    poster = models.ForeignKey(UserProfile,
                               on_delete=models.CASCADE,
                               related_name="poster",
                               null=False)
    receiver = models.ForeignKey(UserProfile,
                                 on_delete=models.CASCADE,
                                 related_name="receiver",
                                 null=False)
    context = models.TextField(verbose_name="消息内容")
    post = models.ForeignKey(Post,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name="postId")
    hasReaded = models.BooleanField(verbose_name="是否查看",
                                    null=False,
                                    default=False)
    create_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    
    def read(self):
        self.hasReaded = True
        self.save()