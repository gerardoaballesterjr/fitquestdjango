from rest_framework import generics, permissions, views, pagination
from core import models, utils
from core.api.quest.serializers import QuestSerializer
from rest_framework import response, status, parsers
from collections import OrderedDict
from core import utils

class IndexPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class IndexView(generics.ListAPIView):
    # queryset = models.Quest.objects.all()
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = QuestSerializer
    pagination_class = IndexPagination

    def get_queryset(self):
        season = models.Season.objects.last()
        return models.Quest.objects.filter(season=season)

class DetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,] 
    queryset = models.Quest.objects.all()
    serializer_class = QuestSerializer
    lookup_field = 'slug'


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serialize_data = serializer.data
        
        reward = models.Reward.objects.filter(quest=instance, user=self.request.user).first()
        serialize_data['reward_claimed'] = True if reward and reward.claimed else False
        
        locations = models.Location.objects.filter(user=self.request.user, quest=instance)
        serialize_data['total_distance'] = utils.distance(locations)

        return response.Response(serialize_data)

    