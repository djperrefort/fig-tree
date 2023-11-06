# Generated by Django 4.2.5 on 2023-11-06 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('family_trees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('date_type', models.IntegerField(choices=[(0, 'regular'), (1, 'before'), (2, 'after'), (3, 'about'), (4, 'range'), (5, 'span')], default='regular')),
                ('event_type', models.TextField()),
                ('year_start', models.IntegerField(null=True)),
                ('month_start', models.IntegerField(null=True)),
                ('day_start', models.IntegerField(null=True)),
                ('year_end', models.IntegerField(null=True)),
                ('month_end', models.IntegerField(null=True)),
                ('day_end', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('given_name', models.TextField(null=True)),
                ('surname', models.TextField(null=True)),
                ('suffix', models.TextField(null=True)),
                ('prefix', models.TextField(null=True)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('type', models.TextField()),
                ('name', models.TextField()),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('href', models.TextField()),
                ('name', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gen_rest_api.repository')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('pubinfo', models.CharField(blank=True, max_length=250, null=True)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('place_type', models.TextField(null=True)),
                ('enclosed_by', models.IntegerField(null=True)),
                ('latitude', models.CharField(max_length=10, null=True)),
                ('longitude', models.CharField(max_length=10, null=True)),
                ('code', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('sex', models.IntegerField(choices=[(0, 'female'), (1, 'male'), (2, 'other')], null=True)),
                ('alternate_names', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persons_alternate', to='gen_rest_api.name')),
                ('birth', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_birth', to='gen_rest_api.event')),
                ('death', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_death', to='gen_rest_api.event')),
                ('families', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='gen_rest_api.family')),
                ('nick_names', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_nick', to='gen_rest_api.name')),
                ('parent_families', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people_parent', to='gen_rest_api.family')),
                ('primary_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persons_primary', to='gen_rest_api.name')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('text', models.TextField()),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('relative_path', models.FilePathField()),
                ('date', models.DateField(null=True)),
                ('description', models.TextField(null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='family',
            name='children',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_child', to='gen_rest_api.person'),
        ),
        migrations.AddField(
            model_name='family',
            name='parent1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_parent1', to='gen_rest_api.person'),
        ),
        migrations.AddField(
            model_name='family',
            name='parent2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_parent2', to='gen_rest_api.person'),
        ),
        migrations.AddField(
            model_name='family',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
        ),
        migrations.AddField(
            model_name='event',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gen_rest_api.person'),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='gen_rest_api.place'),
        ),
        migrations.AddField(
            model_name='event',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('page_or_reference', models.CharField(blank=True, max_length=100, null=True)),
                ('confidence', models.IntegerField(choices=[(0, 'low'), (1, 'regular'), (2, 'high')], default=1)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gen_rest_api.source')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('line1', models.CharField(max_length=250, verbose_name='Line 1')),
                ('line2', models.CharField(blank=True, max_length=250, null=True, verbose_name='Line 2')),
                ('lat', models.IntegerField(blank=True, null=True, verbose_name='Latitude')),
                ('long', models.IntegerField(blank=True, null=True, verbose_name='Longitude')),
                ('municipality', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
