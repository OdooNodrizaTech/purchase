# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class PurchaseOrderMailFollowersExtra(models.Model):
    _name = 'purchase.order.mail.followers.extra'
    _description = 'Purchase Order Mail Followers Extra'
    
    partner_id = fields.Many2one(
        comodel_name='res.partner', 
        domain=[('supplier', '=', True)],
        string='Supplier',
    )
    partner_ids_extra = fields.Many2many(
        comodel_name='res.partner', 
        string='Extra followers in purchases'
    )                                                                        