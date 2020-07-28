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
        self.ensure_one()
        if self.id > 0:
            mail_followers_partner_ids = []
            items = self.env['mail.followers'].search([
                ('res_model', '=', 'purchase.order'),
                ('res_id', '=', self.id),
            ])
            if items:
                for item in items:
                    if item.partner_id:
                        mail_followers_partner_ids.append(item.partner_id.id)
            # mail followers extra
            items = self.env['purchase.order.mail.followers.extra'].search(
                [
                    ('partner_id', '=', self.partner_id.id)
                ]
            )
            for item in items:
                for partner_id_extra in item.partner_ids_extra:
                    if partner_id_extra.id not in mail_followers_partner_ids:
                        vals = {
                            'partner_id': int(partner_id_extra.id),
                            'res_model': 'purchase.order',
                            'res_id': self.id,
                            'subtype_ids': [(4, 1)],
                        }
                        self.env['mail.followers'].sudo().create(vals)
