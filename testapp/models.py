from django.db import models
from django.utils import timezone
from django.core.files.storage import default_storage as storage

import tinify
import requests, os
requests.packages.urllib3.disable_warnings()

tinify.key = "YOUR_API_KEY"
#Basic: tinify.from_file('unoptimized.png').to_file('optimized.png')

class Photo(models.Model):
    title = models.CharField(max_length=200)
    photo = models.FileField(upload_to='photos/%Y/%m/%d/')
    created = models.DateField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)
    auto_delete = models.BooleanField(default=True, help_text="Auto Delete image unoptimized when uploaded.")

    def __unicode__(self):
        return self.title

    def get_image_optimized(self):
        """In your templates: {{ get_image_optimized }}"""
        if self.auto_delete == True:
            return str(self.photo.url)
        return str(os.path.splitext(str(self.photo.url))[0])+'_optimized_' + str(os.path.splitext(str(self.photo.url))[1])

    def optimize(self):
        fh = storage.open(self.photo.name)
        from_file = tinify.from_file(fh)

        image_path = str(os.path.splitext(str(fh))[0])
        extentions = str(os.path.splitext(str(fh))[1])

        if self.auto_delete == True:
            from_file.to_file(image_path+"_optimized_"+extentions) #to optimize
            os.rename(str(self.photo.file.name), image_path+"_origin_"+extentions) #rename original photo
            os.rename(image_path+"_optimized_"+extentions, str(self.photo.file.name)) #rename optimized to original str(self.photo.file.name).
            os.remove(image_path+"_origin_"+extentions) #removing original photo

        else:
            from_file.to_file(image_path+"_optimized_"+extentions) #to optimize

        fh.close()

        return True

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        if not self.optimize():
            raise Exception('Could not create optimation!')

    class Meta:
        verbose_name = "Photos"
        verbose_name_plural = "Detail Photo"
        ordering = ["-created"]
