# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import api, models, fields

import logging
_logger = logging.getLogger(__name__)

class PurchaseOrderMailFollowersExtra(models.Model):
    _name = 'purchase_order_mail_followers_extra'
    
    partner_id = fields.Many2one(
        comodel_name='res.partner', 
        domain=[('supplier', '=', True)],
        string='Proveedore',
    )
    partner_ids_extra = fields.Many2many(
        comodel_name='res.partner', 
        string='Seguidores adicionales compras'
    )                                                                        