# Generated by Django 3.2.3 on 2021-05-24 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_rename_review_title_moviereview_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereview',
            old_name='title',
            new_name='review_title',
        ),
    ]
