from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from samples.models import Location, Project, Sample


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "location_name")
    search_fields = ("location_name",)
    ordering = ("location_name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "project_name")
    search_fields = ("project_name",)
    ordering = ("project_name",)


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
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
            "fields": ("original_sample_id",),
        }),
        (_("Basic information"), {
            "fields": ("date", "location", "project"),
        }),
        (_("Sample parameters"), {
            "fields": ("count", "length", "samples_sum"),
        }),
        (_("Processing"), {
            "fields": ("process_date", "complete_date", "complete", "store"),
        }),
    )

    @admin.display(boolean=True, description=_("Completed"))
    def complete_status(self, obj):
        return obj.complete