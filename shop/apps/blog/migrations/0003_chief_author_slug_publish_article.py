# Generated by Django 4.0.5 on 2022-07-26 13:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='chief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('score', models.CharField(choices=[('senior', 'senior'), ('midlle', 'midlle'), ('junior', 'junior')], max_length=50, verbose_name='جایگاه')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='new_slug'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('chief', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.chief', verbose_name='سر دبیر')),
            ],
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_article', models.CharField(max_length=50, verbose_name='نام مقاله')),
                ('text_article', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیر فعال')),
                ('update', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('publish', 'publish')], max_length=50, verbose_name='وضعیت')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author', verbose_name='نویسنده')),
                ('publish', models.ManyToManyField(to='blog.publish', verbose_name='انتشارات')),
            ],
        ),
    ]
