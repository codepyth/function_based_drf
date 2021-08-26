# Generated by Django 3.2.6 on 2021-08-24 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210824_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrelations',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prs', to='core.product'),
        ),
        migrations.AlterField(
            model_name='financial',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financial', to='core.product'),
        ),
        migrations.AlterField(
            model_name='property',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='core.product'),
        ),
    ]