from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("work/", views.portfolio, name="portfolio"),
    path("pricing/", views.pricing, name="pricing"),
    path("process/", views.process, name="process"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    path("contact/", views.contact, name="contact"),
]
