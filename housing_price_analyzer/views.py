import json

from django.http import HttpResponse

from .models import HousePrice, JsonEncoder


def result(request, query_id):
    query_detail_list = json.dumps(list(HousePrice.objects.filter(query_id=query_id)), default=JsonEncoder.to_json)
    return HttpResponse(query_detail_list)
