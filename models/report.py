from odoo import models, fields, api

class IncomeReport(models.Model):
    _name = 'income.report'
    _inherit = 'income'
    _description = 'Income Report'

    total_income = fields.Float(string='Tổng thu')




class ExpenseReport(models.Model):
    _name = 'expense.report'
    _inherit = 'expense'
    _description = 'Expense Report'



