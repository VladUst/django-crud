# Generated by Django 4.0.2 on 2022-12-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0004_rename_uneversity_student_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_year',
            field=models.CharField(max_length=10),
        ),
    ]
