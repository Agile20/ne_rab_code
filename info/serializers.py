from rest_framework import serializers

from info.models import(
    SubmitApplication,
)


class SubmitApplicationSerializer(serializers.Serializer):
    class Meta:
        model = SubmitApplication
        fields = (
            'id', 'name', 'email', 'resume',
        )
    