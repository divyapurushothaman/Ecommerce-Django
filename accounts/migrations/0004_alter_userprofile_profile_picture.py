# Generated by Django 4.2.5 on 2023-10-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_options_remove_account_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default/default-user.png', upload_to='userprofile'),
        ),
    ]