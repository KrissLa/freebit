from datetime import datetime

from pytz import timezone

from db_api import Profiles, Rolls
from tortoise.exceptions import IntegrityError
from loguru import logger


async def add_profiles(profiles):
    """Добавляем профили в базу"""

    for pr in profiles:
        try:
            await Profiles.create(name=pr['name'], email=pr['email'], start_balance=f"{pr['start_balance']:8f}",
                                  total_winnings=0)
        except IntegrityError:
            pass


async def update_profile(profile_id,
                         actual_balance,
                         total_winning,
                         last_date,
                         winning=None):
    """Обновляем аккаунт"""
    left_until_withdraw = 0.0003 - actual_balance
    left_until_withdraw_times = (0.0003 - actual_balance) // 0.00000014
    if winning:
        total_winning = total_winning + winning

    try:
        await Profiles.filter(id=profile_id).update(actual_balance=actual_balance,
                                                    left_until_withdraw=left_until_withdraw,
                                                    left_until_withdraw_times=left_until_withdraw_times,
                                                    total_winnings=total_winning,
                                                    last_date=last_date)

    except Exception as err:
        logger.error(err)


async def add_roll(profile_id, winning, status, date_of_roll):
    """Обновляем аккаунт"""
    try:
        await Rolls.create(profile_id=profile_id, winning=winning, status=status,
                           date_of_roll=date_of_roll.strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as err:
        logger.error(err)


async def get_profiles():
    """Получаем все аккаунты"""
    try:
        return await Profiles.all().order_by('id').values('id', 'name', 'actual_balance', 'last_date', 'total_winnings')
    except Exception as err:
        logger.exception(err)
