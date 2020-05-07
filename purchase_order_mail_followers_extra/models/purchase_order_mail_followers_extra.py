# -*- coding: utf-8 -*-
from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)

class PurchaseOrderMailFollowersExtra(models.Model):
    _name = 'purchase.order.mail.followers.extra'
    _description = 'Purchase Order Mail Followers Extra'
    
    partner_id = fields.Many2one(
        comodel_name='res.partner', 
        domain=[('supplier', '=', True)],
        string='Proveedore',
    )
    partner_ids_extra = fields.Many2many(
        comodel_name='res.partner', 
        string='Seguidores adicionales compras'
    )                                                                        