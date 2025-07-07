# posts/views.py
from rest_framework import viewsets
from .models import SocialPost
from .serializers import SocialPostSerializedr


class SocialPostViewSet(viewsets.ModelViewSet):
    '''this class defines the view for listing and creating social posts'''
    queryset = SocialPost.objects.all()
    serializer_class = SocialPostSerializedr
