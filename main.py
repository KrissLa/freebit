import asyncio

from roll import start_rolling


if __name__ == '__main__':
    asyncio.run(start_rolling())
    # roll(datetime.now(timezone('Europe/Moscow')) - timedelta(minutes=70))
    # roll_one()

# curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d {\"clientKey\":\"417605982153d740ef7f678aab123e39\"} https://api.anti-captcha.com/getBalance
