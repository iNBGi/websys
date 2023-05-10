from django.db import models
#DataFlair Models
class Post(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'Describe your post here')
    def __str__(self):
        return self.name