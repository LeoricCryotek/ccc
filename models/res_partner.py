from odoo import models, fields, api
## models/res_partner.py

class ResPartner(models.Model):
    _inherit = 'res.partner'

    favorite_drink = fields.Char(string='Favorite Drink', default='')
    munis_vendor_id = fields.Integer(string='Vendor ID', help='Munis Vendor ID')
