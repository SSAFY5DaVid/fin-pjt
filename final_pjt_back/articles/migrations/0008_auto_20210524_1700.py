# Generated by Django 3.2.3 on 2021-05-24 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_moviereview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereview',
            old_name='title',
            new_name='review_title',
        ),
        migrations.RemoveField(
            model_name='moviereview',
            name='username',
        ),
    ]