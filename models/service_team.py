from odoo import api, fields, models


class ServiceTeam(models.Model):
    _name = 'booking.service_team'
    _description = 'Service Team'

    name = fields.Char(string='Name', required=True)
    team_leader = fields.Many2one(
        comodel_name='res.users', 
        string='Team Leader',
        required=True)

    team_members = fields.Many2many(
        comodel_name='res.users', 
        string='Team Members',
        required=True)
    



