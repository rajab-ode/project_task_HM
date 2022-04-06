from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class BookingOrder(models.Model):
    
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(string='Is Booking Order')
    team = fields.Many2one(
        comodel_name='booking.service_team',
        string='Team'
    )
    team_leader = fields.Many2one(
        comodel_name='res.users', 
        string='Team Leader', 
        required=True
    )
    team_members = fields.Many2many(
        comodel_name='res.users', 
        string='Team Members', 
        required=True
    )
    booking_start = fields.Datetime(
        string='Booking Start'
    )
    booking_end = fields.Datetime(
        string='Booking End'
    )

    @api.onchange('team')
    def onchange_team(self):
        search = self.env['booking.service_team'].search([('id','=', self.team.id)])
        team_members = []
        for team in search:
            team_members.extend(members.id for members in team.team_members)
            self.team_leader = team.team_leader.id
            self.team_members = team_members
    
    def action_check(self):
        for check in self:
            wo = self.env['booking.work_order'].search(
                ['|','|','|',
                    ('team_leader', 'in', [wo.id for wo in self.team_members]),
                    ('team_members', 'in', [self.team_leader.id]),
                    ('team_leader', '=', self.team_leader.id),
                    ('team_members', '=', [wo.id for wo in self.team_members]),
                    ('state', '=', 'cancelled'),
                    ('planned_start','<=', self.booking_end),
                    ('planned_end','>=', self.booking_start),
                    
                ], limit=1

            )
            if wo:
                raise ValidationError('Team already has work order during that period on SOXX')
            else:
                raise ValidationError('Team is available for booking')

    def action_check(self):
        res = super(BookingOrder, self).action_confirm()
        for check in self:
            wo = self.env['booking.work_order'].search(
                ['|','|','|',
                    ('team_leader', 'in', [wo.id for wo in self.team_members]),
                    ('team_members', 'in', [self.team_leader.id]),
                    ('team_leader', '=', self.team_leader.id),
                    ('team_members', '=', [wo.id for wo in self.team_members]),
                    ('state', '=', 'cancelled'),
                    ('planned_start','<=', self.booking_end),
                    ('planned_end','>=', self.booking_start),
                    
                ], limit=1

            )
            if wo:
                raise ValidationError('Team is not available during this period, already booked on SOXX, Please book on another date.')
            check.action_create_work_order()
        return res

    def action_create_work_order(self):
        wo = self.env['booking.work_order']
        for search in self:
            wo.create([{
                'bo_references': search.id,
                'team': search.team.id,
                'team_leader': search.team_leader.id,
                'team_members': search.team_members.ids,
                'planned_start': search.planned_start,
                'planned_end': search.planned_end,
            }])

    
