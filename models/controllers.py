from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal
# models/controllers.py

class CustomCustomerPortal(CustomerPortal):

    @http.route()
    def account(self, redirect=None, **post):
        response = super(CustomCustomerPortal, self).account(redirect=redirect, **post)
        if post and 'favorite_drink' in post:
            response.qcontext['favorite_drink'] = post['favorite_drink']
        return response
