from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from rest_framework.permissions import IsAuthenticated

class DataValidationView(APIView):
    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Data is valid"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecureDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Secure data accessed"}, status=200)


def process_large_file(file_path, chunk_size=1000):
    with open(file_path, 'r') as file:
        while chunk := file.readlines(chunk_size):
            process_chunk(chunk)

def process_chunk(chunk):
    pass

