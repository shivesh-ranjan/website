# Generated by Django 4.1.1 on 2022-10-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailList',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.CharField(max_length=100)),
            ],
        ),
    ]