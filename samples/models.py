from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("User"),
    )
    zooplankton_analyst = models.BooleanField(
        verbose_name=_("Zooplankton analyst"),
        default=False,
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _("User profile")
        verbose_name_plural = _("User profiles")

class Location(models.Model):
    location_name = models.CharField(max_length=255, unique=True, verbose_name=_("Location"))

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")


class Project(models.Model):
    project_name = models.CharField(max_length=255, unique=True, verbose_name=_("Project"))

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


class Sample(models.Model):
    original_sample_id = models.PositiveIntegerField(verbose_name=_("Original sample ID"), unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name=_("Location"))
    date = models.DateField(verbose_name=_("Date"))
    count = models.PositiveSmallIntegerField(
        verbose_name=_("Number of throws"),
        help_text=_("Number of throws in the sample. If that was not possible, enter 0 - Details are in the laboratory’s main database."),
    )
    length = models.PositiveSmallIntegerField(verbose_name=_("Throw length"))
    samples_sum = models.PositiveSmallIntegerField(verbose_name=_("Number of samples"))
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name=_("Project"),
        null=True,
        blank=True,
    )
    process_date = models.DateField(verbose_name=_("Sample handover date"))
    complete_date = models.DateField(verbose_name=_("Data delivery date"))
    complete = models.BooleanField(verbose_name=_("Completed"), default=False)
    store = models.BooleanField(verbose_name=_("Keep stored"), default=True)
    lost = models.BooleanField(verbose_name=_("Lost sample"), default=False)

    def __str__(self):
        return f"{self.location} - {self.date}"

    class Meta:
        verbose_name = _("Sample")
        verbose_name_plural = _("Samples")