from django.urls import path
from data import views
from data.models import StateData

home_list_view = views.HomeListView.as_view(
    queryset=StateData.objects.all(),
    context_object_name="stateData",
    template_name="data/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
