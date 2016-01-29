from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models
import uuid
# Create your models here.

#
class UserEntity(models.Model):
    email = models.EmailField(null=False)
    public_key = models.UUIDField("publicKey",default=str(uuid.uuid4()))
    private_key = models.UUIDField("privateKey",default=str(uuid.uuid4()))


class DataStore(models.Model):
    userEntity = models.ForeignKey(UserEntity)
    data = JSONField()
