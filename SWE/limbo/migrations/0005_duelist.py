# Generated by Django 3.1.7 on 2021-04-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limbo', '0004_auto_20210406_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='DueList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
