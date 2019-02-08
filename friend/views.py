from django.contrib.auth import get_user_model

from django.db.models import Q

from .models import FriendRequest, Friend

from .serializers import FriendRequestSerializer, FriendSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


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
                Friend.objects.get(Q(request_user=data['request_user'], response_user=data['response_user']) | Q(request_user=data['response_user'], response_user=data['request_user']))

                return Response({
                    'status': 200,
                    'message': "이미 친구 상태입니다."
                })
            except:
                try:
                    friend_request = FriendRequest.objects.filter(request_user=data['response_user'], response_user=data['request_user'])[0]
                except:
                    friend_request = None

            if friend_request:
                # friend_request = friend_request[0]
                friend_request.delete()
                Friend.objects.create(request_user=data['response_user'], response_user=data['request_user'])

                headers = self.get_success_headers(serializer.data)

                return Response({
                    'status': 200,
                    'message': "친구 요청 수락"
                }, status=status.HTTP_200_OK, headers=headers)
            else:
                try:
                    FriendRequest.objects.get(Q(request_user=data['request_user'], response_user=data['response_user']) | Q(request_user=data['response_user'], response_user=data['request_user']))

                    return Response({
                        'status': 200,
                        'message': "이미 친구 요청을 한 상태입니다."
                    })
                except:
                    serializer.save()
                    headers = self.get_success_headers(serializer.data)

                    return Response({
                        'status': 201,
                        'message': "친구 요청 완료"
                    }, status=status.HTTP_201_CREATED, headers=headers)


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    @action(detail=False)
    def filter(self, request):
        try:
            user = request.GET.get('user')

            try:
                user = User.objects.get(nick_name=user)
            except:
                return Response({
                    'message': '잘못된 요청'
                })

            friends = Friend.objects.filter(Q(request_user=user) | Q(response_user=user))

            serializer = self.get_serializer(friends, many=True)

            return Response(serializer.data)
        except:
            return Response({
                'message': '잘못된 요청'
            })