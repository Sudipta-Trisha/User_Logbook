# Generated by Django 4.2.7 on 2023-11-29 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.IntegerField(max_length=20)),
                ('country', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_types', models.CharField(choices=[('Parent', 'Parent'), ('Child', 'Child')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('user_address_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_Active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_addresses', to='users.user')),
            ],
        ),
    ]
