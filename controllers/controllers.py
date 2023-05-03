from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomCustomerPortal(CustomerPortal):

    @http.route()
    def portal_save_changes(self, **kw):
        if 'favorite_drink' in kw:
            partner_id = request.env.user.partner_id
            partner_id.sudo().write({'favorite_drink': kw['favorite_drink']})
            kw.pop('favorite_drink')

        return super(CustomCustomerPortal, self).portal_save_changes(**kw)
