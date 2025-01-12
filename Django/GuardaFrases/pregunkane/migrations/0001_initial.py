# Generated by Django 4.0.4 on 2022-04-16 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TNom', models.CharField(max_length=5)),
                ('Desc', models.CharField(max_length=200)),
                ('NSFW', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FraseText', models.CharField(max_length=100)),
                ('data', models.DateTimeField(verbose_name='data de la frase')),
                ('Dicho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pregunkane.user')),
                ('Tags', models.ManyToManyField(to='pregunkane.tag')),
            ],
        ),
    ]
