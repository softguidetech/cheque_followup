{

    'name': 'Cheque Followup',
    'version': '1.0.0',
    'summary': """
    Cheque followup as PDC/CDC/Direct Payment/Advance payment
    """,
    'category': 'Accounting',
    'author': 'SGT',
    'support': 'info@softguidetech.com',
    'website': 'https://softguidetech.com',
    'license': 'OPL-1',
    'price': 65,
    'currency': 'EUR',
    'data': [
        'security/ir.model.access.csv',
        # 'views/account_view.xml',
        'views/check_followup_view.xml',
        'views/payment_view.xml',
        'views/journal_view.xml',
        'wizard/change_bank_view.xml',
        'report/report.xml',
        'report/report_bank_payment_voucher.xml',
        'report/report_telegraphic_transfer_payment.xml',
        # 'data/data.xml',
        # 'reports/finance_report.xml'
    ],
    'depends': ['account','payment'],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}