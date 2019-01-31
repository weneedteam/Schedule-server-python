from django.contrib.auth import get_user_model

from .models import FriendRequest, Friend

from .serializers import FriendRequestSerializer, FriendSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response


User = get_user_model()

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Todo: Is_valid 에러코드 작성 필요
        serializer.is_valid(raise_exception=True)

        # self.perform_create(serializer)

        if serializer.is_valid():
            data = serializer.validated_data

            try:
                friend_request = FriendRequest.objects.filter(request_user=data['response_user'], response_user=data['request_user'])[0]
            except:
                friend_request = None

            if friend_request:
                # friend_request = friend_request[0]
                friend_request.delete()
                friend = Friend.objects.create(request_user=data['response_user'], response_user=data['request_user'])

                headers = self.get_success_headers(serializer.data)

                return Response({
                    'status': 200,
                    'message': "친구 요청 수락"
                }, status=status.HTTP_200_OK, headers=headers)
            else:
                serializer.save()
                headers = self.get_success_headers(serializer.data)

                return Response({
                    'status': 201,
                    'message': "친구 요청 완료"
                }, status=status.HTTP_201_CREATED, headers=headers)


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer