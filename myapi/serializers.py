# serializers.py
from rest_framework import serializers

from .models import Member, Period, Main_class

class Periodserializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('start', 'end')

class MemberSerializer(serializers.ModelSerializer):
    activity_periods = Periodserializer(many=True, source = 'period_def',read_only = True)
    # , read_only=True)

    class Meta:
        model = Member
        fields = ('id', 'real_name' ,'tz', 'activity_periods',)
        #fields = ('id', 'real_name', 'tz', 'activity_periods')
        #model = Period
        #fields = ('start','end')
    def create(self, validated_data):
        periods_data = validated_data.pop('periods')
        member = Member.objects.create(**validated_data)
        for period_data in periods_data: 
            Period.objects.create(member=member, **period_data)
        return member
    
class mainclassserializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True,required = True)
    class Meta:
        model = Main_class
        fields = ('ok', 'members',)

