from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Servers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ServersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servers
        fields = ('id', 'name', 'ip', 'os', 'production', 'created')

