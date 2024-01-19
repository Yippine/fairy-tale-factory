from django.db import models

# 使用者 User
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.SmallIntegerField(default=1, choices=[(0, '開發人員'), (1, '一般用戶')])
    user_name = models.CharField(max_length=50)
    user_nick_name = models.CharField(max_length=50, null=True, blank=True)
    user_password = models.CharField(max_length=16)
    user_email = models.EmailField(max_length=255, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'user'

# 指令 Prompt（Deprecated）
class Prompt(models.Model):
    prompt_id = models.PositiveSmallIntegerField(primary_key=True)
    prompt_name = models.CharField(max_length=50, null=False)
    version_code = models.PositiveSmallIntegerField(null=True, blank=True)
    version_desc = models.CharField(max_length=255, null=True, blank=True)
    prompt_content = models.CharField(max_length=2000, null=False)
    developer_id = models.PositiveIntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'prompt'

# 金鑰費用 ApiKeyCost
class ApiKeyCost(models.Model):
    key_id = models.PositiveSmallIntegerField()
    user_id = models.PositiveIntegerField()
    usd_key_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    twd_key_cost = models.PositiveSmallIntegerField(null=True, blank=True)
    unit = models.CharField(max_length=10, choices=[('Tokens', 'Tokens'), ('Images', 'Images')], null=False)
    quantity = models.PositiveSmallIntegerField(null=False)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'api_key_cost'
        unique_together = (('key_id', 'user_id'),)

# 金鑰 ApiKey
class ApiKey(models.Model):
    key_id = models.PositiveSmallIntegerField(primary_key=True)
    key_name = models.CharField(max_length=50, null=False)
    key_password = models.CharField(max_length=255, null=False)
    developer_id = models.PositiveIntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'api_key'
