from odoo import fields, models, api


class MyContract(models.Model):
    _inherit = 'hr.contract'

    def write(self, vals):
        self.ensure_one()
        hr_responsible = self.hr_responsible_id
        payroll = self.wage
        effective_date = self.date_start
        contract_id = self.id
        employee_id = self.employee_id

        if 'hr_responsible_id' in vals:
            hr_responsible = vals['hr_responsible_id']
        if 'wage' in vals:
            payroll = vals['wage']
        if 'date_start' in vals:
            effective_date = vals['date_start']
        if 'id' in vals:
            contract_id = vals['id']

        # Create new record on Payroll Wage History
        new_record = {'contract_id': contract_id,
                      'create_uid': hr_responsible,
                      'previous_wage': self.wage,
                      'current_wage': payroll,
                      'currency_id': 2,
                      'effective_date': effective_date}

        new_record_exc = self.env['payroll.wage.history'].create(new_record)

        # Update values on hr.employee
        wage_history_rec_count = self.env["payroll.wage.history"].search_count(
            [('employee_id', '=', self.employee_id.id)])
        new_record_ = {
            'previous_wage': self.wage,
            'current_wage': payroll,
            'effective_date': effective_date,
            'wage_history_rec_count': wage_history_rec_count,
            'percentage': new_record_exc.percentage
        }

        self.env['hr.employee'].browse(employee_id.id).write(new_record_)

        return super(MyContract, self).write(vals)
