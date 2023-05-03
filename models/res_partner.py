from odoo import models, fields, api
## models/res_partner.py

class ResPartner(models.Model):
    _inherit = 'res.partner'

    favorite_drink = fields.Char(string='Favorite Drink')
    munis_vendor_id = fields.Integer(string='Vendor ID', help='Munis Vendor ID')

class PortalMixin(models.AbstractModel):
    _inherit = 'portal.mixin'

    def details_form_validate(self, data):
        error, error_message = super(PortalMixin, self).details_form_validate(data)

        # Validate favorite_drink field
        favorite_drink = data.get('favorite_drink', '').strip()
        if not favorite_drink:
            error['favorite_drink'] = 'error'
            error_message.append(('favorite_drink', 'The Favorite Drink field is required.'))

        return error, error_message
