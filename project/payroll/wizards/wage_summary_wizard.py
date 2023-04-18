from odoo import fields, models, api


class WageSummaryWizard(models.TransientModel):
    _name = "wage.summary.wizard"
    _description = "Wage Summary Wizard"

    payroll_ids = fields.Many2many(
        comodel_name="payroll.wage.history")

    @api.model
    def default_get(self, fields_list):
        res = super(WageSummaryWizard, self).default_get(fields_list)

        # payrolls = self.env["payroll.wage.history"].browse(
        #     self.env.context.get("active_ids"))

        # === === ===
        # payrolls = self.env["payroll.wage.history"].search([], )

        # res['employee_ids'] = [(4, r.employee_id.id)
        #                        for r in payrolls]

        self.env.cr.execute("""
        SELECT id FROM payroll_wage_history
        WHERE id IN
        (
            SELECT max(id) FROM payroll_wage_history
            GROUP BY employee_id
        )
        """)
        payrolls = self.env.cr.fetchall()
        res['payroll_ids'] = [(4, r[0]) for r in payrolls]
        return res
