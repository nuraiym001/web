from django.conf.urls import url , include
from . import views

#urlpatterns = [
#    url('companies/', views.companies_lst),
#    url('companies/<int:company_id>/', views.getOneCompany),
#    url('companies/<int:company_id>/vacancies/', views.vacanciesByCompany),
#    url('vacancies/', views.vacancies_lst),
#    url('vacancies/<int:vacancy_id>/', views.getOneVacancy),
#    url('vacancies/top_ten/', views.decSortedVacancies)
#]

from django.urls import path
from api.views import views_fbv, views_cbv
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', views_fbv.companies_list),
    path('companies/<int:company_id>/', views_fbv.company_details),
    path('companies/<int:company_id>/vacancies/', views_fbv.vacancies_list_by_company),
    path('vacancies/', views_cbv.VacanciesListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', views_cbv.VacancyDetailsAPIView.as_view()),
    path('vacancies/top_ten/', views_cbv.TopTenVacanciesAPIView.as_view())
]