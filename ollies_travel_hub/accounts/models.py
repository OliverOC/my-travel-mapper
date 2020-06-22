from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.urls import reverse

#
# class User(User, PermissionsMixin):
#
#     def __str__(self):
#         return self.username
#
#     # def get_absolute_url(self):
#     #     return reverse('scratch_map:home', kwargs={'pk': self.pk})
#


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='accounts/profile_pics', blank=True)

    def __str__(self):
        return self.user.username
