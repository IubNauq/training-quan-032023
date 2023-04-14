from odoo import fields, models, api


class HrContract(models.Model):
    _inherit = 'hr.contract'

    def write(self, vals):
        for r in self:
            hr_responsible = r.hr_responsible_id
            payroll = r.wage
            effective_date = r.date_start
            contract_id = r.id
            employee_id = r.employee_id

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
                          'previous_wage': r.wage,
                          'current_wage': payroll,
                          'currency_id': 2,
                          'effective_date': effective_date}

            new_record_exc = self.env['payroll.wage.history'].create(
                new_record)

            # Update values on hr.employee
            wage_history_rec_count = self.env[
                "payroll.wage.history"].search_count(
                [('employee_id', '=', r.employee_id.id)])
            new_record_ = {
                'previous_wage': r.wage,
                'current_wage': payroll,
                'effective_date': effective_date,
                'wage_history_rec_count': wage_history_rec_count,
                'percentage': new_record_exc.percentage
            }

            self.env['hr.employee'].browse(employee_id.id).write(new_record_)

        return super(HrContract, self).write(vals)
