# Generated by Django 3.1.4 on 2022-11-09 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_auto_20221109_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]