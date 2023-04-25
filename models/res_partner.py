from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    favorite_drink = fields.Char(string='Favorite Drink')
