from django.urls import path
from .views import *

urlpatterns = [
    path('comment/<int:pk>/', CommentListCreateView.as_view()),
    path('download/<int:pk>/', DownloadView.as_view(), name='download'),
    path('rate/', RateView.as_view(), name='rate')
]
