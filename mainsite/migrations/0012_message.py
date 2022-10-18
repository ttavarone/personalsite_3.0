# Generated by Django 4.0 on 2022-10-18 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_alter_accomplishment_image_dir'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('email', models.EmailField(default='unknown@email.com', max_length=254)),
                ('message', models.TextField(default='Message body')),
                ('date_received', models.DateTimeField(verbose_name='Date message received')),
            ],
        ),
    ]