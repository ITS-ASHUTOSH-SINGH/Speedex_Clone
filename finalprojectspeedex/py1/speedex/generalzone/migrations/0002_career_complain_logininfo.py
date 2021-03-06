# Generated by Django 2.2.3 on 2019-07-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('qualification', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=10)),
                ('keyskills', models.TextField()),
                ('cv', models.CharField(max_length=100)),
                ('connectdate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('complaintext', models.TextField()),
                ('complaindate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('usertype', models.CharField(max_length=20)),
            ],
        ),
    ]
