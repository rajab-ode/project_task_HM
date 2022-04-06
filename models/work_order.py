from odoo import api, fields, models, _


class WorkOrder(models.Model):
    _name = 'booking.work_order'
    _description = 'Work Order'

    wo_number = fields.Char(
        string='WO Number',
        required=True,
        default=lambda self: _('New')
    )
    bo_references = fields.Many2one(
        comodel_name='sale.order',
        string='BO Reference',
        readonly=True
    )
    team = fields.Many2one(
        comodel_name='booking.service_team', 
        string='Team',
        required=True
    )
    team_leader = fields.Many2one(
        comodel_name='res.users', 
        string='Team Leader',
        required=True
    )
    team_members = fields.Many2one(
        comodel_name='res.users', 
        string='Team Members',
        required=True
    )
    planned_start = fields.Datetime(
        string='Planned Start',
        required=True
    )
    planned_end = fields.Datetime(
        string='Planned End',
        required=True
    )
    date_start = fields.Datetime(
        string='Booking Start'
    )
    date_end = fields.Datetime(
        string='Booking End',
    )
    state = fields.Selection(
        [('pending','Pending'),('in_progress','In Progress'),('done','Done'),('cancelled', 'Cancelled')],
        string='State',
        default='pending',
    )
    note = fields.Text(
        string='Note'
    )

    
