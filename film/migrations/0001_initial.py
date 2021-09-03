# Generated by Django 3.2.5 on 2021-09-01 04:40

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
                ('namafilm', models.CharField(max_length=100)),
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
                ('type', models.CharField(choices=[('DL', 'DOWNLOAD LINK')], max_length=2)),
                ('link_144', models.TextField(blank=True, default='#')),
                ('link_240', models.TextField(blank=True, default='#')),
                ('link_360', models.TextField(blank=True, default='#')),
                ('link_480', models.TextField(blank=True, default='#')),
                ('link_720', models.TextField(blank=True, default='#')),
                ('link_1080', models.TextField(blank=True, default='#')),
                ('Film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_link', to='film.film')),
            ],
        ),
    ]