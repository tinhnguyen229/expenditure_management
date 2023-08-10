from odoo import models, fields, api
import re
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
    email = fields.Char(string='Email', compute='_get_email', store=True)
    position_id = fields.Many2one('position.rule', string='Vị trí công việc')

    @api.depends('name')
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