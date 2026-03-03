from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def action_set_won_rainbowman(self):
        # Chạy lệnh gốc của Odoo
        res = super(CrmLead, self).action_set_won_rainbowman()
        
        for lead in self:
            # TỰ ĐỘNG HÓA QUY TRÌNH (MỨC 2)
            self.env['project.task'].create({
                'name': f'Triển khai cho khách hàng: {lead.partner_id.name or lead.name}',
                'project_id': 1, 
                'user_id': lead.user_id.id, # ĐỒNG BỘ NHÂN SỰ TỪ HRM (MỨC 1)
                'description': f'Công việc được tạo tự động từ cơ hội: {lead.name}',
            })
        return res
