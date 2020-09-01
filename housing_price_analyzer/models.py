from django.db import models


class HousePrice(models.Model):
    id = models.IntegerField(primary_key=True)
    house_city = models.CharField(max_length=255)
    house_area = models.CharField(max_length=255)
    house_community = models.CharField(max_length=255)
    house_price = models.BigIntegerField()
    house_square = models.BigIntegerField()
    update_date = models.DateTimeField('date published')
