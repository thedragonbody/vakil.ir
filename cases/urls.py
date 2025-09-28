from django.urls import path
from .views import ClientCaseListView, LawyerCaseListView

urlpatterns = [
    path('client/', ClientCaseListView.as_view(), name='client-cases'),
    path('lawyer/', LawyerCaseListView.as_view(), name='lawyer-cases'),
]