from odoo import fields, models, api
from datetime import datetime, timedelta

# last_year = datetime.today()-timedelta(days=365)


class PayrollWageHistory(models.Model):
    _name = "payroll.wage.history"
    _description = "Payroll Wage History"

    name = fields.Char(
        string="Revision No.",
        readonly=True)

    employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Employee",
        index=True,
        related='contract_id.employee_id',
        store=True)

    contract_id = fields.Many2one(
        comodel_name="hr.contract",
        string="Contract",
        ondelete="restrict",
        index=True)

    department_id = fields.Many2one(
        comodel_name="hr.department",
        string="Department",
        ondelete="restrict",
        index=True,
        related='contract_id.department_id',
        store=True)

    job_id = fields.Many2one(
        comodel_name="hr.job",
        string="Job Title",
        ondelete="restrict",
        index=True,
        related='contract_id.job_id',
        store=True)

    # create_uid = fields.Many2one(comodel_name="res.users",
    #                              string="Responsible", index=True)

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency')

    previous_wage = fields.Float(
        digits=(16, 2),
        string='Previous Wage')

    current_wage = fields.Float(
        digits=(16, 2),
        string='Current Wage')

    difference = fields.Float(
        digits=(16, 2),
        string='Difference',
        store=True,
        compute="_compute_difference")

    percentage = fields.Float(
        string="Percentage (%)",
        digits=(4, 2),
        store=True,
        readonly=True,
        compute="_compute_difference")

    effective_date = fields.Date(
        string="Effective Date")

    index = fields.Integer(
        string="No.",
        default=0,
        readonly=True)

    @api.depends("previous_wage", "current_wage")
    def _compute_difference(self):
        for r in self:
            r.difference = r.current_wage-r.previous_wage
            if not r.previous_wage:
                r.percentage = 0
            else:
                r.percentage = 100.0 * \
                    (r.current_wage-r.previous_wage)/r.previous_wage

    @api.model_create_multi
    def create(self, values):
        wage_history_env = self.env["payroll.wage.history"]

        for value in values:
            contract_id = wage_history_env.search(
                [('contract_id', '=', value['contract_id'])],
                order='id desc', limit=1)
            if contract_id:
                value['index'] = contract_id.index+1
            else:
                value['index'] = 0
            value['name'] = str(value['contract_id']) + "-" +\
                str(value['index'])+"-"+str(value['effective_date'])[:4]

        return super(PayrollWageHistory, self).create(values)

    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self.env.context.get("highest_raise_in_12_month"):
            self.env.cr.execute("""
            SELECT * FROM payroll_wage_history
            WHERE difference = (
                SELECT difference FROM payroll_wage_history
                WHERE effective_date>%s
                ORDER BY difference DESC LIMIT 1
            )
            """, [datetime.today()-timedelta(days=365)])

            results = self.env.cr.fetchall()
            record_ids = [result[0] for result in results]
            args.append(('id', 'in', record_ids))
            # return self.browse(record_ids)

        elif self.env.context.get("no_raise_in_12_month"):
            self.env.cr.execute("""
            SELECT * FROM payroll_wage_history t1
            WHERE effective_date<%s
            AND id IN
            (
                SELECT max(id) from payroll_wage_history
                GROUP BY contract_id
            )
            """, [datetime.today()-timedelta(days=365)])

            results = self.env.cr.fetchall()
            record_ids = [result[0] for result in results]
            args.append(('id', 'in', record_ids))
            # return self.browse(record_ids)

        return super(PayrollWageHistory, self).search(args, offset=offset,
                                                      limit=limit, order=order,
                                                      count=count)
