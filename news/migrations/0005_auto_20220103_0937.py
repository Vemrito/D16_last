

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211214_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_ru',
            field=models.TextField(null=True),
        ),
    ]
