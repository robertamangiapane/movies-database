# Generated by Django 3.0.4 on 2020-03-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('watched', models.CharField(default='No', max_length=3)),
                ('date', models.DateTimeField()),
                ('review', models.CharField(max_length=500)),
                ('other', models.CharField(max_length=200)),
            ],
        ),
    ]
