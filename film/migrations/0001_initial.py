# Generated by Django 3.2.5 on 2021-09-14 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idfilm', models.IntegerField(default=0)),
                ('namafilm', models.CharField(default='', max_length=100)),
                ('desc', models.TextField(default='')),
                ('date', models.DateField(default='YYYY-MM-DD', max_length=100)),
                ('poster', models.ImageField(default='media/film/poster/cs.jpg', upload_to='Films')),
                ('genrefilm', models.CharField(default='', max_length=100)),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Xerror_Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tidakdiketahui', models.TextField(blank=True, default='#')),
            ],
        ),
        migrations.CreateModel(
            name='Links_Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_144', models.TextField(blank=True, default='#')),
                ('link_240', models.TextField(blank=True, default='#')),
                ('link_360', models.TextField(blank=True, default='#')),
                ('link_480', models.TextField(blank=True, default='#')),
                ('link_720', models.TextField(blank=True, default='#')),
                ('link_1080', models.TextField(blank=True, default='#')),
                ('verified', models.BooleanField(default=False)),
                ('Film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_link', to='film.film')),
            ],
        ),
    ]
