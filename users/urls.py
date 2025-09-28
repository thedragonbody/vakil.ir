from django.urls import path
from .views import LawyerRegisterView, ClientRegisterView, LawyerListView, LawyerSearchView

urlpatterns = [
    path('register/lawyer/', LawyerRegisterView.as_view(), name='register-lawyer'),
    path('register/client/', ClientRegisterView.as_view(), name='register-client'),
    path('', LawyerListView.as_view(), name='lawyer-list'),
    path('search/', LawyerSearchView.as_view(), name='lawyer-search'),

]