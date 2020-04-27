# Generated by Django 2.2.7 on 2020-04-27 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imgUrl', models.CharField(max_length=300)),
                ('boneDate', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=12, null=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('priceStandard', models.CharField(max_length=10)),
                ('coverSmallUrl', models.CharField(max_length=150)),
                ('coverLargeUrl', models.CharField(max_length=150)),
                ('publisher', models.CharField(max_length=30)),
                ('translator', models.CharField(max_length=30)),
                ('pubDate', models.CharField(max_length=10)),
                ('contents', models.TextField()),
                ('publisherReview', models.TextField(null=True)),
                ('author', models.ManyToManyField(blank=True, related_name='author_books', to='api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MainCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=140, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetailCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('book_category', models.ManyToManyField(blank=True, related_name='favoriteCategory', to=settings.AUTH_USER_MODEL)),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SubCategory')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='detailCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DetailCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='like_user',
            field=models.ManyToManyField(blank=True, related_name='like_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='mainCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.MainCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='subCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SubCategory'),
        ),
    ]
