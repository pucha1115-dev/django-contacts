from email.errors import CloseBoundaryNotFoundDefect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app.models import Contacts
from app.serializers import ContactSerializer


# Create your views here.

@csrf_exempt
def ContactApi(request, id=0):
    if request.method=='GET':
        if id != 0:
            contact = Contacts.objects.get(ContactId=id)
            contact_serializer = ContactSerializer(contact, many=False)
            return JsonResponse(contact_serializer.data, safe=False)
        else:
            contacts = Contacts.objects.all()
            contacts_serializer = ContactSerializer(contacts, many=True)
            return JsonResponse(contacts_serializer.data, safe=False)

    elif request.method=='POST':
        contact_data = JSONParser().parse(request)
        contacts_serializer = ContactSerializer(data=contact_data)
        if contacts_serializer.is_valid():
            contacts_serializer.save()
            return JsonResponse(contacts_serializer.data, safe=False)
        return JsonResponse('Failed to Add', safe=False)

    elif request.method=='PUT':
        contact_data = JSONParser().parse(request)
        contact = Contacts.objects.get(ContactId=id)
        contact_serializer = ContactSerializer(contact, data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data, safe=False)
        return JsonResponse("Update Failed", safe=False)

    elif request.method=='DELETE':
        contact = Contacts.objects.get(ContactId=id)
        contact_serializer = ContactSerializer(contact, many=False)
        contact.delete()
        return JsonResponse("Deleted Successfully", safe=False)