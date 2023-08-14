from odoo import models, fields, api

class Report(models.Model):
    _name = 'report'
    _description = 'Report'

    total_income = fields.Float(string='Tổng thu', compute='_compute_total_income') # , compute='_compute_total_income'
    total_expense = fields.Float(string='Tổng chi', compute='_compute_total_expense') # , compute='_compute_total_expense'
    balance = fields.Float(string='Quỹ còn lại', compute='_compute_balance') # , compute='_compute_balance'


    def _compute_total_income(self):
        incomes = self.env['income'].search([])
        income_list = incomes.mapped('payment')
        self.total_income = sum(income_list)

    def _compute_total_expense(self):
        expenses = self.env['expense'].search([])
        expense_list = expenses.mapped('expense_amount')
        self.total_expense = sum(expense_list)

    def _compute_balance(self):
        for r in self:
            r.balance = r.total_income - r.total_expense
