from django.db import models

# Generate custom field for primary key
# https://docs.djangoproject.com/en/4.0/howto/custom-model-fields/#custom-database-types
# https://stackoverflow.com/a/56306262/9655579
class UnsignedAutoField(models.AutoField):
    def db_type(self, connection):
        return 'INT(8) UNSIGNED ZEROFILL AUTO_INCREMENT'

    def rel_db_type(self, connection):
        return 'INT(8) UNSIGNED ZEROFILL'

class Areas(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    description = models.CharField(max_length=200)

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )