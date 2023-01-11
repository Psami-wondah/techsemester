from django.urls import path
from .views import Suggestion

urlpatterns = [path("suggestions", Suggestion.as_view())]
