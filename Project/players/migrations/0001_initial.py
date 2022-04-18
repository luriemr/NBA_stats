# Generated by Django 3.0.7 on 2020-06-17 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(null=True)),
                ('player', models.CharField(max_length=50, null=True)),
                ('pos', models.CharField(max_length=10, null=True)),
                ('age', models.IntegerField(null=True)),
                ('tm', models.CharField(max_length=10, null=True)),
                ('g', models.IntegerField(null=True)),
                ('tspercent', models.FloatField(null=True)),
                ('mpg', models.FloatField(null=True)),
                ('fg', models.IntegerField(null=True)),
                ('fga', models.IntegerField(null=True)),
                ('fgpercent', models.FloatField(null=True)),
                ('threep', models.IntegerField(null=True)),
                ('threepa', models.IntegerField(null=True)),
                ('threeppercent', models.FloatField(null=True)),
                ('twop', models.IntegerField(null=True)),
                ('twopa', models.IntegerField(null=True)),
                ('twoppercent', models.FloatField(null=True)),
                ('efgpercent', models.FloatField(null=True)),
                ('ft', models.IntegerField(null=True)),
                ('fta', models.IntegerField(null=True)),
                ('ftpercent', models.FloatField(null=True)),
                ('rpg', models.FloatField(null=True)),
                ('reb', models.IntegerField(null=True)),
                ('apg', models.FloatField(null=True)),
                ('ast', models.IntegerField(null=True)),
                ('spg', models.FloatField(null=True)),
                ('stl', models.IntegerField(null=True)),
                ('bpg', models.FloatField(null=True)),
                ('blk', models.IntegerField(null=True)),
                ('topg', models.FloatField(null=True)),
                ('tov', models.IntegerField(null=True)),
                ('ppg', models.FloatField(null=True)),
                ('pts', models.IntegerField(null=True)),
            ],
        ),
    ]
