# -*- coding: utf-8 -*-


from datetime import date, datetime, timedelta
from openerp import models, fields, api, exceptions
from openerp.exceptions import Warning




class Sale(models.Model):
    _inherit = ['sale.order']


class SaleOrder(models.Model):
    _inherit = ['sale.order.line']
