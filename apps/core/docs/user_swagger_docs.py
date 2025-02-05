from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from apps.core.serializers.user_serializers import UserRegisterSerializer, UserBasicFieldsSerializer, \
    UserRegisterRequestSerializer

register_user_docs = swagger_auto_schema(
    operation_summary="Registrar um novo usuário",
    operation_description="Endpoint para criar um novo usuário na plataforma.",
    method="post",
    request_body=UserRegisterRequestSerializer,
    responses={
        status.HTTP_201_CREATED: UserBasicFieldsSerializer,
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Erros de validação",
            examples={"application/json": {"errors": ["Campo obrigatório: email"]}},
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
            description="Erro interno do servidor",
            examples={"application/json": {"error": "Erro interno do servidor"}},
        ),
    },
)
