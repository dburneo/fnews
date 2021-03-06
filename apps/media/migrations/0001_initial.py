# Generated by Django 3.0.2 on 2020-01-12 02:00

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('url', models.URLField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('visible', models.BooleanField(default=True, verbose_name='¿Tiene vista previa?')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='country.Country')),
                ('languages', models.ManyToManyField(blank=True, to='country.Language')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Medias',
            },
        ),
    ]
