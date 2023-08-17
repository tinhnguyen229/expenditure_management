from odoo import models, fields, api
import re
from datetime import datetime, date, timedelta

class Staff(models.Model):
    _name = 'staff'
    _description = 'Staff Model'

    name = fields.Char(string='Họ tên', required=True)
    date_of_birth = fields.Date(string='Ngày sinh')
    team = fields.Selection([('ceo', 'CEO'), ('design', 'Design'),
                             ('front_end', 'Front-end'), ('odoo1', 'Odoo 1'),
                             ('odoo2', 'Odoo 2')], string='Team', defaul='front_end')
    # position = fields.Selection([('ceo', 'CEO'), ('leader', 'Leader'),
    #                          ('staff', 'Staff'), ('intern', 'Intern')],
    #                         string='Vị trí', defaul='staff')
    phone_num = fields.Char(string='Số ĐT')
    email = fields.Char(string='Email', store=True)
    position_id = fields.Many2one('position.rule', string='Vị trí công việc')

    @api.onchange('name')
    def _get_email(self):
        for record in self:
            name_list = Staff.no_accent_vietnamese(str(record.name).lower()).split()
            last_name = name_list[len(name_list) - 1]

            first_name = ''
            for i in range(len(name_list) - 1):
                first_name += name_list[i][0]
            print(f'{last_name + first_name}@batgroup.vn')
            record.email = f'{last_name + first_name}@batgroup.vn'


    @api.model
    def no_accent_vietnamese(s):
        s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
        s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
        s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
        s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
        s = re.sub(r'[ìíịỉĩ]', 'i', s)
        s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
        s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
        s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
        s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
        s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
        s = re.sub(r'[Đ]', 'D', s)
        s = re.sub(r'[đ]', 'd', s)
        return s

    @api.model
    def send_mail_auto(self):
        first_day_of_month = date.today().replace(day=1)
        last_day_of_month = date.today().replace(day=1, month=date.today().month % 12 + 1) - timedelta(days=1)
        # domain search
        domain = [('date', '>=', first_day_of_month), ('date', '<=', last_day_of_month), ('debt_status', '=', False)]
        # filter income in a month
        income_current_month = self.env['income'].search(domain)

        # get all staffs
        staff_id = self.env['staff'].search([])
        # get staffs paid in a month
        staff_id_paid = income_current_month.staff_id
        # get staffs unpaid in a month
        staff_unpaid = staff_id - staff_id_paid

        # refer to mail_template_tinhnn.xml file with file's ID: 'send_mail_template_tttt'
        template = self.env.ref('expenditure_management.send_mail_template_tttt')

        # for loop to send mail. Call send_mail_auto() method in send_mail_template.xml file
        for r in staff_unpaid:
            template.send_mail(r.id)
