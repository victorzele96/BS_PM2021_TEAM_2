# Generated by Django 3.1.7 on 2021-04-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyBuddy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ID_TZ',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='Parent_1_Phone',
            field=models.CharField(blank=True, max_length=10, verbose_name='Parent_1_Phone'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Parent_1_first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Parent_1_first_name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Parent_2_Phone',
            field=models.CharField(blank=True, max_length=10, verbose_name='Parent_2_Phone'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Parent_2_first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Parent_2_first_name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Personal_Phone',
            field=models.CharField(blank=True, max_length=10, verbose_name='Personal Phone'),
        ),
    ]
