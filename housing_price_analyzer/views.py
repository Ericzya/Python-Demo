import json

from django.http import HttpResponse
from django.template import loader

from .models import HousePrice, QueryStatistic, JsonEncoder


def house_price_data(request, query_id):
    house_price_info = HousePrice.objects.filter(query_id=query_id)[0]
    template = loader.get_template('housing_price_analyzer/query_data_detail.html')
    context = {
        'house_price_info': house_price_info,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    query_statistic_list = QueryStatistic.objects.all()
    template = loader.get_template('housing_price_analyzer/index.html')
    context = {
        'query_statistic_list': query_statistic_list,
    }
    return HttpResponse(template.render(context, request))
