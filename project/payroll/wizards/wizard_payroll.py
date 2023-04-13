from odoo import fields, models, api
import io
import xlsxwriter


class WageSummaryWizard(models.TransientModel):
    _name = "wage.summary.wizard"
    # _name = "report.wizards.wizardxlsx"
    # _inherit = 'report.report_xlsx.abstract'
    _description = "Wage Summary Wizard"

    employee_ids = fields.Many2many(comodel_name="hr.employee")

    currency_id = fields.Many2one('res.currency', string='Currency')

    previous_wage = fields.Float(digits=(16, 2),
                                 string='Previous Wage')
    current_wage = fields.Float(digits=(16, 2),
                                string='Current Wage')

    percentage = fields.Float(string="Percentage (%)", digits=(
        4, 2), readonly=True)

    effective_date = fields.Date(string="Effective Date")

    @api.model
    def default_get(self, fields_list):
        res = super(WageSummaryWizard, self).default_get(fields_list)

        # payrolls = self.env["payroll.wage.history"].browse(
        #     self.env.context.get("active_ids"))

        payrolls = self.env["payroll.wage.history"].search([])

        res['employee_ids'] = [(4, r.employee_id.id)
                               for r in payrolls]
        return res
