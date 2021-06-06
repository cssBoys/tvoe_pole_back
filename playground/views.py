from datetime import timedelta
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated


from utils.pagination import CustomPageNumberPagination
from .models import Category, Playground, Review
from . import serializers

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes

import playground


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny, )



def get_month(id):
    month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    return month[id - 1]

def get_dayofweek(id):
    days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
    return days[id]

class PlaygroundViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.PlaygroundListSerializer
    serializer_action_classes = {
        'list': serializers.PlaygroundListSerializer,
        'retrieve': serializers.PlaygroundDetailsSerializer
    }
    queryset = Playground.objects.all()
    permission_classes = (AllowAny, )
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    @action(detail=True, permission_classes=[IsAuthenticated, ], methods=['get', ])
    def days(self, request, pk):
        import datetime
        dates = [datetime.datetime.today() + datetime.timedelta(days=day) for day in range(14)]
        playground = Playground.objects.get(id=pk)
        wokring_days = list(playground.working_days.all().values_list('id', flat=True))
        for index in range(len(dates)):
            weekday = dates[index].weekday() + 1
            if weekday not in wokring_days:
                dates.remove(index)

        data = []

        for date in dates:
            data.append(
                {
                    'day': date.day,
                    'month': date.month,
                    'month_content': get_month(date.month),
                    'day_content': get_dayofweek(date.weekday())
                }
            )
            
        return Response(data)

    @action(detail=True, permission_classes=[IsAuthenticated, ], methods=['post', ])
    def watch(self, request, pk):
        import datetime
        from booking.models import Booking
        data = request.data
        date = datetime.datetime(day=data['day'], month=data['month'], year=2021)
        playground = Playground.objects.get(pk = pk)
        data = []
        for hour in range(playground.time_start.hour, playground.time_finish.hour, 2):
            date_start = date +  datetime.timedelta(hours=playground.time_start.hour + hour)
            date_finish = date + datetime.timedelta(hours=playground.time_start.hour + hour + 2)
            data.append({
                'hour': hour,
                'date_start': date_start.strftime("%Y-%m-%d %H:%M:%S"),
                'date_finish': date_finish.strftime("%Y-%m-%d %H:%M:%S"),
                'active': True
            })
        booking_qs = Booking.objects.filter(pk=pk)
        for el in data:
            datex = date + datetime.timedelta(hours=el['hour'])
            if booking_qs.filter(date_start__gte = datex, date_finish__lte = datex).exists():
                el['active'] = False
        return Response(data)



class ReviewCreateViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = serializers.ReviewCreateSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
