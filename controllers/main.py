from cStringIO import StringIO
from pytz import timezone
import datetime
import re
import openerp
import xlwt 
from openerp import http
from openerp.tools.translate import _
from openerp.http import  request
from openerp.exceptions import Warning
from openerp.addons.web.controllers.main import ExcelExport

class InheritExcelExport(ExcelExport, http.Controller):
    @http.route('/web/export/xls', type='http', auth="user")
    def index(self, data, token):
        return super(InheritExcelExport,self).index(data,token)

    def utc_to_local(self,date_field, local_tz):
            utc = timezone('UTC')
            local_timezone = timezone(local_tz)
            date_field = utc.localize(date_field)
            finalDate = date_field.astimezone(local_timezone)
            finalDate = finalDate.replace(tzinfo=None)
            return finalDate

    def from_data(self, fields, rows):
        if len(rows) > 65535:
            raise Warning(_('There are too many rows (%s rows, limit: 65535) to export as Excel 97-2003 (.xls) format. Consider splitting the export.') % len(rows))

        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Sheet 1')

        lang_setting_obj = request.env['res.lang'].search([])
        if len(lang_setting_obj.ids) >1 :
            lang_setting_obj = lang_setting_obj[0]

        if lang_setting_obj:
            date_format = str(lang_setting_obj.custom_date_format)
            time_format = str(lang_setting_obj.custom_time_format)
            date_time_format = date_format + ' ' + time_format
        else:
            date_format = "YYYY-MM-DD"
            date_time_format = "YYYY-MM-DD HH:mm:SS"
        
        for i, fieldname in enumerate(fields):
            worksheet.write(0, i, fieldname)
            worksheet.col(i).width = 8000 # around 220 pixels

        base_style = xlwt.easyxf('align: wrap yes')
        date_style = xlwt.easyxf('align: wrap yes', num_format_str=date_format)
        datetime_style = xlwt.easyxf('align: wrap yes', num_format_str=date_time_format)

        timezone = request.env.user.tz 

        for row_index, row in enumerate(rows):
            for cell_index, cell_value in enumerate(row):
                cell_style = base_style
                if isinstance(cell_value, basestring):
                    cell_value = re.sub("\r", " ", cell_value)
                elif isinstance(cell_value, datetime.datetime):
                    if timezone:
                        cell_value = self.utc_to_local(cell_value, timezone)
                    cell_style = datetime_style
                elif isinstance(cell_value, datetime.date):
                    cell_style = date_style
                worksheet.write(row_index + 1, cell_index, cell_value, cell_style)

        fp = StringIO()
        workbook.save(fp)
        fp.seek(0)
        data = fp.read()
        fp.close()
        return data
