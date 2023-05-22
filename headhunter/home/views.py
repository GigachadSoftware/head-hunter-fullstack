from allauth.socialaccount.models import SocialAccount
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

from home.forms import SignUpForm
from home.models import Summary, User, Vacancy


def render_home(request: WSGIRequest) -> HttpResponse:
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.city is None:
                return redirect(render_sign_up)
        return render(request, "pages/home.html", {})

    vacancies = Vacancy.objects.all()
    if request.POST.get("city"):
        vacancies = vacancies.filter(city=request.POST["city"])
    if request.POST.get("job_type"):
        vacancies = vacancies.filter(type=request.POST["job_type"])
    result = vacancies
    if request.POST.get("description"):
        result = []
        for vacancy in vacancies:
            if request.POST.get("description").lower() in vacancy.looking_for.lower():
                result.append(vacancy)
    return render(
        request, "pages/home.html", {"search_results": result, "form": request.POST}
    )


def render_sign_up(request: WSGIRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "pages/sign_up.html", {})

    form = SignUpForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            "pages/sign_up.html",
            {
                "form": {
                    "phone_number": form.phone_number,
                    "city": form.city,
                    "birthday": form.birthday,
                },
                "error": "Invalid form!",
            },
        )
    request.user.phone_number = form.cleaned_data["phone_number"]
    request.user.city = form.cleaned_data["city"]
    request.user.birthday = form.cleaned_data["birthday"]
    request.user.save()
    return redirect(render_home)


def render_vacancy(request: WSGIRequest, vacancy_id: int) -> HttpResponse:
    vacancy = Vacancy.objects.filter(id=vacancy_id).first()
    if not vacancy:
        return redirect(render_home)
    return render(request, "pages/vacancy.html", {"vacancy": vacancy})


def apply_vacancy(request: WSGIRequest, vacancy_id: int):
    if not request.user.is_authenticated:
        return redirect(render_home)

    vacancy = Vacancy.objects.filter(id=vacancy_id).first()
    if not vacancy:
        return redirect(render_home)
    vacancy.candidates.add(request.user)
    return redirect(f"/vacancy/@{vacancy_id}/")


def cancel_vacancy(request: WSGIRequest, vacancy_id: int):
    if not request.user.is_authenticated:
        return redirect(render_home)

    vacancy = Vacancy.objects.filter(id=vacancy_id).first()
    if not vacancy:
        return redirect(render_home)
    vacancy.candidates.remove(request.user)
    return redirect(f"/vacancy/@{vacancy_id}/")


def render_profile(request: WSGIRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(render_home)

    return render(request, "pages/profile.html")


def render_profile_personal(request: WSGIRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(render_home)

    social_account = SocialAccount.objects.filter(user=request.user).first()
    return render(
        request,
        "pages/profile/personal.html",
        {
            "email_verified": social_account.extra_data.get("email_verified"),
            "picture": social_account.extra_data.get("picture"),
        },
    )


def render_profile_summary(request: WSGIRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(render_home)
    summaries = Summary.objects.filter(user_id=request.user.id).all()
    return render(request, "pages/profile/summary.html", {"summaries": summaries})
