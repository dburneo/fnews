# Generated by Django 3.0.2 on 2020-01-12 09:01

import apps.news.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsWithRead',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('title', models.TextField()),
                ('short_desc', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('photo', models.URLField(blank=True, null=True)),
                ('order', models.IntegerField(default=apps.news.models.order_random)),
                ('readlater', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'news_news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('title', models.TextField()),
                ('short_desc', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('photo', models.URLField(blank=True, max_length=380, null=True)),
                ('order', models.IntegerField(default=apps.news.models.order_random)),
                ('long_desc', models.TextField(blank=True, null=True)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.Language')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Media')),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'News',
                'unique_together': {('link', 'title')},
            },
        ),
        migrations.CreateModel(
            name='Verbs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(default='algo')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_verbs_news', to='news.News')),
            ],
        ),
        migrations.CreateModel(
            name='ReadLater',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('readed', models.BooleanField(default=False)),
                ('marked', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_readlater_news', to='news.News')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_readlater_news', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ReadLater',
                'verbose_name_plural': 'ReadLaters',
            },
        ),
        migrations.CreateModel(
            name='MediaInterest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('marked', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Media', verbose_name='Medio de Prensa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_mediainterest_news', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Medios de interes',
                'verbose_name_plural': 'Medios de Interes',
            },
        ),
        migrations.CreateModel(
            name='FollowNew',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('readed', models.BooleanField(default=False)),
                ('marked', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('until', models.DateTimeField(blank=True, null=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_follownew_news', to='news.News')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_follownew_news', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'FullNewsText',
                'verbose_name_plural': 'FullNewsTexts',
            },
        ),
    ]