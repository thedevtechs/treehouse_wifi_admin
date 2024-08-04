from django.db import models

class EmailSubscription(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    join_mailing_list = models.BooleanField(default=False)  # Add the new field

    class Meta:
        db_table = 'users'  # Specify the actual table name

    def __str__(self):
        return self.email
