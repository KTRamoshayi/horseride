from generic.models import *


class UserExtention(Model):
    user = OneToOneField(User, on_delete=CASCADE)

    class Meta:
        ordering = ["user"]
        abstract = True

    def __str__(self):
        return self.user.username


class DisplaySetting(UserExtention):
    small_text = BooleanField(default=False)
    dark_mode = BooleanField(default=False)


class Residence(Address, UserExtention):
    # song = FileField(upload_to='singles/%Y/%m/%d/', null=True, blank=True   )
    pass


class ContactDetail(Contact, UserExtention):
    pass



@receiver(signals.post_save, sender=User)
def profile_setup(sender, instance, *args, **kwargs):
    """
    When user is created, the following models are checked and created if not found

    1. Display Settings
    2. Residence Information
    3. Communication Information

    email is synchronised with account email
    """
    DisplaySetting.objects.get_or_create(user=instance)
    Residence.objects.get_or_create(user=instance)
    ContactDetail.objects.get_or_create(user=instance)
    instance.contactdetail.email=instance.email
    instance.contactdetail.save()
