# Generated by Django 3.2.5 on 2022-06-01 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200528_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Phone', models.IntegerField(default=0)),
                ('Email', models.EmailField(max_length=40)),
                ('Note', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Adulte',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Children',
            field=models.CharField(max_length=20),
        ),
    ]
