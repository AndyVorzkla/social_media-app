import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Profile(models.Model):
    class RelationshipChoices(models.TextChoices):
        NONE = '', _('None')
        SINGLE = 'single', _('Single')
        IN_A_RELATIONSHIP = 'relationship', _('In a relationship')
        MARRIED = 'married', _('Married')
        ENGAGED = 'engaged', _('Engaged')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images/', default='default-profile.png')
    location = models.CharField(max_length=100, blank=True)
    working_at = models.CharField(max_length=200, blank=True, default='')
    relationship = models.TextField(_('relationship'), choices=RelationshipChoices.choices, default='', blank=True)

    def __str__(self):
        return self.user.username
