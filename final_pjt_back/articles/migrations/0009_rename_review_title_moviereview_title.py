# Generated by Django 3.2.3 on 2021-05-24 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20210524_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereview',
            old_name='review_title',
            new_name='title',
        ),
    ]