# Generated by Django 3.1.6 on 2021-03-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=100, verbose_name='職種')),
                ('campany', models.CharField(max_length=100, verbose_name='会社')),
                ('description', models.TextField(verbose_name='説明')),
                ('place', models.CharField(max_length=100, verbose_name='場所')),
                ('period', models.CharField(max_length=100, verbose_name='期間')),
            ],
        ),
    ]
