from django.db import models

class CategoryOption(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    some_text = models.CharField(max_length=255, verbose_name="Some text ?")
    category = models.ForeignKey(CategoryOption, on_delete=models.SET_NULL, null=True)
    time_start = models.DateTimeField()
    time_stop = models.DateTimeField()
    comments = models.TextField(verbose_name="Any comments", blank=True, null=True)

    def __str__(self):
        return self.some_text

from django.db import models

# ... (Keep your existing CategoryOption and Entry models here) ...

class VrajLocation(models.Model):
    kha_paya_gya_tha = models.CharField(max_length=255, verbose_name="Vraj's kha paya gya tha")
    kis_jagah = models.CharField(max_length=255, verbose_name="kis jagah")
    time_kya_tha = models.DateTimeField(verbose_name="time kya tha")

    def __str__(self):
        return f"{self.kha_paya_gya_tha} - {self.kis_jagah}"