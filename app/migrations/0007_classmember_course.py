# Generated by Django 3.2 on 2021-06-23 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_classmember_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmember',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.course'),
        ),
    ]
