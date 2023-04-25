from odoo import models, fields
 # css/models/hr_employee.py

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    zoom_credit = fields.Boolean(string='Zoom Credit')
    favorite_drink = fields.Char(string='Favorite Drink')
    employee_id = fields.Char(string='Employee ID')
    employee_badge_id = fields.Char(string='Badge #')
    physical_key = fields.Char(string='Physical Key')

# Extend the ResPartner model
class ResPartner(models.Model):
    _inherit = 'res.partner'

    favorite_drink = fields.Char(string='Favorite Drink')
