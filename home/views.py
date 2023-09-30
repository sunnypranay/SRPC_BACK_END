from time import sleep
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students, Scores_Round_1, Scores_Round_2, \
Total_Scores_Round_2_Graduate, Total_Scores_Round_2_Undergraduate, \
Total_Scores_Round_1_Graduate, Total_Scores_Round_1_Undergraduate
from rest_framework import status
from django.http import HttpResponseRedirect
from django.urls import reverse
from .ScoreSerializer import Scores_Round_Serializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class home(APIView):
    def get(self, request):
        # I need to send the user Name 
        # I need to the send the scores of round 1 and round 2 posted by the user
        # get all finalist poster id from students table 

        user = request.user

        score_round_1 = Scores_Round_1.objects.filter(judge = user.id)

        score_round_2 = Scores_Round_2.objects.filter(judge = user.id)

        status_of_round_1_table = False
        status_of_round_2_table = False

        if score_round_1.count() > 0:
            status_of_round_1_table = True
        
        if score_round_2.count() > 0:
            status_of_round_2_table = True
        
        finalist_poster_id = Students.objects.filter(finalist = True).values_list('poster_ID', flat=True)

        # write a serializer for the scores of round 1 and round 2 
        # send the scores of round 1 and round 2 to the frontend

        serialized_score_round_1 = Scores_Round_Serializer(score_round_1, many=True)

        serialized_score_round_2 = Scores_Round_Serializer(score_round_2, many=True)

        data = {
            "status_of_round_1_table": status_of_round_1_table,
            "status_of_round_2_table": status_of_round_2_table,
            "finalist_poster_id": finalist_poster_id,
            "score_round_1": serialized_score_round_1.data,
            "score_round_2": serialized_score_round_2.data,
            "Judge": user.first_name + " " + user.last_name,
        }


        return Response(data, status=status.HTTP_200_OK)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class validate_token(APIView):
    def post(self, request):
        # sleep(10)
        return Response(status=status.HTTP_200_OK)
    
class populate_round_1_table(APIView):
    def get(self, request):

         # scores for undergraduate students whose poster id is in range 100 to 199
         scores = Scores_Round_1.get_average_scores()
         
         undergraduate_scores = scores.filter(Student__poster_ID__range=(100, 199))

         poster_id = undergraduate_scores.values_list('Student__poster_ID', flat=True)

         # delete the scores of undergraduate students from the total scores table

         Total_Scores_Round_1_Undergraduate.objects.exclude(poster_id__in=poster_id).delete()

         for score in undergraduate_scores:
             total_score, created = Total_Scores_Round_1_Undergraduate.objects.get_or_create(poster_id=Students.objects.get(poster_ID=score['Student__poster_ID']))
             total_score.Name = score['Student__Name']
             total_score.email = score['Student__email']
             total_score.avg_research_score = score['avg_research_score']
             total_score.avg_communication_score = score['avg_communication_score']
             total_score.avg_presentation_score = score['avg_presentation_score']
             total_score.total_score = score['total_score']
             total_score.save()
        
         # filter the scores for graduate students
         graduate_scores = scores.filter(Student__poster_ID__range=(200, 299))
         
         poster_ids = graduate_scores.values_list('Student__poster_ID', flat=True)

         Total_Scores_Round_1_Graduate.objects.exclude(poster_id__in=poster_ids).delete()

         for score in graduate_scores:
             total_score, created = Total_Scores_Round_1_Graduate.objects.get_or_create(poster_id=Students.objects.get(poster_ID=score['Student__poster_ID']))
             total_score.Name = score['Student__Name']
             total_score.email = score['Student__email']
             total_score.avg_research_score = score['avg_research_score']
             total_score.avg_communication_score = score['avg_communication_score']
             total_score.avg_presentation_score = score['avg_presentation_score']
             total_score.total_score = score['total_score']
             total_score.save()
         
         return HttpResponseRedirect(reverse('admin:index'))

class populate_round_2_table(APIView):
    def get(self, request):
        # scores for undergraduate students whose poster id is in range 100 to 199
        scores = Scores_Round_2.get_average_scores()
        
        undergraduate_scores = scores.filter(Student__poster_ID__range=(100, 199))

        poster_id = undergraduate_scores.values_list('Student__poster_ID', flat=True)

        # delete the scores of undergraduate students from the total scores table

        Total_Scores_Round_2_Undergraduate.objects.exclude(poster_id__in=poster_id).delete()

        for score in undergraduate_scores:
            total_score, created = Total_Scores_Round_2_Undergraduate.objects.get_or_create(poster_id=Students.objects.get(poster_ID=score['Student__poster_ID']))
            total_score.Name = score['Student__Name']
            total_score.email = score['Student__email']
            total_score.avg_research_score = score['avg_research_score']
            total_score.avg_communication_score = score['avg_communication_score']
            total_score.avg_presentation_score = score['avg_presentation_score']
            total_score.total_score = score['total_score']
            total_score.save()
       
        # filter the scores for graduate students
        graduate_scores = scores.filter(Student__poster_ID__range=(200, 299))
        
        poster_ids = graduate_scores.values_list('Student__poster_ID', flat=True)

        Total_Scores_Round_2_Graduate.objects.exclude(poster_id__in=poster_ids).delete()

        for score in graduate_scores:
            total_score, created = Total_Scores_Round_2_Graduate.objects.get_or_create(poster_id=Students.objects.get(poster_ID=score['Student__poster_ID']))
            total_score.Name = score['Student__Name']
            total_score.email = score['Student__email']
            total_score.avg_research_score = score['avg_research_score']
            total_score.avg_communication_score = score['avg_communication_score']
            total_score.avg_presentation_score = score['avg_presentation_score']
            total_score.total_score = score['total_score']
            total_score.save()
        
        return HttpResponseRedirect(reverse('admin:index'))