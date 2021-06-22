from django.db import models


# Create your models here.
class Note(models.Model):
    note_of_subject = models.CharField(max_length=50, blank=False, null=False)
    note_of_semester = models.CharField(max_length=50, blank=False, null=False)
    note_title = models.CharField(max_length=220, blank=False, null=False)
    note_file = models.FileField(upload_to='documents/%Y/%m/%d/')
    note_description = models.TextField(max_length=200, blank=True, null=False)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_uploaded']

    def __str__(self):
        return self.note_title
