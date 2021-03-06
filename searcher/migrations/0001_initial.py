# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-14 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('session', models.IntegerField(blank=True, null=True)),
                ('meeting_type', models.CharField(blank=True, max_length=1024, null=True)),
                ('heading_type', models.CharField(blank=True, max_length=1024, null=True)),
                ('heading', models.CharField(blank=True, max_length=1024, null=True)),
                ('subheading_type', models.CharField(blank=True, max_length=1024, null=True)),
                ('subheading', models.CharField(blank=True, max_length=1024, null=True)),
                ('party', models.CharField(blank=True, max_length=1024, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('member_office', models.CharField(blank=True, max_length=1024, null=True)),
                ('has_been_scraped', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_id', models.CharField(blank=True, max_length=256, null=True)),
                ('sp_ref', models.CharField(blank=True, max_length=128, null=True)),
                ('sub_type', models.CharField(blank=True, max_length=128, null=True)),
                ('party', models.CharField(blank=True, max_length=256, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('is_potential_mb', models.BooleanField(default=False)),
                ('has_cross_party_support', models.BooleanField(default=False)),
                ('has_been_scraped', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_id', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('is_msp', models.BooleanField(default=True)),
                ('has_been_scraped', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_id', models.CharField(blank=True, max_length=256, null=True)),
                ('sp_ref', models.CharField(blank=True, max_length=128, null=True)),
                ('sub_type', models.CharField(blank=True, max_length=128, null=True)),
                ('party', models.CharField(blank=True, max_length=256, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('answer_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('answer_text', models.TextField(blank=True, null=True)),
                ('answered_by', models.CharField(blank=True, max_length=256, null=True)),
                ('has_been_scraped', models.BooleanField(default=False)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='searcher.Person')),
            ],
        ),
        migrations.AddField(
            model_name='motion',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='searcher.Person'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='searcher.Person'),
        ),
    ]
