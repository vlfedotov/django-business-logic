# -*- coding: utf-8 -*-

from django.views import generic

from business_logic.models import Program, Context

from .models import *


class CalculationList(generic.ListView):
    model = Calculation


class CalculationDetail(generic.DetailView):
    model = Calculation

    def get_object(self, queryset=None):
        calculation = super(CalculationDetail, self).get_object(queryset)
        program = Program.objects.get(code='on_calculation_view')
        version = program.versions.order_by('id').last()
        version.execute(context=Context(debug=True, log=True), book=book)
        book.publisher.save()

        return calculation

