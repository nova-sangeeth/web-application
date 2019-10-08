from django.db import models


# this is the where all the attributes are placed  and defined accordingly
# pay attention to the spellings makes huge errors


class Items(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url_path = models.CharField(max_length=2083)


# the max standard lenght for the url is 2083 characters which is available on the url
class products_discounts(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Products_shoes(models.Model):
    shoe_type = models.CharField(max_length=255)
    shoe_color = models.CharField(max_length=100)
    shoe_brand = models.CharField(max_length=80)
