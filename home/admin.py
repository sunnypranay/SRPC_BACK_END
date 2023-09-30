from django.contrib import admin

# Register your models here.

from .models import Students, Scores_Round_1, Scores_Round_2, \
Total_Scores_Round_2_Graduate, Total_Scores_Round_2_Undergraduate, \
Total_Scores_Round_1_Graduate, Total_Scores_Round_1_Undergraduate

from signup.models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_superuser')
    list_display_links = ('email',)
    list_filter = ('email',)
    search_fields = ('email',)
    list_per_page = 25

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'poster_ID', 'judged_count_round_1', 'judged_count_round_2', 'finalist')
    list_display_links = ('Name', 'poster_ID')
    list_filter = ('Name', 'poster_ID')
    search_fields = ('Name', 'poster_ID')
    list_per_page = 25

# class Scores_Round_1(models.Model):
#     judge = models.ForeignKey(User, on_delete=models.CASCADE)
#     student = models.ForeignKey(Students, on_delete=models.CASCADE)
#     research_score = models.IntegerField(null=True, blank=True)
#     communication_score = models.IntegerField(null=True, blank=True)
#     presentation_score = models.IntegerField(null=True, blank=True)

@admin.register(Scores_Round_1)
class Scores_Round_1Admin(admin.ModelAdmin):
    list_display = ('judge', 'Student', 'research_score', 'communication_score', 'presentation_score')
    list_display_links = ('judge', 'Student')
    list_filter = ('judge', 'Student')
    search_fields = ('judge', 'Student')
    list_per_page = 25

@admin.register(Scores_Round_2)
class Scores_Round_2Admin(admin.ModelAdmin):
    list_display = ('judge', 'Student', 'research_score', 'communication_score', 'presentation_score')
    list_display_links = ('judge', 'Student')
    list_filter = ('judge', 'Student')
    search_fields = ('judge', 'Student')
    list_per_page = 25


# class Total_Scores_Round_1_Graduate(models.Model):
#     poster_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     Name = models.CharField(max_length=100)
#     email = models.EmailField()
#     avg_research_score = models.FloatField(default=0)
#     avg_communication_score = models.FloatField(default=0)
#     avg_presentation_score = models.FloatField(default=0)
#     total_score = models.FloatField(default=0)

@admin.register(Total_Scores_Round_1_Graduate)
class Total_Scores_Round_1_GraduateAdmin(admin.ModelAdmin):
    list_display = ('poster_id', 'Name', 'email','total_score', 'avg_research_score', 'avg_communication_score', 'avg_presentation_score')
    list_display_links = ('poster_id', 'Name')
    list_filter = ('poster_id', 'Name')
    search_fields = ('poster_id', 'Name')
    list_per_page = 25

@admin.register(Total_Scores_Round_1_Undergraduate)
class Total_Scores_Round_1_UndergraduateAdmin(admin.ModelAdmin):
    list_display = ('poster_id', 'Name', 'email','total_score', 'avg_research_score', 'avg_communication_score', 'avg_presentation_score')
    list_display_links = ('poster_id', 'Name')
    list_filter = ('poster_id', 'Name')
    search_fields = ('poster_id', 'Name')
    list_per_page = 25

@admin.register(Total_Scores_Round_2_Graduate)
class Total_Scores_Round_2_GraduateAdmin(admin.ModelAdmin):
    list_display = ('poster_id', 'Name', 'email','total_score', 'avg_research_score', 'avg_communication_score', 'avg_presentation_score')
    list_display_links = ('poster_id', 'Name')
    list_filter = ('poster_id', 'Name')
    search_fields = ('poster_id', 'Name')
    list_per_page = 25

@admin.register(Total_Scores_Round_2_Undergraduate)
class Total_Scores_Round_2_UndergraduateAdmin(admin.ModelAdmin):
    list_display = ('poster_id', 'Name', 'email','total_score', 'avg_research_score', 'avg_communication_score', 'avg_presentation_score')
    list_display_links = ('poster_id', 'Name')
    list_filter = ('poster_id', 'Name')
    search_fields = ('poster_id', 'Name')
    list_per_page = 25

