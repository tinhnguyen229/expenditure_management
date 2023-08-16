from odoo import models, fields, api
from datetime import datetime, date, timedelta

class SendMail(models.Model):
    _name = 'send.mail'
    _description = 'Send Mail'


    # def filter_income_current_month(self):
    #     first_day_of_month = date.today().replace(day=1)
    #     last_day_of_month = date.today().replace(day=1, month=date.today().month % 12 + 1) - timedelta(days=1)
    #
    #     domain = [('date', '>=', first_day_of_month), ('date', '<=', last_day_of_month), ('debt_status', '=', False)]
    #     income_current_month = self.env['income'].search(domain)
    #     return income_current_month
    #
    # def filter_unpaid_staff(self):
    #     staff_id = self.env['staff'].search([])
    #     staff_id_paid = self.filter_income_current_month().staff_id
    #     return staff_id - staff_id_paid
    #
    # def send_mail_auto(self):
    #     template = self.env.ref('expenditure_management.my_email_template')
    #     staff_unpaid = self.filter_unpaid_staff()
    #     for r in staff_unpaid:
    #         template.send_mail(r.id, force_send=True)
    #
