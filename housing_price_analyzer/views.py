from django.http import HttpResponse


def result(request, query_id):
    return HttpResponse("You're looking at the results of query Id: %s." % query_id)
