from rest_framework import serializers
from baseball_api_app.models import Master, Batting, Pitching, Fielding


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class BattingSerializer(serializers.ModelSerializer):
    player_code = serializers.HyperlinkedRelatedField(
        many = False,
        view_name = "master_detail_update_destroy_api_view",
        read_only = True,
    )
    on_base_percentage = serializers.FloatField()
    class Meta:
        model = Batting
        fields = '__all__'


class PitchingSerializer(serializers.ModelSerializer):
    player_code = serializers.HyperlinkedRelatedField(
        many = False,
        view_name = "master_detail_update_destroy_api_view",
        read_only = True,
    )

    class Meta:
        model = Pitching
        fields = '__all__'


class FieldingSerializer(serializers.ModelSerializer):
    player_code = serializers.HyperlinkedRelatedField(
        many = False,
        view_name = "master_detail_update_destroy_api_view",
        read_only = True,
    )

    class Meta:
        model = Fielding
        fields = '__all__'
