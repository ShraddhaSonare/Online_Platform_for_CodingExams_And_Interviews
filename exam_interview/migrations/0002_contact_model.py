# Generated by Django 4.0 on 2022-03-31 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_interview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('desc', models.CharField(max_length=4141)),
            ],
        ),
    ]
