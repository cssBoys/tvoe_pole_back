from django.db import models

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
        return 0


class PlaygroundImage(models.Model):
    playground = models.ForeignKey(to="Playground", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()
