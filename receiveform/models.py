from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models
import uuid
# Create your models here.

#
class UserEntity(models.Model):
    email = models.EmailField(null=False,primary_key=True,db_index=True)
    public_key = models.UUIDField("publicKey",default=str(uuid.uuid4()))
    private_key = models.UUIDField("privateKey",default=str(uuid.uuid4()),db_index=True)


    @classmethod
    def is_present(cls,email):
        return cls.objects.filter(email=email).count() > 0


class DataStore(models.Model):
    userEntity = models.ForeignKey(UserEntity)
    data = JSONField()
