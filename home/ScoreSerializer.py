from rest_framework import serializers
from .models import Students, Scores_Round_1, Scores_Round_2, Total_Scores_Round_1_Undergraduate, Total_Scores_Round_1_Graduate, Total_Scores_Round_2_Undergraduate, Total_Scores_Round_2_Graduate
from signup.models import User

class Students_Serializer(serializers.ModelSerializer):
    # the student field is a foreign key, so we need to specify the fields we want to include

    class Meta:
        model = Students
        fields = ('Name', 'poster_ID')


class Scores_Round_Serializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='Student.Name')
    poster_id = serializers.ReadOnlyField(source='Student.poster_ID')
    #  I want judge name
    judge = serializers.ReadOnlyField(source='judge.first_name')
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = Scores_Round_1
        fields = ['id', 'judge', 'Student', 'student_name', 'poster_id', 'research_score', 'communication_score', 'presentation_score', 'total_score']

    def get_total_score(self, obj):
        return obj.research_score + obj.communication_score + obj.presentation_score
