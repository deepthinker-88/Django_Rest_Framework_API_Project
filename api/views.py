from django.shortcuts import render
from .models import Players
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status,generics,mixins
from api.serializers import PlayerSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404






@api_view(["GET"])
def player_list(request):
    if request.method == "GET":
        players = Players.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def individual_player(request, pk):
    try:
        player = Players.objects.get(pk=pk)
    except Players.DoesNotExist:
        return Response(data={'Error':'Chelsea player Id does not exist'},status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        player = Players.objects.get(pk=pk)
        serializer = PlayerSerializer(player)
    
        #return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    
    

@api_view(["POST"])
def player_post(request):
    if request.method == "POST":
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(data={'Player Error':'Unable to add new Player, as player already exists!'}, status=status.HTTP_400_BAD_REQUEST)
            
            #return Response(data={"Message":"Player has been created"}, status=status.HTTP_201_CREATED)
       

@api_view(['PATCH'])
def player_update(request,pk):
    if request.method == 'PATCH':
        player = Players.objects.get(pk=pk)
        serializer = PlayerSerializer(player,partial=True,data=request.data)
        if serializer.is_valid(raise_exception=True):
            #first_name =serializer.validated_data['first_name']
            serializer.save()
            return Response(data={"Message:Player updated succesfully"},status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            #return Response(data=serializer.data,status=status.HTTP_200_OK)
            return Response(data={"Player not updated: Unable to update player"},status=status.HTTP_400_BAD_REQUEST) 


@api_view(["DELETE"])
def delete_player(request, pk):
    if request.method == "DELETE":
        player = Players.objects.get(pk=pk)
        player.delete()
        return Response(data={'Confirmation:Player has been deleted'},status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)



