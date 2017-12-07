# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PartnerActivities(models.Model):
    _name = 'partner.activities'
    _description = 'SII Economical Activities'

    @api.multi
    def name_get(self):
        res = []
        for r in self:
            res.append((r.id, (r.code and '[' + r.code + '] ' + r.name or '') ))
        return res

    code = fields.Char(
            string='Activity Code',
            required=True,
            translate=True,
        )
    parent_id = fields.Many2one(
            'partner.activities',
            string='Parent Activity',
            ondelete='cascade',
        )
    name = fields.Char(
            string='Nombre Completo',
            required=True,
            translate=True,
        )
    vat_affected = fields.Selection(
            (
                ('SI', 'Si'),
                ('NO', 'No'),
                ('ND', 'ND'),
            ),
            string='VAT Affected',
            required=True,
            translate=True,
            default='SI',
        )
    tax_category = fields.Selection(
            (
                ('1', '1'),
                ('2', '2'),
                ('ND', 'ND'),
            ),
            string='TAX Category',
            required=True,
            translate=True,
            default='1',
        )
    internet_available = fields.Boolean(
            string='Available at Internet',
            default=True,
        )
    active = fields.Boolean(
            string='Active',
            help="Allows you to hide the activity without removing it.",
            default=True,
        )
    partner_ids = fields.Many2many(
            'res.partner',
            id1='activities_id',
            id2='partner_id',
            string='Partners',
        )
    journal_ids = fields.Many2many(
            'account.journal',
            id1='activities_id',
            id2='journal_id',
            string='Journals',
        )
