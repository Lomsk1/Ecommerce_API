# Generated by Django 4.1.4 on 2022-12-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklySale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('text', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='./images/weekly_sale')),
                ('deadline', models.DateField(null=True)),
            ],
        ),
    ]
