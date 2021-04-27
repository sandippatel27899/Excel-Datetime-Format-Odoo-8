# -*- coding: utf-8 -*-
{
    'name': "Excel Report Date/Time Format",

    'summary': """
        Functionality to Change Format of Date and Time 
        And Values as per Timezone in Excel Export Report
        """,

    'description': """
        Timezone of Datetime values in Excel Exporting reports (Base)
        is based on loggedin user's Timezone

        To change the Format of date and time in Excel Export Report
        Visit Odoo language settings 

        GoTo : Settings >> Translations >> Languages (Debug Mode)
        Checkout Legends for supported Custom Date and Time Formats 
    
       Excel_Date_Format and Excel_Time_Format  are for XLS reports
    """,

    'author': "Sandip Patel",
    'website': "http://www.sandippatel.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        'views/res_lang.xml'
    ],
    'images': ['static/description/date.jpeg'],

    # only loaded in demonstration mode
    'demo': [],
}