from odoo import fields, models

class EstateProperty(models.Model):
    _name = "test_model"
    _description = "Test Model"

    name = fields.Char()