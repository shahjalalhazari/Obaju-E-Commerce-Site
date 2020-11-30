from django.db import models

# FOR WHOM MODEL
class ForWhom(models.Model):
    whom = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.whom
    class Meta:
        verbose_name_plural = 'For Whom List'


# CATEGORY MODEL
class Category(models.Model):
    for_whom = models.ForeignKey(ForWhom, on_delete=models.CASCADE, related_name='for_whom')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='CategoryImg', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} for {}".format(self.name, self.for_whom)
    class Meta:
        verbose_name_plural = 'Categories'


# SUB-CATEGORY MODEL
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='SubCategoryImg', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} from {}".format(self.name, self.category)
    class Meta:
        verbose_name_plural = 'Sub-Categories'


# PRODUCT MODEL# PRODUCT MODEL
class Product(models.Model):
    main_image = models.ImageField(upload_to="ProductImg")
    title = models.CharField(max_length=264)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='product', default="")
    description = models.TextField()
    price = models.FloatField()
    old_price = models.FloatField(blank=True, null=True)
    #EXTRA IMAGE FIELDS
    img_1 = models.ImageField(upload_to="ProductImg", blank=True, null=True)
    img_2 = models.ImageField(upload_to="ProductImg", blank=True, null=True)
    img_3 = models.ImageField(upload_to="ProductImg", blank=True, null=True)
    img_4 = models.ImageField(upload_to="ProductImg", blank=True, null=True)
    img_5 = models.ImageField(upload_to="ProductImg", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created']