from member.models import Member
from rest_framework import serializers

class MemberSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=50)
    age=serializers.IntegerField()
    addres=serializers.CharField()

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.addres=validated_data.get('addres',instance.addres)
        instance.save()
        return instance