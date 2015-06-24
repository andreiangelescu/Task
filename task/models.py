from urlparse import urlparse

from django.core.urlresolvers import reverse
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    due_date = models.DateField('Due date')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('account.MyUser', null=True)

    def delete_task(self):
        return reverse('task_manager:delete', args=(self.pk,))

    def get_edit_url(self):
        return reverse('task_manager:edit', args=(self.pk,))

    def __unicode__(self):
        return self.title