from django.urls import path
from .views import (
    DepartmentListView,
    DepartmentDetailView,
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDeleteView,
)

urlpatterns = [
    path("", DepartmentListView.as_view(), name="department-list"),
    path("<int:pk>/", DepartmentDetailView.as_view(), name="department-detail"),
    path("create/", DepartmentCreateView.as_view(), name="department-create"),
    path("<int:pk>/update/", DepartmentUpdateView.as_view(), name="department-update"),
    path("<int:pk>/delete/", DepartmentDeleteView.as_view(), name="department-delete"),
]
