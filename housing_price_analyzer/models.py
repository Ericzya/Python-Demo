from django.db import models


class QueryStatistic(models.Model):
    id = models.IntegerField(primary_key=True)
    update_date = models.DateField("date published")
    # 未更新-0 正在更新-1 更新失败-2 更新成功-3
    query_result = models.IntegerField()

    def __str__(self):
        return str(self.__to_dict())

    def __to_dict(self):
        return {
            'id': self.id,
            'update_date': str(self.update_date),
            'query_result': self.query_result
        }


class HousePrice(models.Model):
    id = models.IntegerField(primary_key=True)
    query_id = models.ForeignKey(QueryStatistic, on_delete=models.CASCADE, related_name='update_data')
    house_city = models.CharField(max_length=255)
    house_area = models.CharField(max_length=255)
    house_community = models.CharField(max_length=255)
    house_price = models.BigIntegerField()
    house_square = models.BigIntegerField()

    def __str__(self):
        return str(self.__to_dict())

    def __to_dict(self):
        return {
            'id': self.id,
            'query_id': str(self.query_id),
            'house_city': self.house_city,
            'house_area': self.house_area,
            'house_community': self.house_community,
            'house_price': self.house_price,
            'house_square': self.house_square
        }


class JsonEncoder(models.Model):
    def to_json(self):
        print(str(self))
        return str(self)
