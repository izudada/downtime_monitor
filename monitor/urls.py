from django.urls import path
from . import views


urlpatterns = [
    path('websites/', views.WebsiteAPIView.as_view(), name="create_website"),
    path('websites/<int:id>/logs/', views.get_logs, name="view_logs")
]