# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields
import odoo.addons.decimal_precision as dp

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    price_unit = fields.Float(
        string='Unit Price',
        required=True,
        digits=dp.get_precision('Price Unit')
    )