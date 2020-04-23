import json
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import JsonResponse, HttpResponse
from api.models import Company, Vacancy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        company=Company.objects.create(name=data['name'],description=data['description'],city=data['city'],address=data['address'])
        return JsonResponse(company.to_json())
@csrf_exempt
def company_detail(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'message does not exits'})
    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data.get('name',company.name)
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})
@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json,safe=False)
    elif request.method == 'POST':
        data2=json.loads(request.body)
        vacancy=Vacancy.objects.create(name=data2['name'],salary=data2['salary'],)
        return JsonResponse(vacancy.to_json())
@csrf_exempt
def vacancy_detail(request,vacancy_id):
    try:
        vacancy=Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':'message does not exits'})
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name=data['name']
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})