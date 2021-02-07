# Generated by Django 3.1.5 on 2021-02-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category_order', models.IntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('is_special', models.BooleanField(default=False)),
            ],
        ),
    ]
