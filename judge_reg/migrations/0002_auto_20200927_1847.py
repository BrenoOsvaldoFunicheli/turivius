# Generated by Django 3.0.6 on 2020-09-27 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge_reg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrojuridico',
            old_name='cliente',
            new_name='id_cliente',
        ),
    ]