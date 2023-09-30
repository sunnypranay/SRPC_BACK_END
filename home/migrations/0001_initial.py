# Generated by Django 4.1.7 on 2023-04-07 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('date', models.DateField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('academic_status', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phonetic_spelling', models.CharField(blank=True, max_length=100, null=True)),
                ('research_adviser_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('research_adviser_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('research_adviser_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('poster_title', models.CharField(blank=True, max_length=100, null=True)),
                ('jacket_size', models.CharField(blank=True, max_length=100, null=True)),
                ('jacket_gender', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('poster_ID', models.IntegerField(blank=True, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('scored_By_Judges', models.IntegerField(blank=True, null=True)),
                ('finalist', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Students',
                'verbose_name_plural': 'Students',
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Total_Scores_Round_2_Undergraduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('avg_research_score', models.FloatField(default=0)),
                ('avg_communication_score', models.FloatField(default=0)),
                ('avg_presentation_score', models.FloatField(default=0)),
                ('total_score', models.FloatField(default=0)),
                ('poster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.students')),
            ],
            options={
                'verbose_name': 'Total Scores Round 2 Undergraduate',
                'verbose_name_plural': 'Total Scores Round 2 Undergraduate',
                'db_table': 'total_scores_round_2_undergraduate',
            },
        ),
        migrations.CreateModel(
            name='Total_Scores_Round_2_Graduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('avg_research_score', models.FloatField(default=0)),
                ('avg_communication_score', models.FloatField(default=0)),
                ('avg_presentation_score', models.FloatField(default=0)),
                ('total_score', models.FloatField(default=0)),
                ('poster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.students')),
            ],
            options={
                'verbose_name': 'Total Scores Round 2 Graduate',
                'verbose_name_plural': 'Total Scores Round 2 Graduate',
                'db_table': 'total_scores_round_2_graduate',
            },
        ),
        migrations.CreateModel(
            name='Total_Scores_Round_1_Undergraduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('avg_research_score', models.FloatField(default=0)),
                ('avg_communication_score', models.FloatField(default=0)),
                ('avg_presentation_score', models.FloatField(default=0)),
                ('total_score', models.FloatField(default=0)),
                ('poster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.students')),
            ],
            options={
                'verbose_name': 'Total Scores Round 1 Undergraduate',
                'verbose_name_plural': 'Total Scores Round 1 Undergraduate',
                'db_table': 'total_scores_round_1_undergraduate',
            },
        ),
        migrations.CreateModel(
            name='Total_Scores_Round_1_Graduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('avg_research_score', models.FloatField(default=0)),
                ('avg_communication_score', models.FloatField(default=0)),
                ('avg_presentation_score', models.FloatField(default=0)),
                ('total_score', models.FloatField(default=0)),
                ('poster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.students')),
            ],
            options={
                'verbose_name': 'Total Scores Round 1 Graduate',
                'verbose_name_plural': 'Total Scores Round 1 Graduate',
                'db_table': 'total_scores_round_1_graduate',
            },
        ),
        migrations.CreateModel(
            name='Scores_Round_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_score', models.IntegerField(blank=True, null=True)),
                ('communication_score', models.IntegerField(blank=True, null=True)),
                ('presentation_score', models.IntegerField(blank=True, null=True)),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.students')),
            ],
            options={
                'verbose_name': 'Scores Round 2',
                'verbose_name_plural': 'Scores Round 2',
                'db_table': 'scores_round_2',
            },
        ),
        migrations.CreateModel(
            name='Scores_Round_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_score', models.IntegerField(blank=True, null=True)),
                ('communication_score', models.IntegerField(blank=True, null=True)),
                ('presentation_score', models.IntegerField(blank=True, null=True)),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.students')),
            ],
            options={
                'verbose_name': 'Scores Round 1',
                'verbose_name_plural': 'Scores Round 1',
                'db_table': 'scores_round_1',
            },
        ),
    ]
