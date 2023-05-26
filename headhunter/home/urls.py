from django.urls import path
from .views import *


urlpatterns = [
    path("", render_home, name="home"),
    path("sign_up/", render_sign_up, name="sign_up"),
    path("profile/", render_profile, name="profile"),
    path("profile/personal/", render_profile_personal, name="profile_personal"),
    path("profile/summary/", render_profile_summary, name="profile_summary"),
    path("profile/summary/new/", new_profile_summary, name="new_profile_summary"),
    path("summary/@<int:summary_id>/", render_summary, name="summary"),
    path("vacancy/@<int:vacancy_id>/", render_vacancy, name="vacancy"),
    path("vacancy/@<int:vacancy_id>/appeal/", apply_vacancy, name="apply_vacancy"),
    path("vacancy/@<int:vacancy_id>/cancel/", cancel_vacancy, name="cancel_vacancy"),
]
