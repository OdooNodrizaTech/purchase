# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def create(self, vals):
        return_create = super(PurchaseOrder, self).create(vals)
        return_create.action_mail_followers_override()                                          
        return return_create

    @api.multi
    def write(self, vals):
        return_create = super(PurchaseOrder, self).write(vals)
        self.action_mail_followers_override()                                          
        return return_create
                    
    @api.multi
    def action_mail_followers_override(self):
        if self.id > 0:
            mail_followers_partner_ids = []
            mail_followers_ids = self.env['mail.followers'].search([
                ('res_model', '=', 'purchase.order'),
                ('res_id', '=', self.id),
            ])
            if len(mail_followers_ids) > 0:
                for mail_followers_id in mail_followers_ids:
                    if mail_followers_id.partner_id.id > 0:
                        mail_followers_partner_ids.append(mail_followers_id.partner_id.id)
            
            purchase_order_mail_followers_extra_ids = self.env['purchase.order.mail.followers.extra'].search([('partner_id', '=', int(self.partner_id.id))])    
            for purchase_order_mail_followers_extra_id in purchase_order_mail_followers_extra_ids:
                for partner_id_extra in purchase_order_mail_followers_extra_id.partner_ids_extra:
                    if not partner_id_extra.id in mail_followers_partner_ids:   
                        mail_followers_vals = {
                            'partner_id': int(partner_id_extra.id),
                            'res_model': 'purchase.order',
                            'res_id': self.id,
                            'subtype_ids': [(4,1)],                                        
                        }
                        self.env['mail.followers'].sudo().create(mail_followers_vals)