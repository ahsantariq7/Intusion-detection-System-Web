# Generated by Django 5.0.2 on 2024-05-19 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesnippet', '0005_alter_projectoutput_output_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='student3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student3', to='codesnippet.student'),
        ),
    ]