from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from samples.models import Location, Project, Sample, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    extra = 0
    verbose_name = _("User profile")
    verbose_name_plural = _("User profile")


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "location_name")
    search_fields = ("location_name",)
    ordering = ("location_name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "project_name", "deadline", "project_done", "count_samples", "count_complete_samples")
    list_filter = (
        "deadline",
        "project_done",
    )
    search_fields = ("project_name",)
    ordering = ("project_name",)


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = (
        "original_sample_id",
        "date",
        "location",
        "project",
        "count",
        "length",
        "samples_sum",
        "process_date",
        "complete_date",
        "complete",
        "store",
        "lost",
    )
    list_filter = (
        "complete",
        "store",
        "date",
        "process_date",
        "complete_date",
        "location",
        "project",
    )
    search_fields = (
        "original_sample_id",
        "location__location_name",
        "project__project_name",
    )
    autocomplete_fields = ("location", "project")
    date_hierarchy = "date"
    ordering = ("-date", "-original_sample_id")
    list_select_related = ("location", "project")
    list_per_page = 30
    save_on_top = True

    fieldsets = (
        (_("Identification"), {
            "fields": ("original_sample_id", "created_at",),
        }),
        (_("Basic information"), {
            "fields": ("date", "location", "project"),
        }),
        (_("Sample parameters"), {
            "fields": ("count", "length", "samples_sum"),
        }),
        (_("Processing"), {
            "fields": ("process_date", "zooplankton_analyst", "complete_date", "complete", "store", "lost"),
        }),
    )

    @admin.display(boolean=True, description=_("Completed"))
    def complete_status(self, obj):
        return obj.complete