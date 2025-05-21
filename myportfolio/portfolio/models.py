# portfolio/models.py
from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name


# from django.db import models

# class Project(models.Model):
#     CATEGORY_CHOICES = [
#         ("webapp", "Web App"),
#         ("mobileapp", "Mobile App"),
#         ("aiml", "AI/ML"),
#     ]

#     title = models.CharField(max_length=255)
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     description = models.TextField()
#     thumbnail = models.ImageField(upload_to="portfolio/thumbnails/")
#     preview_image = models.ImageField(upload_to="portfolio/previews/")
#     details_link = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.title



# from django.db import models

# class Project(models.Model):
#     CATEGORY_CHOICES = [
#         ('webapp', 'Web App'),
#         ('mobileapp', 'Mobile App'),
#         ('aiml', 'AI/ML'),
#     ]
    
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     main_image = models.ImageField(upload_to='projects/main_images/')  # Primary image
#     details_link = models.URLField(blank=True, null=True)
    
#     def __str__(self):
#         return self.title


# class ProjectImage(models.Model):
#     project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='projects/gallery/')  # Additional images

#     def __str__(self):
#         return f"Image for {self.project.title}"


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name="projects")  # Multiple categories
    main_image = models.ImageField(upload_to='projects/main_images/')  # Primary image
    details_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')  # Additional images

    def __str__(self):
        return f"Image for {self.project.title}"
