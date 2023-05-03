from odoo import http
from odoo.addons.portal.controllers.portal import PortalDetails

class CustomPortalDetails(PortalDetails):

    @http.route()
    def submit_form(self, **kw):
        values = self._prepare_portal_layout_values()
        partner = values['partner']

        data = {
            'name': kw.get('name'),
            'email': kw.get('email'),
            'mobile': kw.get('mobile'),
            'phone': kw.get('phone'),
            'favorite_drink': kw.get('favorite_drink'),
        }

        error, error_message = partner.details_form_validate(data)
        if not error:
            partner.sudo().write(data)
            return http.redirect_with_hash(self._get_portal_redirect())

        values.update({
            'error': error,
            'error_message': error_message,
            'data': data,
        })

        return request.render("portal.portal_my_details", values)
