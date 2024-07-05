# Generated by Django 5.0.2 on 2024-03-31 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesnippet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_name', models.CharField(max_length=100)),
                ('output_image', models.ImageField(upload_to='project_images/')),
                ('output_description', models.TextField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codesnippet.section')),
            ],
        ),
    ]