# Generated by Django 3.2.25 on 2024-11-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='execution',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='exercise',
            name='starting_position',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='Bodypart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('similar_bodyparts', models.ManyToManyField(blank=True, related_name='_exercises_bodypart_similar_bodyparts_+', to='exercises.Bodypart')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='main_muscles',
            field=models.ManyToManyField(blank=True, related_name='primary_exercises', to='exercises.Bodypart'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='secondary_muscles',
            field=models.ManyToManyField(blank=True, related_name='secondary_exercises', to='exercises.Bodypart'),
        ),
    ]
