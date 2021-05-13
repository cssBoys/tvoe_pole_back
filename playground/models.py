from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class PlaygroundType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Playground(models.Model):
    # LOGICAL FIELDS
    title = models.CharField(max_length=255)
    time_start = models.TimeField()
    time_finish = models.TimeField()
    categories = models.ManyToManyField(to='Category', related_name="playgrounds")
    working_days = models.ManyToManyField(to='utils.DayOfWeek')
    city = models.ForeignKey(to='utils.City', on_delete=models.CASCADE)
    price = models.FloatField()

    # ADDITIONAL FIELDS
    phone = models.CharField(max_length=255)
    playground_type = models.ForeignKey(
        to='PlaygroundType',
        on_delete=models.SET_NULL,
        null=True
    )
    address = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    @property
    def cover(self):
        if self.images.first():
            return self.images.first().image.url
        return None

    @property
    def rating(self):
        return self.reviews.all().aggregate(Avg('rating')).get('rating__avg', 0) or 0
        

class PlaygroundImage(models.Model):
    playground = models.ForeignKey(to="Playground", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()


class Review(models.Model):
    playground = models.ForeignKey(Playground, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    text = models.TextField()
    rating = models.IntegerField(default=0)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)