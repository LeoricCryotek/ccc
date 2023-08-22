from odoo import models, fields, api
 # css/models/hr_employee.py

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    zoom_credit = fields.Boolean(string='Zoom Credit')
    partner_drink = fields.Char(related='user_id.partner_id.drink', string='Drink Preference', readonly=True)
    partner_zoom_ext = fields.Char(related='user_id.partner_id.zoom_ext', string='Zoom Extension', readonly=True)
    employee_id = fields.Char(string='Employee ID')
    employee_badge_id = fields.Char(string='Badge #')
    physical_key = fields.Char(string='Physical Key')



