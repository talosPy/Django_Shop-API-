from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from carts.models import Cart, CartItem  # Ensure these models exist
from carts.serializers import CartSerializer, CartItemSerializer  # Ensure these serializers exist


@api_view(['GET', 'POST'])
def cart_list(request):
    """
    List all carts, or create a new cart.
    """
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, id):
    """
    Retrieve, update or delete a cart.
    """
    cart = get_object_or_404(Cart, id=id)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def user_cart_view(request, user_id):
    """
    Retrieve, create, or delete a user's cart.
    """
    cart, created = Cart.objects.get_or_create(user_id=user_id)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def cart_item_list(request, cart_id):
    """
    List all items in a cart, or add a new item.
    """
    cart = get_object_or_404(Cart, id=cart_id)

    if request.method == 'GET':
        items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cart_item_detail(request, cart_id, item_id):
    """
    Retrieve, update, or delete a specific item in a cart.
    """
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)

    if request.method == 'GET':
        serializer = CartItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_to_cart(request, cart_id):
    """
    Add an item to a cart.
    """
    cart = get_object_or_404(Cart, id=cart_id)
    serializer = CartItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(cart=cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_carts_view(request):
    """
    List all carts.
    """
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)
