from django.contrib import admin
from .models import User, Task, JournalEntry

admin.site.register(User)
admin.site.register(Task)
admin.site.register(JournalEntry)
