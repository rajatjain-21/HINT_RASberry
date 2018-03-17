# Generated by Django 2.0.3 on 2018-03-17 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('causes', models.TextField(default='')),
                ('symptoms', models.TextField(blank='')),
                ('diagnosis', models.TextField(blank='')),
                ('complications', models.TextField(blank='')),
                ('medicine', models.TextField(blank='')),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
            ],
        ),
    ]
