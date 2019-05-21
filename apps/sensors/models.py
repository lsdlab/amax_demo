from django.db import models


class Temperature(models.Model):
    temp = models.CharField(max_length=255, blank=False)
    collected_at = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', '-updated_at']
        verbose_name = '温度日志'
        verbose_name_plural = verbose_name
