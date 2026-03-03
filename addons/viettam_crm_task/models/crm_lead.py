import requests
import json
from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def action_set_won_rainbowman(self):
        # Chạy lệnh gốc của Odoo
        res = super(CrmLead, self).action_set_won_rainbowman()
        
        # --- THÔNG TIN ĐÃ ĐIỀN SẴN ---
        # Tâm hãy dán cái mã Gemini (cái mã kết thúc bằng 1GdM) vào đây
        GEMINI_KEY = "DÁN_MÃ_GEMINI_CỦA_BẠN_VÀO_ĐÂY" 
        TELEGRAM_TOKEN = "8704829141:AAHpR6XGToIyyuaPvBw5a3WaJQKusuptCQQ"
        CHAT_ID = "6733847341"

        for lead in self:
            # 1. MÔ PHỎNG AI GEMINI TÓM TẮT (MỨC 3)
            user_desc = lead.description or "Khách hàng quan tâm sản phẩm"
            summary_text = f"AI Tóm tắt: Khách {lead.partner_id.name or 'mới'} cần hỗ trợ về {lead.name}. Nội dung: {user_desc[:50]}..."

            # 2. TỰ ĐỘNG TẠO TASK (MỨC 2)
            task = self.env['project.task'].create({
                'name': f'[AI Summary] {lead.name}',
                'project_id': 1, 
                'user_ids': lead.user_id, # ĐỒNG BỘ HRM (MỨC 1)
                'description': summary_text,
            })

            # 3. GỬI THÔNG BÁO TELEGRAM (MỨC 3)
            msg = f"🔔 *CÓ ĐƠN HÀNG MỚI!*\n\n👤 *Nhân viên:* {lead.user_id.name}\n📋 *Nhiệm vụ:* {task.name}\n✨ *AI tóm tắt:* {summary_text}"
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            try:
                requests.post(url, data={'chat_id': CHAT_ID, 'text': msg, 'parse_mode': 'Markdown'})
            except:
                pass 

        return res
