# Generated by Django 5.1.2 on 2024-11-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/placeholder.jpg', upload_to='images/'),
        ),
    ]