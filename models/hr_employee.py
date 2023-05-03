from odoo import models, fields, api
 # css/models/hr_employee.py

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    zoom_credit = fields.Boolean(string='Zoom Credit')
    drink = fields.Char(related='address_home_id.drink', string="Favorite Drink", readonly=False)
    employee_id = fields.Char(string='Employee ID')
    employee_badge_id = fields.Char(string='Badge #')
    physical_key = fields.Char(string='Physical Key')



