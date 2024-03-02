# Generated by Django 5.0.2 on 2024-03-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('direccion_envio', models.CharField(max_length=100)),
                ('cantidad_productos', models.PositiveIntegerField()),
                ('pagado', models.BooleanField(default=False)),
            ],
        ),
    ]
