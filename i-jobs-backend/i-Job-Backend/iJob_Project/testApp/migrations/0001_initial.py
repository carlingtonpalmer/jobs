# Generated by Django 2.1.3 on 2018-12-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('number', models.DateField(null=True)),
            ],
        ),
    ]
