from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver
from upload_page.models import UploadFile
from upload_page.utils import get_format


@receiver(post_save, sender=UploadFile)
def apply_format_to_file(sender, instance, created, **kwargs):
    if created:
        print("Processing file format...")
        with open(instance.format_file.path, 'r') as f:
            django_file = File(f)
            file_contents = django_file.read()
            instance.format = get_format(file_contents)
            instance.save()
        with open(instance.format_file.path, 'w') as f:
            f.write(instance.format)
        print("File format processing completed.")