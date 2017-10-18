# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Driver(models.Model):
    CHOICES = (
        ('Возраст до 22 лет включительно, стаж до 3 лет включительно',
         'age<=22, exp<=3'),
        ('Возраст старше 22 лет, стаж до 3 лет включительно',
         'age>22, exp<=3'),
        ('Возраст до 22 лет включительно стаж свыше 3 лет',
         'age<=22, exp>3'),
        ('Возраст старше 22 лет, стаж свыше 3 лет',
         'age>22, exp>3')
    )
    
    title = models.CharField(verbose_name='Title', max_length=64, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CustomerType(models.Model):
    CHOICES = (
        ('Юридическое лицо', 'Legal Person'),
        ('Физическое лицо', 'Natural Person'),
    )
    
    title = models.CharField(verbose_name='Title', max_length=16, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'Customer Type'
        verbose_name_plural = 'Customer Types'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CarType(models.Model):
    title = models.CharField(verbose_name='Title', max_length=256, unique=True)
    is_trailer_allowed = models.BooleanField(verbose_name='Is trailer option allowed?', default=False)

    class Meta:
        verbose_name = 'Car Type'
        verbose_name_plural = 'Car Types'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Calculation(models.Model):
    customer_type = models.ForeignKey(CustomerType, verbose_name='Customer type')
    car_type = models.ForeignKey(CarType, verbose_name='Car type')
    is_car_with_trailer = models.BooleanField(verbose_name='Is car with trailer?', default=False)
    drivers = models.ManyToManyField(Driver, verbose_name='Drivers')

    # is_foreign_car
    # is_car_not_registered
    # engine_power
    # insurance_duration
    # car_expluatation_period
    # kbm_class
    # owner_registration_territory

    # coefs = models.JSONField()
    result_sum = models.DecimalField(verbose_name='Result sum', max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Calculation'
        verbose_name_plural = 'Calculations'

    @property
    def is_multidrive(self):
        return not self.drivers.all()
        
    def __str__(self):
        return '{self.id} {self.result_sum}'.format(self)

    def get_absolute_url(self):
        return reverse('calculation-detail', kwargs={'pk': self.pk})

