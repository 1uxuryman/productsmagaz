# Generated by Django 4.1.5 on 2023-01-24 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=350)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='text',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.text'),
        ),
    ]
