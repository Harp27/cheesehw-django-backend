from .models import Cheese
from rest_framework import serializers


class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    ## Meta class is for configuring the CheeseSerializer class.
    class Meta:
        # model to serialize
        model = Cheese
        # fields to show in json
        fields = ('id','name', 'origin_country', 'type')