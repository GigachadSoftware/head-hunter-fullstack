from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import User, Vacancy, Summary
from home.tests import get_city_name
from .serializers import UserSerializer, VacancySerializer, SummarySerializer


@api_view(["GET"])
def get_routes(request: WSGIRequest):
    return Response({
        "/": "This page",
        "/get_user/": "Get the current authenticated user",
        "/get_summaries/": "Get all summaries of the authenticated user",
        "/fetch_summaries/<USER_EMAIL>": "Get all summaries of a user",
        "/get_vacancies/": "Get all vacancies",
        "/get_city/<CITY_ID>/": "Get the name (in Ukrainian) of a city using its ID",
    })


@api_view(["GET"])
def get_user(request: WSGIRequest):
    if not request.user.is_authenticated:
        return HttpResponseNotFound({
            "message": "Request is not authenticated. Please, log-in using Google before continuing!"
        })
    return Response(UserSerializer(User.objects.filter(id=request.user.id).first(), many=False).data)


@api_view(["GET"])
def get_summaries(request: WSGIRequest):
    if not request.user.is_authenticated:
        return HttpResponseNotFound({
            "message": "Request is not authenticated. Please, log-in using Google before continuing!"
        })

    return Response(SummarySerializer(Summary.objects.filter(user_id=request.user.id).all(), many=True).data)


@api_view(["GET"])
def fetch_summaries(request: WSGIRequest, user: str):
    return Response(SummarySerializer(Summary.objects.filter(email=user).all(), many=True).data)


@api_view(["GET"])
def get_vacancies(request: WSGIRequest):
    if not request.user.is_authenticated:
        return HttpResponseNotFound({
            "message": "Request is not authenticated. Please, log-in using Google before continuing!"
        })

    return Response(VacancySerializer(Vacancy.objects.all(), many=True).data)


@api_view(["GET"])
def get_city(request: WSGIRequest, city: str):
    return Response({
        "city": city,
        "name": get_city_name(city)
    })
