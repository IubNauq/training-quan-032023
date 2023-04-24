from odoo import fields, models, api


class HrContract(models.Model):
    _inherit = 'hr.contract'

    def write(self, vals):
        for contract in self:
            hr_responsible = contract.hr_responsible_id
            payroll = contract.wage
            effective_date = contract.date_start
            contract_id = contract.id
            # employee_id = contract.employee_id

            if 'hr_responsible_id' in vals:
                hr_responsible = vals['hr_responsible_id']
            if 'wage' in vals:
                payroll = vals['wage']
            if 'date_start' in vals:
                effective_date = vals['date_start']
            # if 'id' in vals:
            #     contract_id = vals['id']

            # Create new record on Payroll Wage History
            new_record = {'contract_id': contract_id,
                          'create_uid': hr_responsible,
                          'previous_wage': contract.wage,
                          'current_wage': payroll,
                          'currency_id': 2,
                          'effective_date': effective_date}

            self.env['payroll.wage.history'].create(new_record)

            # Update values on hr.employee

            # wage_history_rec_count = self.env[
            #     "payroll.wage.history"].search_count(
            #     [('employee_id', '=', contract.employee_id.id)])
            # new_record_ = {
            #     'current_wage': payroll
            # }
            # self.env['hr.employee'].browse(employee_id.id).write(new_record_)

        return super(HrContract, self).write(vals)
