from django.db import models


class QueryStatistic(models.Model):
    id = models.IntegerField(primary_key=True)
    update_date = models.DateField("date published")
    # 未更新-0 正在更新-1 更新失败-2 更新成功-3
    query_result = models.IntegerField()

    def __str__(self):
        return 'id:%s,update_date:%s,query_result:%s' % (self.id, self.update_date, self.query_result)


class HousePrice(models.Model):
    id = models.IntegerField(primary_key=True)
    query_id = models.ForeignKey(QueryStatistic, on_delete=models.CASCADE, related_name='query_data')
    house_city = models.CharField(max_length=255)
    house_area = models.CharField(max_length=255)
    house_community = models.CharField(max_length=255)
    house_price = models.BigIntegerField()
    house_square = models.BigIntegerField()

    def __str__(self):
        return 'id:%s,query_id:%s,house_city:%s,house_area:%s,house_community:%s,house_price:%s,house_square:%s' % (
            self.id, self.query_id, self.house_city, self.house_area, self.house_community, self.house_price,
            self.house_square)