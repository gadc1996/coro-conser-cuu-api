from rest_framework import serializers
from concerts.models import Concert, Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["id", "name", "file"]


class ConcertSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Concert
        fields = ["id", "name", "date", "time", "location", "image", "scores"]
