# Generated by Django 4.1.2 on 2022-10-17 11:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('innoapp', '0003_post_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
