# Generated by Django 4.0.5 on 2022-10-06 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_coment_serv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='serv',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
            preserve_default=False,
        ),
    ]
