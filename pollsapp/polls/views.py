from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Track, Question, Choice
from .api import TrackSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET', 'POST'])
def tracks_list(request):
    """
    List all tracks, or create a new track.
    """
    if request.method == 'GET':
        tier = Track.objects.all()
        serializer = TrackSerializer(tier, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = TrackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def track_info(request, pk):
    """
    Get, udpate, or delete a specific track
    """
    try:
        track = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrackSerializer(track)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
