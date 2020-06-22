from django.contrib.auth import get_user_model
from django.db import models
# from accounts.models import UserProfile
from django.urls import reverse

User = get_user_model()


class Country(models.Model):
    country_name = models.CharField(max_length=100, primary_key=True, unique=True)
    country_code = models.CharField(max_length=50)
    country_type = models.CharField(max_length=100)
    country_coordinates = models.TextField()

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = 'Countries'


class Trip(models.Model):
    country_visited = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='trips', default=None)
    year_visited = models.IntegerField()
    note = models.TextField()
    trip_img = models.ImageField(upload_to='scratch_map/images', blank=True)
    author = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #     return reverse('scratch_map:photo_cards', kwargs={'username': self.user.username, 'pk': self.pk})

    def __str__(self):
        return "{} - {} {}".format(self.author, self.country_visited, self.year_visited)
