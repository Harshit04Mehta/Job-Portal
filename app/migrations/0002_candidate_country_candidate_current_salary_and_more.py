# Generated by Django 4.1.3 on 2022-12-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='country',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='current_salary',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='expected_salary',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='highest_education',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='website',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usermaster',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
