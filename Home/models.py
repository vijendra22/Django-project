from  django.db import models

class Page(models.Model):
    page_name = models.CharField(max_length=250)
    page_num = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.page_name + ' - ' + str(self.page_num)

