from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMessage
import requests

class Users(AbstractBaseUser, PermissionsMixin):

    world_datetime = requests.get('https://worldtimeapi.org/api/ip')
    current_time = world_datetime.json()['datetime']

    username = models.CharField(max_length=150, blank=True , unique=True)
    email = models.EmailField(_('email address'), unique=True)
    points = models.IntegerField(default=0)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=current_time)
    is_superuser = models.BooleanField(_('staff'), default=False)
    is_logged_in = models.BooleanField(_('logged in'), default=False)
    is_activated = models.BooleanField(_('activated'), default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

#     # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
#     email_html_message = f"""
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>รีเซ็ตรหัสผ่านสำหรับบัญชี Crediation portal</title>
#             <style>
#                 /* Inline CSS styles */
#                 body {{
#                     font-family: Arial, sans-serif;
#                     background-color: #f4f4f4;
#                     margin: 0;
#                     padding: 0;
#                 }}
#                 .container {{
#                     max-width: 600px;
#                     margin: 0 auto;
#                     padding: 20px;
#                     background-color: #fff;
#                     border-radius: 10px;
#                     box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
#                 }}
#                 h1 {{
#                     color: #333;
#                 }}
#                 p {{
#                     color: #555;
#                 }}
#                 .button {{
#                     display: inline-block;
#                     padding: 10px 20px;
#                     background-color: #007bff;
#                     text-decoration: none;
#                     color:white;
#                     border-radius: 5px;
#                     border: none;
#                     cursor: pointer;
#                 }}
#                 .button:hover {{
#                     background-color: #0056b3;
#                 }}
#             </style>
#         </head>
#         <body>
#             <div class="container">
#                 <h1>รีเซ็ตรหัสผ่าน</h1>
#                 <p>เรียนผู้ใช้งาน,</p>
#                 <p>เราได้รับคำขอเพื่อรีเซ็ตรหัสผ่านสำหรับบัญชี Crediation portal ของคุณ หากคุณไม่ได้ทำคำขอนี้ โปรดเพิกเฉยต่ออีเมลนี้</p>
#                 <p>เพื่อรีเซ็ตรหัสผ่านของคุณ โปรดคลิกที่ปุ่มด้านล่าง:</p>
#                 <a href="{instance.request.build_absolute_uri('https://vanman.vercel.app/reset-password/')}{reset_password_token.key}" class="button">รีเซ็ตรหัสผ่าน</a>
#                 <p>หากปุ่มด้านบนไม่ทำงาน คุณสามารถคัดลอกและวาง URL ต่อไปนี้ลงในแถบที่อยู่ของเบราว์เซอร์ของคุณ:</p>
#                 <p>{instance.request.build_absolute_uri('https://vanman.vercel.app/reset-password/')}{reset_password_token.key}</p>
#                 <p>ขอบคุณค่ะ</p>
#                 <p>ขอแสดงความนับถือ<br>บริษัท VANMAN</p>
#             </div>
#         </body>
#         </html>
#     """
#     send_mail(
#         # title:
#         # หัวข้อ
#         "คุณขอรีเซ็ตรหัสผ่านบนเว็บไซต์ Mixallz",
#         # ข้อความ (เนื้อหา HTML)
#         "",
#         # ผู้ส่ง
#         "ระบบ Mixallz",
#         # ผู้รับ
#         [reset_password_token.user.email],
#         # ข้อความ HTML
#         html_message=email_html_message,
#         # ห้ามล้มเหลวเงียบ (เกิดข้อผิดพลาดหากการส่งล้มเหลว)
#         fail_silently=False,
#     )