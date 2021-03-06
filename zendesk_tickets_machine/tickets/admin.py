from django.contrib import admin

from .models import (
    Ticket,
    TicketZendeskAPIUsage
)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'comment',
        'organization',
        'requester',
        'assignee',
        'ticket_type',
        'due_at',
        'priority',
        'tags',
        'board',
        'is_active',
    )
    list_filter = (
        'board__name',
        'is_active',
    )


@admin.register(TicketZendeskAPIUsage)
class TicketZendeskAPIUsageAdmin(admin.ModelAdmin):
    list_display = (
        'assignee',
        'ticket_type',
        'priority',
        'board',
        'created',
    )
