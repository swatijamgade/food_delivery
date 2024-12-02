from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem, MenuItem
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):

        try:
           cart_item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExit:
            return Response({'detail : CartItem not found'}, status=status.HTTP_400_BAD_REQUEST)

        cart_item.delete()
        return Response({'detail : CartItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class MenuItemView(APIView):

    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response({ 'message : Menu items retrieved successfully.', 'data:  serializer.data'})

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Menu item created succesfully', 'data : serializer.data'}, status=status.HTTP_201_CREATED)
        return Response({'error : Error'}, status=status.HTTP_400_BAD_REQUEST)

class MenuItemDetailView(APIView):

    def get_object(self, pk):
        try:
            return MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return None

    def get(self, request, pk):
        menu_item = self.get_object(pk)
        if not menu_item:
            return Response({'message: Menu item not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuItemSerializer(menu_item)
        return Response({'message : Menu item retrieved successfully.','data : serializer.data'})

    def put(self, request, pk):
        menu_item = self.get_object(pk)
        if not menu_item:
            return Response({'message : Menu item not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuItemSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Menu item updated successfully','data : serializer.data'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        menu_item = self.get_object(pk)
        if not menu_item:
            return Response({'message : Menu item not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuItemSerializer(menu_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Menu item updated successfully','data : serializer.data'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu_item = self.get_object(pk)
        if not menu_item:
            return Response({'message : Menu item not found.'}, status=status.HTTP_404_NOT_FOUND)

        menu_item.delete()
        return Response({'message : Menu item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


