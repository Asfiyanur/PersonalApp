from rest_framework import serializers
from .models import Department,Personal
from django.utils.timezone import now


class DepartmentSerializers(serializers.ModelSerializer):
    
    personal_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = ("id", "name", "personal_count")
        
    def get_personal_count(self, obj):
        return obj.personals.count()
    
    
    
class PersonalSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    create_user_id = serializers.IntegerField(required = False)
    create_user = serializers.StringRelatedField()
    class Meta:
        model = Personal
        fields = '__all__'

    #! burade user id create edilirken id ekleniyordu bunu view de 47.satırda yapabiliriz orasıda create old içindir
    # def create(self, validated_data):
    #     validated_data["create_user_id"] = self.context['request'].user.id
    #     instance = Personal.objects.create(**validated_data)
    #     return instance
    
    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days
    
    
    
class DepartmentPersonalSerializer(serializers.ModelSerializer):
    
    personnel_count = serializers.SerializerMethodField()
    personals = PersonalSerializer(many=True, read_only=True)
    
    class Meta:
        model = Department
        fields = ("id", "name", "personnel_count", "personals")
        
    def get_personnel_count(self, obj):
        return obj.personals.count()