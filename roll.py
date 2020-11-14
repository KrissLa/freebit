from datetime import datetime, timedelta

import pytz
from pytz import timezone
from time import sleep
from loguru import logger
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from db_api.db_commands import get_profiles, update_profile, add_roll
from db_api.db_tortoise import on_startup

utc = pytz.UTC


async def start_rolling():
    """Запускаем"""
    await on_startup()
    while True:
        try:
            profiles = await get_profiles()
            for pd in profiles:
                try:
                    if pd['last_date']:
                        _check_for_time(pd['last_date'])
                    options = webdriver.ChromeOptions()
                    options.add_argument("user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data")
                    options.add_argument(f"--profile-directory={pd['name']}")
                    browser = webdriver.Chrome(chrome_options=options)
                    sleep(3)
                    browser.get('https://freebitco.in/')
                    sleep(5)
                    _cancel_notification(browser)
                    button = _get_button_or_none(browser)
                    if button:
                        logger.info('Кнопка доступна!')
                        if _captcha_is_needed(browser):
                            logger.info('Капча нужна!')
                            _click_i_not_robot(browser)
                            _wait_captcha_complete(browser)
                        else:
                            logger.info('Капчи нет!')
                        button.send_keys(Keys.RETURN)
                        sleep(2)

                    actual_balance = _get_balance_or_none(browser)
                    if not actual_balance:
                        actual_balance = pd['actual_balance']
                    total_winnings = pd['total_winnings']
                    winning = _get_winning_or_none(browser)
                    if winning:
                        status = 'OK'
                    else:
                        status = 'ERROR'
                    now_date = datetime.now(timezone('Europe/Moscow'))
                    await update_profile(profile_id=pd['id'], actual_balance=actual_balance,
                                         total_winning=total_winnings, last_date=now_date, winning=winning)
                    await add_roll(pd['id'], winning, status, now_date)
                    browser.close()
                except:
                    pass
        except:
            pass


def roll_one():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument(f"--profile-directory=Profile 24")
    # options.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=options)
    sleep(2)
    browser.get('https://freebitco.in/')
    sleep(2)
    account_balance = {
        'account': 'Profile 24',
        'balance': _get_balance_or_none(browser),
        'date': datetime.now(timezone('Europe/Moscow')).strftime("%d.%m.%Y"),
        'time': datetime.now(timezone('Europe/Moscow')).strftime("%H:%M")
    }
    logger.info(account_balance)
    button = _get_button_or_none(browser)
    if button:
        logger.info('Кнопка доступна!')
        if _captcha_is_needed(browser):
            logger.info('Капча нужна!')
            # _wait_captcha_complete(browser)
            _click_i_not_robot(browser)
            sleep(999)
        else:
            logger.info('Капчи нет!')
    button.send_keys(Keys.RETURN)
    sleep(2)
    browser.close()


def _cancel_notification(browser):
    """Отменяем уведомления"""
    try:
        modal = browser.find_element_by_id('push_notification_modal')
        print('Нашел окно')
    except:
        modal = None
    try:
        if modal:
            button = browser.find_element_by_css_selector('.pushpad_deny_button')
            button.click()
    except:
        pass


def _get_button_or_none(browser):
    """Проверяем наличие кнопки ROLL!"""
    try:
        button = browser.find_element_by_css_selector('#free_play_form_button')
        ActionChains(browser).move_to_element(button).perform()
        return button
    except Exception as err:
        logger.error(err)
        return None


def _get_balance_or_none(browser):
    """Получаем баланс аккаунта"""
    try:
        balance = browser.find_element_by_id('balance')
        logger.info(f'Функция _get_balance_or_none:\n'
                    f'balance = {float(balance.text)}')
        return float(balance.text)
    except Exception as err:
        try:
            balance = browser.find_element_by_id('balance_small')
            logger.info(f'Функция _get_balance_or_none:\n'
                        f'balance = {float(balance.text)}')
            return float(balance.text)
        except Exception as err:
            logger.error(f'Функция _get_balance_or_none:\n'
                         f'Не удалось получить баланс {err}')
            return None


def _captcha_is_needed(browser):
    """Проверяем нужна ли капча"""
    try:
        browser.find_element_by_css_selector('.g-recaptcha')
        return True
    except Exception as err:
        return False


def _click_i_not_robot(browser):
    """Нажатие на я не робот"""
    try:
        i_not_robot_button = browser.find_element_by_css_selector('.g-recaptcha div div')
        ActionChains(browser).move_to_element(i_not_robot_button).perform()
        i_not_robot_button.click()
    except Exception as err:
        logger.error(err)
    sleep(3)



def _wait_captcha_complete(browser):
    """Ожидание решения капчи"""
    while True:
        status = browser.find_element_by_css_selector('.status')
        if status.text in ["Solved", "AntiCaptcha"]:
            return True
        elif status.text in ["Could not load captcha provider widget in worker browser. Please try again.",
                             "Outdated, should be solved again"]:
            browser.get('https://freebitco.in/')
            sleep(5)
        sleep(3)


def _get_winning_or_none(browser):
    """Проверяем на ошибку ip после прокрутки"""
    try:
        winning = browser.find_element_by_css_selector('#winnings')
        win = float(winning.text)
        logger.info(f'Функция _get_winning_or_none:\n'
                    f'winning = {win}')
    except Exception as err:
        win = 0
        logger.error(f'Функция _get_winning_or_none:\n'
                     f'Не удалось получить winning {err}')
    return win


def _check_for_time(last_time):
    """Проверяем время и, если нужно, ждем"""
    now = datetime.now(timezone('Europe/Moscow'))
    logger.info(f'Вошел в функцию _check_for_time с параметрами:\n'
                f'Последнее время - {last_time.strftime("%d.%m.%Y _ %H:%M:%S")}\n'
                f"Сейчас - {now.strftime('%d.%m.%Y _ %H:%M:%S')}")
    while True:

        check = datetime.now(timezone('Europe/Moscow')) - timedelta(hours=1, seconds=10)
        if check.replace(tzinfo=None) > last_time:
            logger.info('Выхожу из функции _check_for_time')
            return
        sleep(20)


