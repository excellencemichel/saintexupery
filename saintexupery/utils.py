import os
import random
import string

from datetime import datetime

from django.utils.text import slugify





def get_filename(filepath):
	base_name = os.path.basename(filepath)
	name_file, extension_file = os.path.splitext(base_name)
	return name_file, extension_file



def upload_file_location(instance, filename):
	id_ = instance.id
	if id_ is None:
		Klass = instance.__class__
		qs = Klass.objects.all().order_by("-pk")
		if qs.exists():
			id_ = qs.first().id + 1
		else:
			id_ = 0
	name_file, extension_file =get_filename(filename)

	salt_path = datetime.now().strftime('instance.__class__.__name__/%Y/%m/%d')

	final_filename = "{name_file}_{id_}{extension_file}".format(name_file=name_file, id_=id_, extension_file=extension_file)

	return "{salt_path}/{final_filename}".format(salt_path=salt_path, final_filename=final_filename)

	




def random_string_generator(size=12, chars = string.ascii_lowercase + string.digits):
	return "".join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
	"""
	This is for a Django project and it assumes your instance
	has a model with a slug field and a title character (char)field
	"""
	if new_slug is not None:
		slug = new_slug

	else:
		slug = slugify(instance.title)


	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug=slug).exists()
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=12))


		return unique_slug_generator(instance, new_slug=new_slug)

	return slug



def unique_slug_generator_identif(instance, identif, new_slug=None):
	"""
	This is for a Django project and it assumes your instance
	has a model with a slug field and a title character (char)field
	"""
	if new_slug is not None:
		slug = new_slug

	else:
		slug = slugify(identif)


	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug=slug).exists()
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=12))


		return unique_slug_generator(instance, new_slug=new_slug)

	return slug


def unique_slug_generator_for_null(instance, new_slug=None):
	"""
	This is for a Django project and it assumes your instance
	has a model with a slug field and a title character (char)field
	"""
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.info)

	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug=slug).exists()
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=33))


		return unique_slug_generator(instance, new_slug=new_slug)

	return slug