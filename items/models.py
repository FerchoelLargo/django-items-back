from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib

class Item(models.Model):
	uniqueValue = models.CharField(max_length=40)
	name = models.CharField(max_length=40)
	description = models.CharField(max_length=256)
	quantity = models.IntegerField()
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)



@receiver(post_save, sender=Item, dispatch_uid="set_sysID")
def set_sysID(sender, instance, created,**kwargs):
	if created:
		sys_id = str(instance.id).encode()
		hash_object = hashlib.sha1(sys_id)
		sys_id = hash_object.hexdigest()
		instance.uniqueValue = sys_id

		post_save.disconnect(set_sysID, sender=Item,dispatch_uid="set_sysID")
		instance.save()
		post_save.connect(set_sysID, sender=Item,dispatch_uid="set_sysID")