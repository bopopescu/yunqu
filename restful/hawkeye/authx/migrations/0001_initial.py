# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./authx/migrations/0001_initial.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 2715 bytes
from __future__ import unicode_literals
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion, uuid

class Migration(migrations.Migration):
    initial = True
    dependencies = [
     ('auth', '0008_alter_user_username_max_length')]
    operations = [
     migrations.CreateModel(name='User',
       fields=[
      (
       'password', models.CharField(max_length=128, verbose_name='password')),
      (
       'last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
      (
       'is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
      (
       'id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
      (
       'created_at', models.DateTimeField(auto_now_add=True)),
      (
       'updated_at', models.DateTimeField(auto_now=True)),
      (
       'username', models.CharField(max_length=11, unique=True, verbose_name='')),
      (
       'fullname', models.CharField(blank=True, max_length=80, verbose_name='')),
      (
       'thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail', verbose_name='')),
      (
       'is_active', models.BooleanField(default=True)),
      (
       'is_admin', models.BooleanField(default=False)),
      (
       'is_staff', models.BooleanField(default=False)),
      (
       'phone_number', models.CharField(blank=True, max_length=30, null=True)),
      (
       'email', models.CharField(blank=True, max_length=30, null=True)),
      (
       'groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
      (
       'owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
      (
       'user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'))],
       options={'verbose_name':'', 
      'verbose_name_plural':'', 
      'db_table':'auth_user', 
      'permissions':(('view_user', 'Can drive'), )})]
# okay decompiling ./restful/hawkeye/authx/migrations/0001_initial.pyc