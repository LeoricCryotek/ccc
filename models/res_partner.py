## models/res_partner.py
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    drink = fields.Char(string='Favorite Drink', help='User\'s preferred drink work friendly drink.')
    munis_vendor_id = fields.Integer(string='Vendor ID', help='Munis Vendor ID to identify vendors.')
    zoom_ext = fields.Char(string='Zoom Extension', help='Zoom extension number or ID for the user.')
