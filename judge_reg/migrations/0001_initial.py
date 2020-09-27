# Generated by Django 3.0.6 on 2020-09-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroJuridico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_processo', models.CharField(max_length=30)),
                ('cliente', models.IntegerField()),
                ('favor_contribuinte', models.CharField(choices=[('0', 'Contrário ao Cliente'), ('1', 'Parcialmente Favorável'), ('2', 'Favorável ao Cliente')], max_length=2)),
                ('ementa', models.CharField(max_length=4000)),
            ],
        ),
    ]
