from odoo import models, fields, api
from datetime import datetime

class Income(models.Model):
    _name = 'income'
    _description = 'Income'

    staff_id = fields.Many2one('staff', string='Nhân viên')
    position_id = fields.Many2one(related='staff_id.position_id', string='Vị trí')
    min_money = fields.Float(related='position_id.money', string='Số tiền tối thiểu')

    payment = fields.Float(string='Số tiền đóng')
    payment_status = fields.Boolean(string='Đã đóng', compute='_compute_payment_status', store=True)
    debt = fields.Float(string='Số tiền còn thiếu')
    debt_status = fields.Boolean(string='Còn thiếu')
    date = fields.Date(string='Ngày đóng', default=datetime.today())

    @api.depends('payment')
    def _compute_payment_status(self):
        for r in self:
            r.payment_status = True if (r.payment!=0) else False

    @api.onchange('payment', 'staff_id')
    def _compute_debt(self):
        for r in self:
            # min_money = self.staff_id
            r.debt = r.min_money - r.payment
            r.debt_status = True if r.debt > 0 else False