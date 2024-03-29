from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests


class InfoBaza(models.Model):
    _inherit = 'crm.lead'

    avtovin = fields.Char(string='AutoVIN', index=True)

    @api.constrains('avtovin')
    def _check_info_baza(self):
        for record in self:
            if record.avtovin:

    def action_send_inn(self):
        vin_value = self.avtovin
        lead_id = self.id
        api_url = 'https://2d47-193-93-219-131.ngrok-free.app/avtovin'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Catch-Control': 'no-cache'}
        payload = {'lead_id': lead_id, 'vin_value': vin_value}

        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            return
        else:
            raise ValidationError('За цим VIN даних не знайдено')
