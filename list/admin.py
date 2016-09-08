from django.contrib import admin

from list.models import List, ListItem, Item


class ListAdmin(admin.ModelAdmin):
    # ordering = ['-date']

    fields = (
        'title',
        'publish_date',
        'slug',
        'user',
        'is_published',
        'description',
    )

    list_display = (
        'title',
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['initial'] = request.user.id

        return super(ListAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

class ListItemAdmin(admin.ModelAdmin):
    # ordering = ['-date']

    fields = (
        'title',
        'publish_date',
        'slug',
        'user',
        'is_published',
        'notes',
    )

    list_display = (
        'title',
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['initial'] = request.user.id

        return super(ListItemAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


class ItemAdmin(admin.ModelAdmin):
    pass
    # fields = (
    #     'title',
    #     'publish_date',
    #     'slug',
    #     'user',
    #     'is_published',
    # )


admin.site.register(List, ListAdmin)
admin.site.register(ListItem, ListItemAdmin)
admin.site.register(Item, ItemAdmin)
