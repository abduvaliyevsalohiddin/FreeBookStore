from django.urls import path
from .views import *

urlpatterns = [
    path('comment/', CommentPostView.as_view(), name='comment_post'),
    path('download/<int:pk>/', DownloadView.as_view(), name='download'),
    path('rate/', RateView.as_view(), name='rate')
]
