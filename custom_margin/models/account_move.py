from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    show_margin = fields.Boolean(string='Enable Margin')
    cost = fields.Float(string='Cost', compute='_compute_cost', store=True)
    margin = fields.Float(string='Margin', compute='_compute_margin', store=True)

    @api.depends('product_id')
    def _compute_cost(self):
        for line in self:
            line.cost = line.product_id.standard_price or 0.0

    @api.depends('price_unit', 'cost', 'quantity')
    def _compute_margin(self):
        for line in self:
            line.margin = (line.price_unit - line.cost) * line.quantity
