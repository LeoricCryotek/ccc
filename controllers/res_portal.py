## controllers/res_portal.py
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class PersonalDetails(http.Controller):

    @http.route(['/my/portal_personal_details'], type='http', auth="user", website=True)
    def personal_details(self, **kwargs):
        show_notification = False

        # Check if we set the 'show_notification' flag in the session
        if request.session.get('show_notification'):
            show_notification = True
            # Clear the flag so the notification doesn't show on subsequent page loads
            request.session['show_notification'] = False

        partner = request.env.user.partner_id
        return request.render('ccc.portal_personal_details', {'show_notification': show_notification, 'partner': partner})

    @http.route('/my/personal/save', type='http', auth='user', methods=['POST'], csrf=False)  # Updated URL endpoint
    # Consider enabling CSRF protection
    def personal_update(self, **post):
        show_notification = False  # Define this at the beginning of the method for clarity
        partner = request.env.user.partner_id

        try:
            # 1. Get the values from the form
            drink = post.get('res.partner.drink')
            zoom_ext = post.get('res.partner.zoom_ext')

            # 2. Log the received values to the Odoo logs
            _logger.info(f"POST data received: {post}")
            _logger.info(f"Received favorite drink: {drink}")
            _logger.info(f"Received Zoom extension: {zoom_ext}")

            # 3. Validate and update
            if drink or zoom_ext:
                partner.write({
                    'drink': drink if drink else partner.drink,  # If no new drink value, retain the old one
                    'zoom_ext': int(zoom_ext) if zoom_ext and zoom_ext.isdigit() else partner.zoom_ext
                    # If no new zoom_ext or not a number, retain the old value
                })

            # Set the notification flag
            show_notification = True
            request.session['show_notification'] = True

        except Exception as e:
            # Handle exceptions and log them
            _logger.error(f"An error occurred while updating personal information: {e}")
            # You can set another session variable to show error notifications if needed

        # Redirect user back to the personal form page
        return request.redirect(
            '/my/portal_personal_details?show_notification=%s&partner=%s' % (show_notification, partner.id))


