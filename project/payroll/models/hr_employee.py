from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    # === USE COMPUTE ===
    wage_history_rec_count = fields.Integer(
        string="Wage History Record(s)",
        store=True,
        readonly=True,
        compute='_compute_wage_history_rec_count')

    payroll_ids = fields.One2many(
        comodel_name="payroll.wage.history",
        inverse_name="employee_id")

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        readonly=True)

    current_wage = fields.Monetary(
        string='Current Wage',
        currency_field='currency_id',
        readonly=True)

    # previous_wage = fields.Monetary(
    #     string='Previous Wage',
    #     currency_field='currency_id')

    # effective_date = fields.Date(
    #     string="Effective Date")

    # percentage = fields.Float(
    #     string="Percentage (%)",
    #     digits=(4, 2),
    #     readonly=True)

    @api.depends('payroll_ids')
    def _compute_wage_history_rec_count(self):
        for employee in self:
            employee.wage_history_rec_count = len(employee.payroll_ids)

    def action_open_history_wage(self):
        self.ensure_one()
        return {
            'name': "History Wage",
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'payroll.wage.history',
            'domain': [('employee_id', '=', self.id)]
        }
