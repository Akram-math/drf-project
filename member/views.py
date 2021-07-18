from django.http import JsonResponse
# from django.shortcuts import render
from rest_framework.views import APIView
from django.core.checks import messages
from rest_framework.parsers import JSONParser

from member.serializers import MemberSerializer
from member.models import Member


# Create your views here.
class MemberView(APIView):

    def post(self,request):
        data_request=JSONParser().parse(request)

        member=MemberSerializer(data=data_request)

        if member.is_valid(raise_exception=True):
            member.save()

            return JsonResponse(member.data, status=200)
        return JsonResponse(status=400, messages="Failed", safe=False)
    # def get(self,request,id=None):

        # data= {
        #     "name": "Akram",
        #     "gender": "male"
        # }

    def get(self, request):
        member=Member.objects.all()
        data_member = MemberSerializer(member, many=True)
        return JsonResponse(data_member.data, status=200,safe=False) 