from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import status
from .responses import ResponseMessages


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/patients',
        'GET /api/patients/:id',
        'POST /api/patients/add'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getAddPatients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseMessages.create_entity("Patient", True), status=status.HTTP_201_CREATED)
        return Response(ResponseMessages.create_entity("Patient", False), status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def modifyPatient(request, pk):
    patient = Patient.objects.get(id=pk)

    if request.method == 'GET':
        serializer = PatientSerializer(patient, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseMessages.modify_entity('Patient', True, 'PUT'))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(ResponseMessages.modify_entity('Patient', True, 'PUT'),status=status.HTTP_204_NO_CONTENT)
