# Generated by Django 2.0.6 on 2018-06-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_personalnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='catergory',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
