from django.contrib.auth.models import User
from django.db import models


class AdminUser(User):
    class Meta:
        proxy = True

    def is_active_administrator(self):
        return self.is_active and self.is_superuser
    


