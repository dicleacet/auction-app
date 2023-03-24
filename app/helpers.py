from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ImageField
from django.core.files.base import ContentFile
from django.db.models.deletion import ProtectedError
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import uuid
import os
import base64


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 200


class DestroyModelMixin:
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if request.user == instance:
                return Response(
                    {"detail": "Kendinize ait kullanıcıyı silemezsiniz."}, status=status.HTTP_400_BAD_REQUEST
                )
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response(
                {'detail': _('Silinmek istenen objeye bağlı veriler olduğu için silinemez.')},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Http404:
            return Response({"detail": "Bulunamadı."}, status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        instance.delete()


class Base64ImageField(ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # base64 encoded image - decode
            img_format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = img_format.split('/')[-1]  # guess file extension
            img_id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name=img_id.urn[9:] + '.' + ext)
        return super(Base64ImageField, self).to_internal_value(data)


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def proof_images_path(instance, filename):
    name, ext = get_filename_ext(filename)
    new_filename = str(uuid.uuid4())
    final_name = f"{slugify(instance)}-{new_filename}{ext}"
    return f"proof_images/{final_name}"
