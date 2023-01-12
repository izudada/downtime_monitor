from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status

from .models import WebLog, Website
from .serializers import LogSerializer, WebsiteSerializer


class WebsiteAPIView(ListCreateAPIView):
    """
        This class defines the create and list
        behavior of product api.
    """
    serializer_class = WebsiteSerializer
    pagination_class = PageNumberPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'url')

    def post(self, serializer):
        data = {}
        web_serializer = self.serializer_class(data=self.request.data['data'], many=True)
        if web_serializer.is_valid():
            web_serializer.save(user=self.request.user)
            data['websites'] = web_serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(web_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user).all()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_logs(request, id):
    """
        API view to get logs of a website
    """
    try:
        website = Website.objects.filter(user=request.user, id=id)[0].get_logs()
        serializer = LogSerializer(website, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"message": "No logs for this website yet"}, status.HTTP_404_NOT_FOUND)
