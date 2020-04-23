from django.urls import path
#from api.views import vacancy_list,vacancy_detail#,company_vacancies,get_top_vacancies
#from api.views.views_fbv import company_vacancies#, company_list, company_detail,  vacancy_list, vacancy_detail
#from api.views.views_cbv import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
#from api.views.views_generic_v1 import CompanyListAPIView, CompanyDetailAPIView, \
    #VacancyListAPIView, VacancyDetailAPIView
from api.views.views_generic import company_vacancies,CompanyListAPIView, CompanyDetailAPIView, \
    VacancyListAPIView, VacancyDetailAPIView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/',CompanyDetailAPIView.as_view()),
    #path('companies/',companies_list),
    #path('companies/<int:company_id>',company_detail),
    path('companies/<int:company_id>/vacancies',company_vacancies),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/',VacancyDetailAPIView.as_view()),
    #path('vacancies/',vacancy_list),
    #path('vacancies/<int:vacancy_id>/',vacancy_detail),
    #path('vacancies/top_ten',get_top_vacancies),
    ]


#urlpatterns = [
#path('companies/', CompanyList.as_view()),
 #   path('companies/<int:pk>/', CompanyDetails.as_view()),
  #  path('companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
   # path('vacancies/', VacancyList.as_view()),
   # path('vacancies/<int:pk>/', VacancyDetails.as_view())
#]