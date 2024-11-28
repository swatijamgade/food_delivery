from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, MenuItemSerializer

class CartListView(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

class CartDetailView(APIView):
    def get(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExit:
            return Response({'detail : Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error : Error'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExit:
            return Response({'detail : Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        cart.delete()
        return Response({'detail : Cart deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class CartItemListView(APIView):

    def get(self, request):

        cart_items = CartItemListView.objects.all()
        serializer = CartItemListView(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail: Cart item created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error : Error'}, status=status.HTTP_400_BAD_REQUEST)

class  CartItemDetailView(APIView):

    def get(self, request, pk):

        try:
            cart_item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExit:
            return Response({'detail : CartItem not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

    def put(self, request, pk):

        try:
            cart_item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExit:
            return Response({'detail : CartItem not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartItemSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)










