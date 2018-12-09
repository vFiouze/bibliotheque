# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-05 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AUTHOR_ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('AUTHOR_NAME', models.CharField(max_length=50)),
                ('AUTHOR_LAST_NAME', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'AUTHOR',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('DOCUMENT_ID', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('DOCUMENT_AUTHOR_TYPE', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bibliothequeapp.Author')),
            ],
            options={
                'db_table': 'DOCUMENT',
            },
        ),
        migrations.CreateModel(
            name='Document_Type',
            fields=[
                ('DOCUMENT_TYPE_ID', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('DOCUMENT_TYPE_DESC', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'DOCUMENT_TYPE',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('LOAN_ID', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('LOAN_ORDINAL', models.IntegerField(default=1)),
                ('LOAN_START_DATE', models.DateField(auto_now_add=True)),
                ('LOAN_END_PREDICT_DATE', models.DateField()),
                ('LOAN_END_EFFECTIVE_DATE', models.DateField()),
                ('LOAN_IS_EXTENDED', models.BooleanField()),
                ('LOAN_DOCUMENT_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bibliothequeapp.Document')),
            ],
            options={
                'db_table': 'LOAN',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('PERSON_ID', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('PERSON_NAME', models.CharField(max_length=50)),
                ('PERSON_LAST_NAME', models.CharField(max_length=50)),
                ('PERSON_DT_BIRTH', models.DateField()),
                ('PERSON_STREET_NAME', models.CharField(max_length=50)),
                ('PERSON_ZIP_CODE', models.CharField(max_length=5)),
                ('PERSON_CITY', models.CharField(max_length=20)),
                ('PERSON_COUNTRY', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'PERSON',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('MEMBER_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='bibliothequeapp.Person')),
                ('MEMBER_DT_JOIN', models.DateField()),
                ('MEMBER_IS_ACTIVE', models.BooleanField()),
            ],
            options={
                'db_table': 'MEMBER',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='DOCUMENT_TYPE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bibliothequeapp.Document_Type'),
        ),
        migrations.AddField(
            model_name='loan',
            name='LOAN_MEMBER_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bibliothequeapp.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='loan',
            unique_together=set([('LOAN_ID', 'LOAN_ORDINAL')]),
        ),
    ]
