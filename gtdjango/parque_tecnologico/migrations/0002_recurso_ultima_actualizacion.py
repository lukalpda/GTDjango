# Generated by Django 2.1.1 on 2018-10-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parque_tecnologico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now_add=True, null=True, ),
        ),
    ]
