# Generated by Django 4.0.3 on 2022-08-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandbox', '0003_delete_user_alter_sandbox_body_alter_sandbox_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandbox',
            name='body',
            field=models.TextField(),
        ),
    ]
