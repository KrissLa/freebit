from tortoise import fields
from tortoise.models import Model


class Profiles(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255)
    start_balance = fields.FloatField()
    actual_balance = fields.FloatField(null=True)
    total_winnings = fields.FloatField(null=True)
    left_until_withdraw = fields.FloatField(null=True)
    left_until_withdraw_times = fields.IntField(null=True)
    last_date = fields.DatetimeField(null=True)
    deposits = fields.FloatField(default=0)
    withdraws = fields.FloatField(default=0)


class Rolls(Model):
    id = fields.IntField(pk=True)
    profile_id = fields.IntField()
    winning = fields.FloatField()
    status = fields.CharField(max_length=10)
    date_of_roll = fields.DatetimeField(tzinfo=True)
