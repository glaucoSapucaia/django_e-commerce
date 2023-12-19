# Generated by Django 5.0 on 2023-12-19 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao_curta', models.TextField(max_length=255)),
                ('descricao_longa', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m')),
                ('slug', models.SlugField(unique=True)),
                ('preco_marketing', models.FloatField()),
                ('preco_marketing_promocional', models.FloatField(default=0)),
                ('tipo', models.CharField(choices=[('V', 'Variação'), ('S', 'Simples')], default='V', max_length=1)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
