# Generated by Django 5.0.3 on 2024-04-04 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_yerkir_img_qaxaq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poxoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Poxoci anuny')),
                ('Qaxaq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yer_poxoc', to='main.qaxaq')),
            ],
            options={
                'verbose_name': 'Poxoc',
                'verbose_name_plural': 'Poxocner',
            },
        ),
    ]
