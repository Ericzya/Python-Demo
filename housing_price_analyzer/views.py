import json

from django.http import HttpResponse
from django.template import loader

from .models import HousePrice,QueryStatistic, JsonEncoder


def result(request, query_id):
    query_detail_list = json.dumps(list(HousePrice.objects.filter(query_id=query_id)), default=JsonEncoder.to_json)
    return HttpResponse(query_detail_list)


def index(request, query_id):
    query_statistic_list = QueryStatistic.objects.filter(id=query_id)
    template = loader.get_template('housing_price_analyzer/index.html')
    context = {
        'query_statistic_list': query_statistic_list,
    }
    return HttpResponse(template.render(context, request))
