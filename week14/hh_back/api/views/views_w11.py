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
        return JsonResponse({'data': 'product post request'})
@csrf_exempt
def company_detail(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'message does not exits'})
    if request.method == 'GET':
        return JsonResponse(company.to_json())


def company_vacancies(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'message does not exits'})

    vacancies = company.vacancy_set.all()
    vacancies_json = [p.to_json() for p in vacancies]
    return JsonResponse(vacancies_json,safe=False)

@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json,safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'product post request'})
@csrf_exempt
def vacancy_detail(request,vacancy_id):
    try:
        vacancy=Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':'message does not exits'})
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())

def get_top_vacancies(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[:10]
    top_vacancies_json = [vacancy.to_json() for vacancy in top_vacancies]
    return JsonResponse(top_vacancies_json, safe=False)
