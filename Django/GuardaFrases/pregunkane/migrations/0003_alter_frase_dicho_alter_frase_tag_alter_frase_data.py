# Generated by Django 4.0.4 on 2022-04-17 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pregunkane', '0002_rename_tags_frase_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frase',
            name='Dicho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='pregunkane.user'),
        ),
        migrations.AlterField(
            model_name='frase',
            name='Tag',
            field=models.ManyToManyField(related_name='Tags', to='pregunkane.tag'),
        ),
        migrations.AlterField(
            model_name='frase',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
