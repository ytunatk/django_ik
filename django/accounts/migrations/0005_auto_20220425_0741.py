# Generated by Django 3.2.13 on 2022-04-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220425_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofil',
            name='autoBiography',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userprofil',
            name='coverLetter',
            field=models.TextField(),
        ),
    ]