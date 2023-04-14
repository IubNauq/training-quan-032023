from odoo import models
from datetime import datetime, timedelta


class PartnerXlsx(models.AbstractModel):
    _name = 'report.payroll.payroll_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet("Report")

        # STYLE
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
        sheet.set_row(0, 25)
        sheet.set_row(3, 40)

        sheet.set_column('A:A', 10)
        sheet.set_column('B:B', 30)
        sheet.set_column('C:C', 30)
        sheet.set_column('D:D', 30)
        sheet.set_column('E:E', 20)
        sheet.set_column('F:F', 30)

        sheet.merge_range('A1:F1', 'A1F1')

        date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})
        sheet.set_column(0, 0, 12, date_format)

        # WRITE
        current_year = datetime.today().year
        current_month = datetime.today().month

        title = 'BÁO CÁO LỊCH SỬ THAY ĐỔI LƯƠNG NHÂN VIÊN NĂM ' + \
            str(current_month)+"/"+str(current_year)

        sheet.write(
            'A1F1', title, bold_big_center)
        sheet.write('B2', "Từ ngày", font)
        sheet.write('C2', '01/'+str(current_month) +
                    '/'+str(current_year), font)
        sheet.write('D2', "Đến ngày", font)
        sheet.write('E2', "31/" +
                    str(current_month)+"/"+str(current_year), font)

        sheet.write('A4', 'STT\nNo.', bold_normal_bg)
        sheet.write('B4', 'NHÂN VIÊN\nEMPLOYEE NAME', bold_normal_bg)
        sheet.write('C4', 'MỨC LƯƠNG HIỆN TẠI\nCURRENT WAGE', bold_normal_bg)
        sheet.write('D4', 'MỨC LƯƠNG TRƯỚC ĐÓ\nPREVIOUS WAGE', bold_normal_bg)
        sheet.write('E4', 'MỨC TĂNG(%)\nRAISE(%)', bold_normal_bg)
        sheet.write('F4', 'ÁP DỤNG TỪ THÁNG\nEFFECTIVE MONTHS', bold_normal_bg)

        index = 0
        for i, obj in enumerate(partners):
            if (obj.effective_date.month == current_month):
                sheet.set_row(index+4, 20)
                sheet.write(index+4, 0, index+1, font_border)
                sheet.write(index+4, 1, obj.employee_id.name, font_border)
                sheet.write(index+4, 2, obj.current_wage, font_border_num)
                sheet.write(index+4, 3, obj.previous_wage, font_border_num)
                sheet.write(index+4, 4, obj.percentage, font_border)
                sheet.write(index+4, 5, str(obj.effective_date.month) +
                            "/" + str(obj.effective_date.year), font_border)
                index += 1

        sheet.set_row(index+6, 30)
        sheet.write(index+6, 1, "Người lập bảng\n(Ký, ghi rõ họ tên)", font)
        sheet.write(index+6, 5, "Giám đốc nhân sự\n(Ký, ghi rõ họ tên)", font)
