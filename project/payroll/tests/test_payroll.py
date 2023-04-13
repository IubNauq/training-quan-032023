from odoo.tests.common import TransactionCase


class TestPayroll(TransactionCase):
    def test_difference_raise(self):
        record_value = {'No': 0, 'contract_id': 1,
                        'previous_wage': 1250, 'current_wage': 2000,
                        'effective_date': '2023-04-01'}
        new_record_exc = self.env['payroll.wage.history'].create(record_value)
        new_record_exc._compute_difference()
        self.assertEqual(new_record_exc.difference,
                         750, "THE DIFFERENCE IS CALCULATED WRONG")
        print("TEST DIFFERENCE: SUCCESS")

    def test_raise(self):
        record_value = {'No': 0, 'contract_id': 1,
                        'previous_wage': 1250, 'current_wage': 2500,
                        'effective_date': '2023-04-01'}
        new_record_exc = self.env['payroll.wage.history'].create(record_value)
        new_record_exc._compute_difference()
        self.assertEqual(new_record_exc.percentage,
                         100, "THE RAISE(%) IS CALCULATED WRONG")
        print("TEST RAISE: SUCCESS")

    def test_wage_history_count(self):
        record_values = {'No': 0, 'contract_id': 1,
                         'previous_wage': 1250, 'current_wage': 2000,
                         'effective_date': '2023-04-01'}

        new_record_exc = self.env['payroll.wage.history'].create(record_values)

        new_record_exc_ = self.env['hr.employee'].search([('id', '=', 1)])
        new_record_exc_.action_count_wage_history_rec()

        self.assertEqual(new_record_exc_.wage_history_rec_count,
                         6, "THE WAGE HISTORY REC COUNT IS CALCULATED WRONG")
        print("TEST WAGE HISTORY REC COUNT: SUCCESS")
