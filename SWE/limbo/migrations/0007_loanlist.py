# Generated by Django 3.1.7 on 2021-04-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limbo', '0006_hostelallot'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=50)),
                ('book_name', models.CharField(max_length=50)),
                ('isbn_no', models.CharField(max_length=50)),
                ('borrow_date', models.CharField(max_length=50)),
                ('due_date', models.CharField(max_length=50)),
            ],
        ),
    ]
