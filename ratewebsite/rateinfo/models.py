from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_mail = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.customer_name}'

    def get_absolute_url(self):
        return reverse('rateinfo_customer_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('rateinfo_customer_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('rateinfo_customer_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['customer_name']


class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.CharField(unique=True, max_length=10)

    def __str__(self):
        return f'{self.year}'

    class Meta:
        ordering = ['year']


class Season(models.Model):
    season_id = models.AutoField(primary_key=True)
    season = models.CharField(unique=True, max_length=10)

    def __str__(self):
        return f'{self.season}'

    class Meta:
        ordering = ['season']


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_year_id = models.ForeignKey(Year, related_name='sections', on_delete=models.PROTECT)
    section_season_id = models.ForeignKey(Season, related_name='sections', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.section_year_id} - {self.section_season_id}'

    def get_absolute_url(self):
        return reverse('rateinfo_section_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('rateinfo_section_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('rateinfo_section_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['section_year_id', 'section_season_id']


class Holder(models.Model):
    holder_id = models.AutoField(primary_key=True)
    holder_name = models.CharField(max_length=45)
    holder_phone = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.holder_name} - {self.holder_phone}'

    def get_absolute_url(self):
        return reverse('rateinfo_holder_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('rateinfo_holder_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('rateinfo_holder_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['holder_name']


class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_place = models.CharField(max_length=225)
    place_street = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.place_place} -{self.place_street}'

    def get_absolute_url(self):
        return reverse('rateinfo_place_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('rateinfo_place_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('rateinfo_place_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['place_place', 'place_street']


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return f'{self.type_name}'

    def get_absolute_url(self):
        return reverse('rateinfo_type_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('rateinfo_type_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('rateinfo_type_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['type_name']


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=127)
    restaurant_place_id = models.ForeignKey(Place, related_name='restaurants', on_delete=models.PROTECT)
    restaurant_holder_id = models.ForeignKey(Holder, related_name='restaurants', on_delete=models.PROTECT)
    restaurant_type = models.ForeignKey(Type, related_name='restaurants', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.restaurant_name} - {self.restaurant_holder_id.holder_name}'

    def get_absolute_url(self):
        return reverse('rateinfo_restaurant_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('rateinfo_restaurant_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('rateinfo_restaurant_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['restaurant_name', 'restaurant_holder_id']


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_text = models.CharField(max_length=255)
    comment_level = models.IntegerField()
    comment_customer_id = models.ForeignKey(Customer, related_name='comments', on_delete=models.PROTECT)
    comment_restaurant_id = models.ForeignKey(Restaurant, related_name='comments', on_delete=models.PROTECT)
    comment_section_id = models.ForeignKey(Section, related_name='comments', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.comment_restaurant_id.restaurant_name} - {self.comment_text}'

    def get_absolute_url(self):
        return reverse('rateinfo_comment_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('rateinfo_comment_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('rateinfo_comment_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['comment_id']
