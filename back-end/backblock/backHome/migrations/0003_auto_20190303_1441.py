# Generated by Django 2.1.7 on 2019-03-03 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backHome', '0002_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='userName',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='userPass',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
