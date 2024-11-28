from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer


class AddressListCreateAPIView(APIView):


    def get(self, request):

        addresses = Address.objects.filter(user=request.user)
        serializer = AddressSerializer(addresses, many=True)
        if not addresses:
            return Response({"detail": "No addresses found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Addresses retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
    
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message : Address created successfully.', 'data : serializer.data'}, status=status.HTTP_201_CREATED)
        return Response({'message : Failed to create address.','data : serializer.data'},  status=status.HTTP_400_BAD_REQUEST)

class AddressRetriveUpdateDestroyaAPIView(APIView):

        def get_object(self, pk, user):
            try:
                return Address.objects.get(pk=pk, user=user)
            except Address.DoesNotExit:
                return None

        def get(self, request, pk):

            address = self.get_object(pk, request.user)
            if address is None:
                return Response({'detail : Address not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = AddressSerializer(Address)
            return Response({'message : Address retrived successfully.','data : serializer.data'},status=status.HTTP_200_OK)

        def put(self, request, pk):

            address = self.get_object(pk, request.user)
            if address is None:
                return Response({'detail : Address is not found.','data : serializer.data'},status=status.HTTP_404_NOT_FOUND)

            serializer = AddressSerializer(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message : Address updated successfully.','data : serializer.data'}, status=status.HTTP_200_OK)
            return Response({'message : Failed to update address.','data : serializer.data'}, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk):
             address = self.get_object(pk, request.user)
             if address is None:
                 return Response({'message : Address is not found.','data : serializer.data'}, status=status.HTTP_404_NOT_FOUND)
             return Response({'message : Address deleted successfully.','data : serializer.data'}, status=status.HTTP_204_NO_CONTENT)

