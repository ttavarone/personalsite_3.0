# Generated by Django 4.0.6 on 2022-08-01 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_profile_alternate_email_profile_alternate_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomplishment',
            name='image_dir',
            field=models.FilePathField(default='mainsite/', path='mainsite/static/mainsite/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='image_dir',
            field=models.FilePathField(default='mainsite/', path='mainsite/static/mainsite/images/'),
            preserve_default=False,
        ),
    ]
