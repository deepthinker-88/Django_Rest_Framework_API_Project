from api.models import Players
from rest_framework import serializers




def check_previous_club(value):
    if value == "Chelsea":
        raise serializers.ValidationError("Previous club can't be current club Chelsea")



class PlayerSerializer(serializers.ModelSerializer):
    previous_club = serializers.CharField(validators=[check_previous_club])
   

    class Meta:
        model = Players
        fields = ["id", "first_name", "last_name", "age", "position", "previous_club"]
        
    def validate(self,data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
    
        if first_name == last_name:
            raise serializers.ValidationError("First name and last name cannot be the same!!!")
        
        return data

    

    def validate(self,data):
        age = data.get('age')
        if age < 18:
            raise serializers.ValidationError("Age can't be lower than 18")
        return data
        

def create(self, validated_data):
    validated_data.get("first_name", self.first_name)
    validated_data.get("last_name", self.last_name)
    validated_data.get("position", self.position)
    validated_data.get("age", self.age)
    validated_data.get("previous_club", self.age)
    return Players.objects.create(
        first_name=validated_data.first_name,
        last_name=validated_data.last_name,
        position=validated_data.position,
        age=validated_data.age,
        previous_club=validated_data.previous_club,
    )


def update(self, instance, validated_data):
    instance.first_name = validated_data.get("first_name", instance.first_name)
    instance.last_name = validated_data.get("last_name", instance.last_name)
    instance.position = validated_data.get("position", instance.position)
    instance.age = validated_data.get("age", instance.age)
    instance.previous_club = validated_data.get("previous_club", instance.previous_club)
    instance.save()
    return instance
