# from django.shortcuts import render
# # from .models import JobAdvert


# from rest_framework.response import Response
# from rest_framework import status

# # Create your views here.

# @swagger_auto_schema(method="post", request_body=JobAdvert_Serializer())
# @action(methods=["post"], detail=True)
# def post(self, request, format=None):
#         """Allow logged in users to create new job adverts."""

#         serializer = JobAdvert_Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"success"}, status = status.HTTP_200_OK)
        
#         return Response({"message":"failed", "error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)























# # def home(request):
# #     posts = JobAdvert.objects.all()
# #     return render(request,"myapp/index.html", {"posts" : posts})
