import base64

from django.shortcuts import render

from .models import User

from .serializers import NickNameSerializer

from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.decorators import action

# from djoser.views import UserCreateView

from djoser.conf import settings
from djoser import signals
from djoser.compat import get_user_email


class CreateModelMixin(object):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        language = request.data['language']

        if not language:
            language = "KR"

        if not serializer.is_valid():
            print(serializer.errors)

            error_keys = serializer.errors.keys()

            error_message = []

            # print(len(error_keys))

            # Todo: already exists 오류 못잡음
            for x in error_keys:
                # Todo: language별 작업 필요
                if language == 'KR':
                    message = "{} 항목 오류" .format(x)
                    error_message.append(message)
                elif language == 'EN':
                    pass


            return Response({
                'status': 412,
                'message': error_message,
            })
        # else:
            # print(serializer)
            # print(serializer.data)
            # print(serializer.data['password'])
            # print(base64.b64encode('dlstjdwpfh'.encode()))
            #
            # serializer.data['password'] = base64.b64encode('dlstjdwpfh'.encode())
            # print(serializer.data['password'])
            # serializer.data['password'] = base64.b64decode((serializer.data['password'])).decode('utf-8')
            # print(serializer.data['password'])


        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # Todo: language별 작업 필요
        if language == 'KR':
            success_message = '유저 생성 완료'
        elif language == 'EN':
            pass
        
        return Response({
            'status': 201,
            'message': '유저 생성 완료',
        }, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class CreateAPIView(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserCreateView(CreateAPIView):
    """
    Use this endpoint to register new user.
    """
    serializer_class = settings.SERIALIZERS.user_create
    # from .serializers import UserSerializer
    # serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )

        context = {'user': user}
        to = [get_user_email(user)]
        if settings.SEND_ACTIVATION_EMAIL:
            settings.EMAIL.activation(self.request, context).send(to)
        elif settings.SEND_CONFIRMATION_EMAIL:
            settings.EMAIL.confirmation(self.request, context).send(to)


class UserCreate(UserCreateView):
    pass

user_create = UserCreate.as_view()


class NickNameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = NickNameSerializer

    @action(detail=False)
    def nick_name_check(self, request):
        q = request.GET.get('q', '')

        if q:
            nick_name_usage =User.objects.filter(nick_name=q)

            serializer = self.get_serializer(nick_name_usage)

            return Response(serializer.data)
        else:
            return Response({
                'status': 406,
                'error': '쿼리셋이 존재하지 않습니다. 쿼리셋을 포함해주세요.'
            }, status=406)