# Generated by Django 4.0.2 on 2022-11-28 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_rename_item_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('admission_year', models.DateField()),
                ('uneversity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.university')),
            ],
        ),
    ]
