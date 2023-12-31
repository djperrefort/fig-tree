# Generated by Django 4.2.7 on 2023-11-26 20:27

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
                ('event_type', models.CharField(max_length=255)),
                ('date_type', models.IntegerField(choices=[(0, 'regular'), (1, 'before'), (2, 'after'), (3, 'about'), (4, 'range'), (5, 'span')], default='regular')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
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
                'verbose_name_plural': 'Families',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('given_name', models.CharField(blank=True, max_length=255, null=True)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('prefix', models.CharField(blank=True, max_length=255, null=True)),
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
                ('type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'verbose_name_plural': 'Repositories',
            },
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('href', models.TextField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('last_accessed', models.DateField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gen_data.repository')),
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
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, null=True)),
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
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('pubinfo', models.CharField(blank=True, max_length=500, null=True)),
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
                ('name', models.CharField(max_length=255)),
                ('place_type', models.CharField(blank=True, max_length=255, null=True)),
                ('enclosed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gen_data.place')),
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
                ('sex', models.IntegerField(blank=True, choices=[(0, 'female'), (1, 'male'), (2, 'other')], null=True)),
                ('alternate_names', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persons_alternate', to='gen_data.name')),
                ('birth', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_birth', to='gen_data.event')),
                ('death', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_death', to='gen_data.event')),
                ('families', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='gen_data.family')),
                ('nick_names', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_nick', to='gen_data.name')),
                ('parent_families', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people_parent', to='gen_data.family')),
                ('primary_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persons_primary', to='gen_data.name')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('blob', models.ImageField(upload_to='')),
                ('date_type', models.IntegerField(choices=[(0, 'regular'), (1, 'before'), (2, 'after'), (3, 'about')], default='regular')),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.AddField(
            model_name='family',
            name='children',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_child', to='gen_data.person'),
        ),
        migrations.AddField(
            model_name='family',
            name='parent1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_parent1', to='gen_data.person'),
        ),
        migrations.AddField(
            model_name='family',
            name='parent2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_parent2', to='gen_data.person'),
        ),
        migrations.AddField(
            model_name='family',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gen_data.place'),
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
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('page_or_reference', models.CharField(blank=True, max_length=100, null=True)),
                ('confidence', models.IntegerField(choices=[(0, 'low'), (1, 'regular'), (2, 'high')], default=1)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gen_data.source')),
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
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('line1', models.CharField(max_length=255, verbose_name='Line 1')),
                ('line2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Line 2')),
                ('line3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Line 3')),
                ('line4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Line 4')),
                ('municipality', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('lat', models.IntegerField(blank=True, null=True, verbose_name='Latitude')),
                ('long', models.IntegerField(blank=True, null=True, verbose_name='Longitude')),
                ('date', models.DateField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
