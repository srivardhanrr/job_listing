# models.py
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    color_code = models.CharField(max_length=7, default='#6c757d',
                                  help_text="Color code in hex format (e.g., #00a0c6)")
    icon = models.CharField(max_length=50, blank=True,
                            help_text="Icon emoji or code (e.g., 👁️ or 🩺)")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class JobListing(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('remote', 'Remote')
    ]

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='job_listings')
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=2)  # US state abbreviation
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    description = models.TextField(help_text="Enter each bullet point on a new line with a leading hyphen (-)")
    salary_range = models.CharField(max_length=100, blank=True)
    application_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return f"{self.title} - {self.location_city}, {self.location_state}"

    def get_card_color(self):
        return self.category.color_code

    def get_category_icon(self):
        return self.category.icon

    def get_description_points(self):
        points = [point.strip('- ') for point in self.description.split('\n') if point.strip('- ')]
        return points