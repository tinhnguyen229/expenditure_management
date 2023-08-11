from odoo import models, fields, api

class Item(models.Model):
    _name = 'item'
    _description = 'Item'

    name = fields.Char(string='Tên vật phẩm')
    cost = fields.Float(string='Giá')
    quantity = fields.Integer(string='Số lượng')
    total_cost = fields.Float(string='Thành tiền', compute='_compute_total_expense', store=True)
    note = fields.Text(string='Ghi chú')
    date = fields.Date(string='Ngày mua', compute='_compute_date', store=True)
    expense_id = fields.Many2one('expense')

    # @api.onchange('cost', 'quantity')
    @api.depends('cost', 'quantity')
    def _compute_total_expense(self):
        for r in self:
            r.total_cost = r.cost * r.quantity

    @api.depends('expense_id.date')
    def _compute_date(self):
        for r in self:
            r.date = r.expense_id.date
