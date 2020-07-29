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
        for item in self:
            if item.id > 0:
                partner_ids = []
                followers_ids = self.env['mail.followers'].search([
                    ('res_model', '=', 'purchase.order'),
                    ('res_id', '=', item.id),
                ])
                if followers_ids:
                    for followers_id in followers_ids:
                        if followers_id.partner_id:
                            partner_ids.append(followers_id.partner_id.id)
                # mail followers extra
                extra_ids = self.env['purchase.order.mail.followers.extra'].search(
                    [
                        ('partner_id', '=', item.partner_id.id)
                    ]
                )
                for extra_id in extra_ids:
                    for partner_id_extra in extra_id.partner_ids_extra:
                        if partner_id_extra.id not in partner_ids:
                            vals = {
                                'partner_id': int(partner_id_extra.id),
                                'res_model': 'purchase.order',
                                'res_id': item.id,
                                'subtype_ids': [(4, 1)],
                            }
                            self.env['mail.followers'].sudo().create(vals)
