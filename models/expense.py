from odoo import models, fields, api

class Expense(models.Model):
    _name = 'expense'
    _description = 'Expense'


    date = fields.Date(string='Ngày chi')
    item_ids = fields.One2many('item', 'expense_id', string='Vật phẩm')
    person = fields.Many2one('staff', string='Người chi')
    note = fields.Text(string='Ghi chú')
    expense_amount = fields.Float('Số tiền đã chi', compute='_compute_expense_amount', store=True)

    @api.depends('item_ids')
    def _compute_expense_amount(self):
        for r in self:
            r.expense_amount = 0
            for item_id in r.item_ids:
                r.expense_amount += item_id.total_cost









