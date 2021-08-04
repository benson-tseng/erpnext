# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.dashboard import cache_source

@frappe.whitelist()
@cache_source
def get(chart_name = None, chart = None, no_cache = None, filters = None, from_date = None,
	to_date = None, timespan = None, time_interval = None, heatmap_year = None):
	

	return {
		'labels': ["北","中","南","東"],
		'datasets': [
			{
				'name': '男',
				'values': [113,152,171,121]
			},
			{
				'name': '女',
				'values': [199,153,109,129]
			},
		],
		'type': 'bar'
	}