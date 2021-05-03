from rest_framework import serializers


class createChallengeSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField()
    repetition = serializers.IntegerField(required=True, allow_null=False)
    start_date = serializers.DateTimeField(required=True, allow_null=False)
    end_date = serializers.DateTimeField(required=True, allow_null=False)
    progress_type = serializers.CharField(required=True, allow_null=False)
    icon = serializers.FileField()
    private_public_type = serializers.CharField(required=True, allow_null=False)
    category_id = serializers.IntegerField()
    # owner_id = serializers.IntegerField(required=True, allow_null=False)
