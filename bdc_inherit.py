# -*- coding: utf-8 -*-


from datetime import date, datetime, timedelta
from openerp import models, fields, api, exceptions
from openerp.exceptions import Warning




class Sale(models.Model):
    _inherit = ['sale.order']


class SaleOrder(models.Model):
    _inherit = ['sale.order.line']



class ParticularReport(models.AbstractModel):
    _name = 'report.charts.report_sale_order_inherit'
    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('charts.report_sale_order_inherit')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self,
        }
        return report_obj.render('charts.report_sale_order_inherit', docargs)


