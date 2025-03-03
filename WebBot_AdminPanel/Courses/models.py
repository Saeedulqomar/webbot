from django.db import models

class Course(models.Model):

    course_type = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Позволяет оставлять описание пустым
    course_name = models.CharField(max_length=255)  # Уникальность зависит от требований
    professor = models.ForeignKey('Professors.Professor', related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name