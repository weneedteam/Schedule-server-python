from django.shortcuts import render

from .models import FriendRequest, Friend

from .serializers import FriendRelationSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from django.utils import timezone


class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRelationSerializer

    def create(self, request, *args, **kwargs):
        # print(request.data)
        serializer = self.get_serializer(data=request.data)

        # Todo: Is_valid 에러 코드 작성 필요
        serializer.is_valid(raise_exception=True)

        # self.perform_create(serializer)

        if serializer.is_valid():
            data = serializer.validated_data

            # print(data)
            
            # Todo: try except 구문으로 로직 최적화 시키기
            friend_request = FriendRequest.objects.filter(request_user=data['response_user'], response_user=data['request_user'])
            before_request = FriendRequest.objects.filter(request_user=data['request_user'], response_user=data['response_user'])

            if Friend.objects.filter(request_user=data['request_user'], response_user=data['response_user']):
                return Response({
                    'status': 200,
                    'message': "이미 친구 상태입니다."
                }, status.HTTP_200_OK)

            if before_request:
                return Response({
                    'status': 202,
                    'message': "이미 친구 요청을 보냈습니다."
                }, status.HTTP_202_ACCEPTED)

            # print(friend_request)

            if friend_request:
                friend_request = friend_request[0]

                now = timezone.now()

                friend_request.assent = 1
                friend_request.assented_at = now
                friend_request.save()

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
        else:
            return Response({
                'status': 409,
                'message': "요청 형식에 맞지 않습니다."
            }, status.HTTP_409_CONFLICT)


    @action(detail=False)
    def f_list(self, request):
        user = self.get_object()

        queryset = FriendRequest.objects.filter(request_user=user, response_user=user, assent=1)

        serializer = FriendRelationSerializer(queryset, many=True)

        print(serializer.data)

        return Response({
            'message': 'testing'
        })