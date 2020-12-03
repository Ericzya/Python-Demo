import json

from django.http import HttpResponse
from django.template import loader

from .models import HousePrice, QueryStatistic, JsonEncoder


def house_price_data(request, query_id):
    house_price_info = json.dumps(HousePrice.objects.filter(query_id=query_id), default=JsonEncoder.to_json)
    return HttpResponse(house_price_info)


def index(request):
    query_statistic_list = QueryStatistic.objects.all()
    template = loader.get_template('housing_price_analyzer/index.html')
    context = {
        'query_statistic_list': query_statistic_list,
    }
    return HttpResponse(template.render(context, request))
