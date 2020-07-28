# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields
import odoo.addons.decimal_precision as dp


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    price_unit = fields.Float(
        string='Unit Price',
        required=True,
        digits=dp.get_precision('Price Unit')
    )
