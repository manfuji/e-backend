# Generated by Django 4.0.1 on 2022-01-13 08:40

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
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=150)),
                ('Description', models.TextField()),
                ('Link', models.CharField(max_length=255)),
                ('Level', models.CharField(choices=[('BEGINNER', 'BEGINNER'), ('INTERMEDIATE', 'INTERMEDIATE'), ('ADVANCE', 'ADVANCE'), ('MASTERCLASS', 'MASTERCLASS')], default='BEGINNER', max_length=50)),
                ('No_of_videos', models.CharField(max_length=50)),
                ('Created_By', models.CharField(max_length=50)),
                ('Status', models.BooleanField(default=True)),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('Udated_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('Content', models.TextField()),
                ('Commented_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Allmodels.postmodel')),
            ],
        ),
    ]