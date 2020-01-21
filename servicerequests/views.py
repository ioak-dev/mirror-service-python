from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
import servicerequests.service as service

@api_view(['GET', 'PUT'])
def sr_main(request, tenant):
    if request.method == 'GET':
        response = service.get_sr_main(request, tenant)
        return JsonResponse(response[1], status=response[0])
    if request.method == 'PUT':
        response = service.update_sr_main(request, tenant)
        return JsonResponse(response[1], status=response[0])

@api_view(['GET', 'PUT'])
def sr_log(request, tenant):
    if request.method == 'GET':
        response = service.get_sr_log(request, tenant)
        return JsonResponse(response[1], status=response[0])
    if request.method == 'PUT':
        response = service.update_sr_log(request, tenant)
        return JsonResponse(response[1], status=response[0])
