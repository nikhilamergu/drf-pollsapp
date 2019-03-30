from django.urls import path
from pollsapp import routers

from . import views
from . import api

router = routers.SharedAPIRootRouter()
router.register(r'questions', api.QuesViewSet)
router.register(r'choices', api.ChoiceViewSet)
router.register(r'tracks', api.TrackViewSet)
router.register(r'userchoice', api.UserChoiceViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('track/list/', views.tracks_list, name="tracks_list"),
    path('update-track/<int:pk>/', views.track_info, name="track_info"),
]
