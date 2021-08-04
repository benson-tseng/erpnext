frappe.provide('frappe.dashboards.chart_sources');

frappe.dashboards.chart_sources["covid_source"] = {
	method: "erpnext.healthcare.dashboard_chart_source.covid_source.covid_source.get",
	filters: [
		{
			fieldname: "company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company")
		}
	]
};