from django.contrib import admin
from django.contrib.auth.models import User
from .models import (
                    Gender,
                    Status,
                    Branch,
                    Nss_team_member,
                    Batch,
                    Document,
                    )

# Register your models here.
admin.site.register(Gender)
admin.site.register(Batch)
admin.site.register(Status)
admin.site.register(Branch)
admin.site.register(Nss_team_member)
admin.site.register(Document)


