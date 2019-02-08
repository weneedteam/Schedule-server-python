# Generated by Django 2.1.5 on 2019-01-20 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.IntegerField()),
                ('assented_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='request_user_friend', to=settings.AUTH_USER_MODEL)),
                ('response_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='response_user_friend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assent', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='request_user_request', to=settings.AUTH_USER_MODEL)),
                ('response_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='response_user_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='friendrelation',
            name='request_user',
        ),
        migrations.RemoveField(
            model_name='friendrelation',
            name='response_user',
        ),
        migrations.DeleteModel(
            name='FriendRelation',
        ),
    ]