from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        """
        Creates and saves a User with the given username, password.
        """
        if not kwargs:
            raise ValueError('Users must have an username address')

        # 开始创建账号
        user = self.model(**kwargs)
        # 设置密码
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 创建管理员
    def create_superuser(self, **kwargs):
        """
        Creates and saves a superuser with the given username, date of
        birth and password.
        """
        user = self.create_user(**kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


# 在这里设置你需要的字段
class UserProfile(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=128,
        unique=True, )
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        null=True,
        blank=True,
        unique=False, )
    headPortrait = models.ImageField(verbose_name="头像",null=True,upload_to="Photos/headPortrait")
    phone = models.CharField(max_length=128, null=True, blank=True)
    qq = models.CharField(max_length=128, null=True, blank=True)
    wechat = models.CharField(max_length=128, null=True, blank=True)
    sex = models.CharField(max_length=45, null=True, blank=True)
    personalSignature = models.CharField(max_length=500, null=True,blank=True)
    is_active = models.BooleanField(verbose_name='是否可用', default=True)
    is_admin = models.BooleanField(verbose_name='是否管理员', default=False)
    create_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    objects = UserProfileManager()

    # 使用username作为必须的字段
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_user_name(self):
        # The user is identified by their username address
        return self.username


    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_admin:
            return True
        else:
            return False

    def has_module_perms(self, perm):
        return True



    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'home_user_profile'
        verbose_name = 'user'
        verbose_name_plural = "user"