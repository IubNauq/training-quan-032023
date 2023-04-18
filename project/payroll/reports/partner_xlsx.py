from odoo import models
from datetime import datetime, timedelta


class PartnerXlsx(models.AbstractModel):
    _name = 'report.payroll.payroll_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet("Report")

        # === 1. STYLE ===
        bold_big_center = workbook.add_format(
            {"bold": True, "font_size": 20, 'font_name': 'Times New Roman',
             'align': 'center', 'valign': 'vcenter'})
        bold_normal_bg = workbook.add_format(
            {"bold": True, "font_size": 14, 'font_name': 'Times New Roman',
             'bg_color': '#D9D9D9', 'valign': 'vcenter',
             'border_color': 'black', 'border': 1})

        font = workbook.add_format({'font_name': 'Times New Roman'})

        font_border = workbook.add_format({'font_name': 'Times New Roman',
                                           'border_color': 'black',
                                           'border': 1,
                                           'align': 'center',
                                           'valign': 'vcenter'})
        font_border_num = workbook.add_format({'font_name': 'Times New Roman',
                                               'border_color': 'black',
                                               'border': 1,
                                               'align': 'center',
                                               'valign': 'vcenter',
                                               'num_format': '#,##0'})
        # CONSTANT
        ROW_HEIGHT = 20
        COLUMN_WIDTH = 20

        sheet.set_row(0, ROW_HEIGHT+5)
        sheet.set_row(3, ROW_HEIGHT+20)

        sheet.set_column('A:A', COLUMN_WIDTH-10)
        sheet.set_column('B:B', COLUMN_WIDTH+10)
        sheet.set_column('C:C', COLUMN_WIDTH+10)
        sheet.set_column('D:D', COLUMN_WIDTH+10)
        sheet.set_column('E:E', COLUMN_WIDTH)
        sheet.set_column('F:F', COLUMN_WIDTH+10)

        sheet.merge_range('A1:F1', 'A1F1')

        date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})
        sheet.set_column(0, 0, 12, date_format)

        # === 2. WRITE ===
        current_year = datetime.today().year
        current_month = datetime.today().month

        # TITLE
        title = f'BÁO CÁO LỊCH SỬ THAY ĐỔI LƯƠNG NHÂN VIÊN NĂM {current_month}/{current_year}'
        sheet.write('A1F1', title, bold_big_center)

        # SUBTITLE
        FIRST_DAY = '01/'
        LAST_DAY = '31/'
        subtitle = [
            ('B2', 'Từ ngày'),
            ('C2', f'{FIRST_DAY}{current_month}/{current_year}'),
            ('D2', 'Đến ngày'),
            ('E2', f'{LAST_DAY}{current_month}/{current_year}'),
            ('A4', 'STT\nNo.')
        ]
        for coord, value in subtitle:
            sheet.write(coord, value, font)

        # COLUMN TITLE
        col_title = [
            ('A4', 'STT\nNo.', bold_normal_bg),
            ('B4', 'NHÂN VIÊN\nEMPLOYEE NAME', bold_normal_bg),
            ('C4', 'MỨC LƯƠNG HIỆN TẠI\nCURRENT WAGE', bold_normal_bg),
            ('D4', 'MỨC LƯƠNG TRƯỚC ĐÓ\nPREVIOUS WAGE', bold_normal_bg),
            ('E4', 'MỨC TĂNG(%)\nRAISE(%)', bold_normal_bg),
            ('F4', 'ÁP DỤNG TỪ THÁNG\nEFFECTIVE MONTHS', bold_normal_bg)
        ]
        for coord, value, style in col_title:
            sheet.write(coord, value, style)

        # Loop through the list of partners and write data to the sheet for
        # partners with effective date in the current month
        row_index = 0
        for i, obj in enumerate(partners):
            if obj.effective_date.month == current_month:
                sheet.set_row(row_index+4, ROW_HEIGHT)
                sheet.write(row_index+4, 0, row_index+1, font_border)
                sheet.write(row_index+4, 1, obj.employee_id.name, font_border)
                sheet.write(row_index+4, 2, obj.current_wage, font_border_num)
                sheet.write(row_index+4, 3, obj.previous_wage, font_border_num)
                sheet.write(row_index+4, 4, obj.percentage, font_border)
                sheet.write(
                    row_index+4, 5, f"{obj.effective_date.month}/{obj.effective_date.year}", font_border)
                row_index += 1

        sheet.set_row(row_index+6, ROW_HEIGHT+10)
        sheet.write(row_index+6, 1,
                    "Người lập bảng\n(Ký, ghi rõ họ tên)", font)
        sheet.write(row_index+6, 5,
                    "Giám đốc nhân sự\n(Ký, ghi rõ họ tên)", font)
