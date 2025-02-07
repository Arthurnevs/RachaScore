from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.core.docs.user_swagger_docs import register_user_docs
from apps.core.enums.request_method_enum import RequestMethodEnum
from apps.core.logger import logger
from apps.core.serializers.user_serializers import UserRegisterSerializer, UserBasicFieldsSerializer
from apps.core.services.user_service import register_user
from rest_framework import status
from django.db import transaction
import traceback


@api_view([RequestMethodEnum.POST])
@transaction.atomic
def view_make_login(request):
    try:
        response_data = register_user(request.data)
        return Response(data=response_data, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        logger.info(f"Erro de validação: {e.messages}")
        return Response(data={"errors": e.messages}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.warning(f"Erro inesperado: {str(e)}\n{traceback.format_exc()}")
        return Response(data={"error": "Erro interno do servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
