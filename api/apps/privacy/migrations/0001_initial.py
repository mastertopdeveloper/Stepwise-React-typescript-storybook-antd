# Generated by Django 4.0.2 on 2022-03-16 14:44

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Privacy policies',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicyConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'revoked_reason',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('UPDATED', 'User accepted an updated policy'),
                            ('REVOKED', 'User revoked his consent'),
                        ],
                        max_length=16,
                    ),
                ),
                ('revoked_at', models.DateTimeField(blank=True, null=True)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='privacy.privacypolicy')),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='consents',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name='privacypolicy',
            constraint=models.UniqueConstraint(
                condition=models.Q(('is_active', True)), fields=('is_active',), name='unique_active_privacy_policy'
            ),
        ),
        migrations.AddConstraint(
            model_name='privacypolicyconsent',
            constraint=models.UniqueConstraint(fields=('policy', 'user'), name='unique_privacy_policy_consent'),
        ),
    ]
