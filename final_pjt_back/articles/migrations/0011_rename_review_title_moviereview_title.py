# Generated by Django 3.2.3 on 2021-05-24 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_rename_title_moviereview_review_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereview',
            old_name='review_title',
            new_name='title',
        ),
    ]
