from django.db import models
from django.urls import reverse


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", null=False)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
    