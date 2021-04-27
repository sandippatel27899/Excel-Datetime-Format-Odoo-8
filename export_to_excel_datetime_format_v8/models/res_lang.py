from openerp import api, fields, models

class Lang(models.Model):
    _inherit = "res.lang"
    _description = "Languages"
    
    custom_date_format = fields.Char(string='Excel Date Format', default="DD-MM-YYYY",
                            help="This format of Date will be used in Excel export Report")
    custom_time_format = fields.Char(string='Excel Time Format',  default="HH:mm:SS", 
                            help="This format of Time will be used in Excel export Report ")
    