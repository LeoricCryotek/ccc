from odoo import models, fields, api
## models/res_partner.py

class ResPartner(models.Model):
    _inherit = 'res.partner'

    drink = fields.Char(string='Favorite Drink')
    munis_vendor_id = fields.Integer(string='Vendor ID', help='Munis Vendor ID')
    city = fields.Char(string='City', required=False)
    country_id = fields.Many2one('res.country', string='Country', required=False)

    @api.model
    def create(self, vals):
        if 'city' in vals and not vals['city']:
            vals.pop('city')
        if 'country_id' in vals and not vals['country_id']:
            vals.pop('country_id')
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if 'city' in vals and not vals['city']:
            vals.pop('city')
        if 'country_id' in vals and not vals['country_id']:
            vals.pop('country_id')
        return super(ResPartner, self).write(vals)
