from django.urls import path
from .views import *


urlpatterns = [
    path("", get_routes),
    path("get_user/", get_user),
    path("get_summaries/", get_summaries),
    path("fetch_summaries/<str:user>", fetch_summaries),
    path("get_vacancies/", get_vacancies),
    path("get_city_name/<str:city>/", get_city),
]
