# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url', models.URLField(verbose_name='URL')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_at', models.DateTimeField(verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('category', models.ForeignKey(to='core.Category')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='sub_cat',
            field=models.ForeignKey(to='core.SubCategory'),
        ),
    ]
