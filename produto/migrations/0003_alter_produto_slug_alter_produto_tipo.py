# Generated by Django 5.0 on 2023-12-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variavel'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
