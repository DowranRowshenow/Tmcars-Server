# Generated by Django 4.2.6 on 2023-10-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('hash', models.CharField(blank=True, max_length=64, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='products')),
            ],
            options={
                'ordering': ['image'],
            },
        ),
    ]
