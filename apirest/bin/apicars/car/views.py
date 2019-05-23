#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from car.models import Car
from car.serializers import CarSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
    
@csrf_exempt
def listAllCars(request):
    if request.method == 'GET':
        carros = Car.objects.all()
        serializer = CarSerializer(carros, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def getCarDataByID(request, pk):
    try:
        carro = Car.objects.get(pk=pk)
        print(carro)
    except Car.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CarSerializer(carro)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        print('PK => ' + str(pk))
        data = JSONParser().parse(request)
        serializer = CarSerializer(carro, data=data)
        if serializer.is_valid():
            print('Todo bien')
            serializer.save()
            print('ya no paso xd')
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        print('Entraaa')
        carro.delete()
        #return HttpResponse(status=204)
