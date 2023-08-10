from odoo import models, fields

class PositionRule(models.Model):
    _name = 'position.rule'

    name = fields.Char(string='Vị trí')
    money = fields.Float(string='Số tiền tối thiểu')