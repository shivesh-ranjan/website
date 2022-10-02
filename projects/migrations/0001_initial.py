# Generated by Django 4.1.1 on 2022-10-02 13:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=70)),
                ('Tag', models.CharField(max_length=30)),
                ('Body', ckeditor.fields.RichTextField()),
                ('TimeStamp', models.DateTimeField(blank=True)),
                ('Source', models.CharField(max_length=300)),
                ('Deploy', models.CharField(max_length=300)),
            ],
        ),
    ]