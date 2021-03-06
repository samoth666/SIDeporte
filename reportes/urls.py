from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import *

urlpatterns =  patterns ('',
	url(r'^graficos$', MenuReportesGraficos.as_view(), name='menu_rep_graficos'),
	url(r'^graficos/ejemplo$', ReportesGraficosBarras.as_view(), name='grafica_barras'),
	url(r'^tablas$', MenuReportesTablas.as_view(), name='menu_rep_tablas'),
	url(r'^tablas/ejemplo$', ReportesTablas.as_view(), name='grafica_tablas'),
)