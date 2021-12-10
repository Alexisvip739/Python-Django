from django.urls import  path

from .views import CompanyListView,CompanyDetailsView
urlpatterns=[
    path('company/',CompanyListView.as_view(),name='company_list'),
    path('company/<int:pk>/',CompanyDetailsView.as_view(), name='company')

]

