# Generated by Django 4.0.6 on 2022-08-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_through_num_user_cleantrashnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]
