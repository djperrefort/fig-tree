# Generated by Django 4.2.7 on 2023-11-08 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family_trees', '0001_initial'),
        ('gen_rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='address',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citation',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='citation',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='family',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='family',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='media',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='name',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='name',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='note',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='place',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repository',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='source',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='source',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='url',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family_trees.familytree'),
            preserve_default=False,
        ),
    ]
