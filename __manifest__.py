{
    'name': 'City Custom Configurations',
    'version': '1.0',
    'author': 'Danny Santiago',
    'category': 'Customizations',
    'license': 'LGPL-3',
    'summary': 'Customizations for employee forms',
    'depends': ['base', 'hr', 'portal', 'web', 'helpdesk', 'timesheet_grid'],
    'data': [
        'views/hr_employee_views.xml',
        'views/portal_layout.xml',
        'views/my_account_portal_view.xml',
        'views/res_partner_views.xml',
        'views/munis_res_partner.xml',
        'views/helpdesk_timesheet_update.xml',
    ],
    'installable': True,
    'application': False,
}
