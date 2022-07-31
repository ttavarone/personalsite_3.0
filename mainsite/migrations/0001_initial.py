# Generated by Django 4.0.6 on 2022-07-31 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='firstname', max_length=32)),
                ('last_name', models.CharField(default='lastname', max_length=32)),
                ('email_address', models.EmailField(default='email@email.com', max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('biography', models.TextField(default='No Bio')),
                ('last_update', models.DateTimeField(verbose_name='Last info update')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='sitename', max_length=32)),
                ('site_url', models.URLField(max_length=256)),
                ('username', models.CharField(default='username', max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(default='skillname', max_length=64)),
                ('skill_level', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='mainsite.profile')),
            ],
        ),
    ]
