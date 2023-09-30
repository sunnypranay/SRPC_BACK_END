from time import sleep
from home.models import Students, Scores_Round_1, Scores_Round_2, \
Total_Scores_Round_1_Undergraduate, Total_Scores_Round_1_Graduate, \
Total_Scores_Round_2_Undergraduate, Total_Scores_Round_2_Graduate
from signup.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from django.urls import reverse


def check_poster_round_1(poster, judge):
    # check if the poster is valid or not
    # 1 -> vaild poster id and can be scored
    # 2 -> invalid poster id
    # 3 -> poster already scored by the judge

    # check if the poster is valid or not if the poster is not a number then return 2

    if not poster.isdigit():
        return 2

    poster_status = Students.objects.filter(poster_ID=poster).exists()

    if poster_status:
        status = Scores_Round_1.objects.filter(judge=judge, Student = Students.objects.filter(poster_ID=poster).first()).exists()
        if status:
            return 3
        else:
            return 1
    else:
        return 2

def check_poster_round_2(poster, judge):
    # check if the poster is valid or not
    # 1 -> vaild poster id and can be scored
    # 2 -> invalid poster id
    # 3 -> poster already scored by the judge
    # 4 -> poster is not a finalist

    if not poster.isdigit():
        return 2

    poster_status = Students.objects.filter(poster_ID=poster).exists()

    if poster_status:
        finalist = Students.objects.filter(poster_ID=poster).first().finalist
        if finalist:
            status = Scores_Round_2.objects.filter(judge=judge, Student = Students.objects.filter(poster_ID=poster).first()).exists()
            if status:
                return 3
            else:
                return 1
        else:
            return 4
    else:
        return 2
    

def check_poster_round_1_edit(poster, judge):
    # 1 -> valid poster id and can be edited
    # 2 -> invalid poster id
    # 3 -> poster is not scored by the judge

    if not poster.isdigit():
        return 2
    
    poster_status = Students.objects.filter(poster_ID=poster).exists()

    if poster_status:
        status = Scores_Round_1.objects.filter(judge=judge, Student = Students.objects.filter(poster_ID=poster).first()).exists()
        if status:
            return 1
        else:
            return 3
    else:
        return 2
    

def check_poster_round_2_edit(poster, judge):
    # 1 -> valid poster id and can be edited
    # 2 -> invalid poster id
    # 3 -> poster is not scored by the judge
    # 4 -> poster is not a finalist

    if not poster.isdigit():
        return 2
    
    poster_status = Students.objects.filter(poster_ID=poster).exists()

    if poster_status:
        finalist = Students.objects.filter(poster_ID=poster).first().finalist
        if finalist:
            status = Scores_Round_2.objects.filter(judge=judge, Student = Students.objects.filter(poster_ID=poster).first()).exists()
            if status:
                return 1
            else:
                return 3
        else:
            return 4
    else:
        return 2

# create a interface so that poster id can be validated before actually scoring 
# and redirecting the scoring page
# poster id will be in the url

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class round1_pre_check(APIView):
    def get(self, request, poster_id):
        # sleep(3)
        user = request.user
        poster_status = check_poster_round_1(poster_id, user)
        if poster_status == 1:
            return Response({"status": "Poster is valid and can be scored"}, status=status.HTTP_200_OK)
        elif poster_status == 2:
            return Response({"status": "Poster ID is invalid"}, status=status.HTTP_401_UNAUTHORIZED)
        elif poster_status == 3:
            return Response({"status": "Poster is already scored by the Judge"}, status=status.HTTP_401_UNAUTHORIZED)
        


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class round2_pre_check(APIView):
    def get(self, request, poster_id):
        user = request.user
        poster_status = check_poster_round_2(poster_id, user)
        if poster_status == 1:
            return Response({"status": "Poster is valid and can be scored"}, status=status.HTTP_200_OK)
        elif poster_status == 2:
            return Response({"status": "Poster ID is invalid"}, status=status.HTTP_401_UNAUTHORIZED)
        elif poster_status == 3:
            return Response({"status": "This poster is already scored by the Judge"}, status=status.HTTP_401_UNAUTHORIZED)
        elif poster_status == 4:
            return Response({"status": "This poster is not a Round 2 finalist"}, status=status.HTTP_401_UNAUTHORIZED)
        


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class round1_pre_check_without_ID(APIView):
    def get(self, request):
        return Response({"status": "Please enter the poster ID"}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class round2_pre_check_without_ID(APIView):
    def get(self, request):
        return Response({"status": "Please enter the poster ID"}, status=status.HTTP_401_UNAUTHORIZED)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class round1_pre_check_edit(APIView):
    def get(self, request, poster_id):
        user = request.user
        poster_status = check_poster_round_1_edit(poster_id, user)
        if poster_status == 1:
            return Response({"status": "Poster is valid and can be edited"}, status=status.HTTP_200_OK)
        elif poster_status == 2:
            return Response({"status": "Poster ID is invalid"}, status=status.HTTP_401_UNAUTHORIZED)
        elif poster_status == 3:
            return Response({"status": "Poster is not scored by the Judge"}, status=status.HTTP_401_UNAUTHORIZED)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class round2_pre_check_edit(APIView):
    def get(self, request, poster_id):
        user = request.user
        poster_status = check_poster_round_2_edit(poster_id, user)
        if poster_status == 1:
            return Response({"status": "Poster is valid and can be edited"}, status=status.HTTP_200_OK)
        elif poster_status == 2:
            return Response({"status": "Poster ID is invalid"}, status=status.HTTP_401_UNAUTHORIZED)
        elif poster_status == 3:
            return Response({"status": "Poster is not scored by the Judge"}, status=status.HTTP_401_UNAUTHORIZED)
        elif poster_status == 4:
            return Response({"status": "Poster is not a finalist"}, status=status.HTTP_401_UNAUTHORIZED)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class round1_pre_check_edit_without_ID(APIView):
    def get(self, request):
        return Response({"status": "Please enter the poster ID"}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class round2_pre_check_edit_without_ID(APIView):
    def get(self, request):
        return Response({"status": "Please enter the poster ID"}, status=status.HTTP_401_UNAUTHORIZED)
    