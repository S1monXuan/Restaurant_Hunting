from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    customer_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                             content_type__model='customer')

    year_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                          content_type__model='year')

    season_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                                  content_type__model='season')

    section_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                                  content_type__model='section')

    holder_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                           content_type__model='holder')

    place_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                         content_type__model='place')

    type_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                          content_type__model='type')

    restaurant_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                               content_type__model='restaurant')

    comment_permissions = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                               content_type__model='comment')

    perm_view_customer = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                           content_type__model='customer',
                                                           codename='view_customer')

    perm_view_year = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                        content_type__model='year',
                                                        codename='view_year')

    perm_view_season = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                               content_type__model='season',
                                                               codename='view_season')

    perm_view_section = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                               content_type__model='section',
                                                               codename='view_section')

    perm_view_holder = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                         content_type__model='holder',
                                                         codename='view_holder')

    perm_view_place = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                       content_type__model='place',
                                                       codename='view_place')

    perm_view_type = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                        content_type__model='type',
                                                        codename='view_type')

    perm_view_restaurant = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                             content_type__model='restaurant',
                                                             codename='view_restaurant')

    perm_view_comment = permission_class.objects.filter(content_type__app_label='rateinfo',
                                                             content_type__model='comment',
                                                             codename='view_comment')

    ci_customer_permissions = chain(perm_view_customer,
                                perm_view_section,
                                perm_view_holder,
                                perm_view_place,
                                perm_view_type,
                                perm_view_restaurant,
                                perm_view_comment,
                                comment_permissions,
                                customer_permissions
                                    )

    ci_holder_permissions = chain(
                                perm_view_section,
                                perm_view_holder,
                                perm_view_place,
                                perm_view_type,
                                perm_view_restaurant,
                                perm_view_comment,
                                restaurant_permissions,
                                holder_permissions)

    ci_manager_permissions = chain(perm_view_customer,
                                perm_view_year,
                                perm_view_season,
                                perm_view_section,
                                perm_view_holder,
                                perm_view_place,
                                perm_view_type,
                                perm_view_restaurant,
                                perm_view_comment,
                                customer_permissions,
                                year_permissions,
                                season_permissions,
                                section_permissions,
                                holder_permissions,
                                place_permissions,
                                type_permissions,
                                restaurant_permissions,
                                comment_permissions,
                                   )

    my_groups_initialization_list = [
        {
            "name": "ci_customer",
            "permissions_list": ci_customer_permissions,
        },
        {
            "name": "ci_holder",
            "permissions_list": ci_holder_permissions,
        },
        {
            "name": "ci_manager",
            "permissions_list": ci_manager_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('rateinfo', '0006_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]