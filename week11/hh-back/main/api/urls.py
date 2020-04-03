from django.conf.urls import url , include
from . import views

urlpatterns = [
    url('companies/', views.companies_lst),
    url('companies/<int:company_id>/', views.getOneCompany),
    url('companies/<int:company_id>/vacancies/', views.vacanciesByCompany),
    url('vacancies/', views.vacancies_lst),
    url('vacancies/<int:vacancy_id>/', views.getOneVacancy),
    url('vacancies/top_ten/', views.decSortedVacancies)
]