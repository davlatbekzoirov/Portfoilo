from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.db.models import SlugField

class Blog(models.Model):
	title = models.CharField(_("Title"), max_length=255)
	slug = models.SlugField(_("Slug"), max_length=255, unique=True, blank=True)
	description = models.TextField(_("Description"), blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='blog/', verbose_name=_("Image"))
	author = models.ForeignKey(
			get_user_model(),
			on_delete=models.CASCADE,
	)

	def __str__(self):
			return f"{self.author} - {self.date} - {self.title}"

	def save(self, *args, **kwargs):
			if not self.slug:
					self.slug = slugify(self.title)  # Generate slug from title
			super().save(*args, **kwargs)

	class Meta:
			verbose_name = _("Blog")
			verbose_name_plural = _("Blogs")

class Technology(models.Model):
    name = models.CharField(_("Technology Name"), max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")

class Portfolio(models.Model):
	title = models.CharField(_("Title"), max_length=255)
	slug = models.SlugField(_("Slug"), max_length=255, unique=True, blank=True)
	description = models.TextField(_("Description"), blank=True, null=True)
	image = models.ImageField(upload_to='portfolio/', verbose_name=_("Image"))
	technologies = models.ManyToManyField(Technology, verbose_name=_("Technologies Used"), blank=True)
	website_link = models.URLField(_("Website Link"), blank=True, null=True)
	repository_link = models.URLField(_("Repository Link"), blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self):
			return self.title

	def save(self, *args, **kwargs):
			if not self.slug:
					self.slug = slugify(self.title)  
			super().save(*args, **kwargs)

	class Meta:
			verbose_name = _("Portfolio")
			verbose_name_plural = _("Portfolios")
