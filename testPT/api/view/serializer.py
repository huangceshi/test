from rest_framework import serializers
from api import models

class ModulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modular
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields ='__all__'


class EnvironmentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Environmental
        fields ='__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields ='__all__'

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Config
        fields ='__all__'

class CursorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cursor
        fields ='__all__'

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Api
        fields ='__all__'

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Run
        fields ='__all__'