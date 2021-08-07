# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.dashboard import cache_source

@frappe.whitelist()
@cache_source
def get(chart_name = None, chart = None, no_cache = None, filters = None, from_date = None,
	to_date = None, timespan = None, time_interval = None, heatmap_year = None):
	data=frappe.db.get_list('covid_test',fields=['covid_name','covid_boy','covid_girl'])
	frappe.logger().debug(data)

	labels = []
	covid_boy = []
	covid_girl = []

	for covid in data:
		labels.append(covid['covid_name'])
		covid_boy.append(covid['covid_boy'])
		covid_girl.append(covid['covid_girl'])
	
	return {
		'labels': labels,
		'datasets': [
			{
				'name': 'boy',
				'values': covid_boy
				# 'colors':['green']
			},
			{
				'name': 'girl',
				'values': covid_girl
			},
		]
	}