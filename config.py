import os

from dotenv import load_dotenv

load_dotenv()

ip = os.getenv("ip")
PORT = int(os.getenv("PORT"))
DB_NAME = str(os.getenv("DB_NAME"))
PG_USER = str(os.getenv("PG_USER"))
PG_PASSWORD = str(os.getenv("PG_PASSWORD"))

POSTGRES_URI = f"postgres://{PG_USER}:{PG_PASSWORD}@{ip}/{DB_NAME}"

key = '417605982153d740ef7f678aab123e39'

PROFILES = [
    {'name': 'Profile 1', 'start_balance': 0.00003777, 'email': 'tigrenok.kisa13@gmail.com'},
    {'name': 'Profile 2', 'start_balance': 0.00003497, 'email': 'arsavit1@gmail.com'},
    {'name': 'Profile 3', 'start_balance': 0.00002648, 'email': 'arsavit.tigrenok@gmail.com'},
    {'name': 'Profile 4', 'start_balance': 0.0000239, 'email': 'voropaev.vladimir94@gmail.com'},
    {'name': 'Profile 5', 'start_balance': 0.00006368, 'email': 'andreykirov721109@gmail.com'},
    {'name': 'Profile 6', 'start_balance': 0.00005459, 'email': 'yavgrniy.prostokov@gmail.com'},
    {'name': 'Profile 7', 'start_balance': 0.00001588, 'email': 'vanykurochkin123@gmail.com'},
    {'name': 'Profile 8', 'start_balance': 0.00003089, 'email': 'dansherizz@gmail.com'},
    {'name': 'Profile 9', 'start_balance': 0.00003847, 'email': 'fedfedkalkal@gmail.com'},
    {'name': 'Profile 10', 'start_balance': 0.00006734, 'email': 'palka4813@gmail.com'},
    {'name': 'Profile 11', 'start_balance': 0.00001865, 'email': 'psina4813@gmail.com'},
    {'name': 'Profile 12', 'start_balance': 0.00004051, 'email': 'stasenkovladislav15@gmail.com'},
    {'name': 'Profile 13', 'start_balance': 0.00010628, 'email': '16kisa@gmail.com'},
    {'name': 'Profile 14', 'start_balance': 0.00009175, 'email': '177kisa@gmail.com'},
    {'name': 'Profile 15', 'start_balance': 0.00004659, 'email': '18lissa18@gmail.com'},
    {'name': 'Profile 16', 'start_balance': 0.0000318, 'email': 'maksimavramcik3@gmail.com'},
    {'name': 'Profile 17', 'start_balance': 0.00001283, 'email': '20vovavo20@gmail.com'},
    {'name': 'Profile 18', 'start_balance': 0, 'email': 'ligusermakova@gmail.com'},
    {'name': 'Profile 19', 'start_balance': 0, 'email': 'tunuevacuentaya01@gmail.com'},
    {'name': 'Profile 20', 'start_balance': 0, 'email': 'socpublic2k19@gmail.com'},
    {'name': 'Profile 21', 'start_balance': 0, 'email': 'unik10102020@gmail.com'},
    {'name': 'Profile 22', 'start_balance': 0, 'email': 'urievvaran@gmail.com'},
    {'name': 'Profile 23', 'start_balance': 0, 'email': 'kirrilbiskup@gmail.com'},
    {'name': 'Profile 24', 'start_balance': 0, 'email': 'ppooommyyy@gmail.com'},
    {'name': 'Profile 25', 'start_balance': 0, 'email': 'socpublic6996@gmail.com'},
    {'name': 'Profile 26', 'start_balance': 0, 'email': 'banatoli399@gmail.com'},
    {'name': 'Profile 27', 'start_balance': 0.00000609, 'email': 'konductor24@gmail.com'},
    {'name': 'Profile 28', 'start_balance': 0.00000609, 'email': 'udovenkoura733@gmail.com'},
    {'name': 'Profile 29', 'start_balance': 0.0000061, 'email': 'sgejahah@gmail.com'},
    {'name': 'Profile 30', 'start_balance': 0.00000817, 'email': 'oprivanov@gmail.com'},
    {'name': 'Profile 31', 'start_balance': 0.00000623, 'email': 'acredis2019@gmail.com'},
    {'name': 'Profile 32', 'start_balance': 0.00000623, 'email': 'dmitriypetrov20000823@gmail.com'},
    {'name': 'Profile 33', 'start_balance': 0.00000622, 'email': 'zanrimma@gmail.com'},
    {'name': 'Profile 34', 'start_balance': 0.00000746, 'email': 'vladimirpalcev129@gmail.com'},
    {'name': 'Profile 35', 'start_balance': 0.00000816, 'email': 'ar1340990@gmail.com'},
    {'name': 'Profile 36', 'start_balance': 0.0000081, 'email': 'olegg97w@gmail.com'},
    {'name': 'Profile 37', 'start_balance': 0.00000622, 'email': 'robota5467@gmail.com'},
    {'name': 'Profile 38', 'start_balance': 0.00000622, 'email': 'luknaarr@gmail.com'},
    {'name': 'Profile 39', 'start_balance': 0.00000622, 'email': 'zanzanzan556@gmail.com'},
    {'name': 'Profile 40', 'start_balance': 0.00000814, 'email': 'snevzh@gmail.com'},
    {'name': 'Profile 41', 'start_balance': 0.00000622, 'email': 'suptik228@gmail.com'},
    {'name': 'Profile 42', 'start_balance': 0.00000622, 'email': 'vasyaandry91@gmail.com'},
    {'name': 'Profile 43', 'start_balance': 0.00000814, 'email': 'ivanov577402@gmail.com'},
    {'name': 'Profile 44', 'start_balance': 0.00000622, 'email': 'pitrpen767@gmail.com'},
    {'name': 'Profile 45', 'start_balance': 0.00000622, 'email': 'gyglposta231234@gmail.com'},
    {'name': 'Profile 46', 'start_balance': 0.00000814, 'email': 'eremeyeremin22@gmail.com'},
    {'name': 'Profile 47', 'start_balance': 0.00000622, 'email': 'russkiy.rosiyan@gmail.com'},
    {'name': 'Profile 48', 'start_balance': 0.00000622, 'email': 'gaponchikdanilo@gmail.com'},
    {'name': 'Profile 49', 'start_balance': 0.00000622, 'email': 'krasavettts.93838@gmail.com'},
    {'name': 'Profile 50', 'start_balance': 0.00002725, 'email': 'avpornev@gmail.com'},
    {'name': 'Profile 51', 'start_balance': 0, 'email': 'ppasha1a@yahoo.com'},
    {'name': 'Profile 52', 'start_balance': 0, 'email': 'ffr3ddis@yahoo.com'},
    {'name': 'Profile 53', 'start_balance': 0, 'email': 'ketttyy@yahoo.com'},
    {'name': 'Profile 54', 'start_balance': 0, 'email': 'peetterr@yahoo.com'},
    {'name': 'Profile 55', 'start_balance': 0, 'email': 'vitalmishkov@yahoo.com'},
    {'name': 'Profile 56', 'start_balance': 0, 'email': 'dorenom@mail.ru'},
    {'name': 'Profile 57', 'start_balance': 0, 'email': 'domiiniik1@mail.ru'},
    {'name': 'Profile 58', 'start_balance': 0, 'email': 'ggaryr@bk.ru'},
    {'name': 'Profile 59', 'start_balance': 0, 'email': 'harollld@yahoo.com'},
    {'name': 'Profile 60', 'start_balance': 0, 'email': 'jonathaah@mail.ru'},
    {'name': 'Profile 61', 'start_balance': 0, 'email': 'samuiuel@mail.ru'},
    {'name': 'Profile 62', 'start_balance': 0, 'email': 'xavierri@mail.ru'},
    {'name': 'Profile 63', 'start_balance': 0, 'email': 'loenaro@mail.ru'},
    {'name': 'Profile 64', 'start_balance': 0, 'email': 'florancere@mail.ru'},
    {'name': 'Profile 65', 'start_balance': 0, 'email': 'branndonn@bk.ru'},
    {'name': 'Profile 66', 'start_balance': 0, 'email': 'cameroom@mail.ru'},
    {'name': 'Profile 67', 'start_balance': 0, 'email': 'edwarido@mail.ru'},
    {'name': 'Profile 68', 'start_balance': 0, 'email': 'ssclifford@mail.ru'},
    {'name': 'Profile 69', 'start_balance': 0, 'email': 'amandianda@mail.ru'},
    {'name': 'Profile 70', 'start_balance': 0, 'email': 'martinnoz@mail.ru'},
    {'name': 'Profile 71', 'start_balance': 0, 'email': 'deisyday@mail.ru'},
    {'name': 'Profile 72', 'start_balance': 0, 'email': 'gabrigabrr@mail.ru'},
    {'name': 'Profile 73', 'start_balance': 0, 'email': 'isaaacas@mail.ru'},
    {'name': 'Profile 74', 'start_balance': 0, 'email': 'ceciili@mail.ru'},
    {'name': 'Profile 75', 'start_balance': 0, 'email': 'amamandana@mail.ru'},
    {'name': 'Profile 76', 'start_balance': 0, 'email': 'benjanimbe@mail.ru'},
    {'name': 'Profile 77', 'start_balance': 0, 'email': 'divad.d@mail.ru'},
    {'name': 'Profile 78', 'start_balance': 0, 'email': 'marjorieer@mail.ru'},
    {'name': 'Profile 79', 'start_balance': 0, 'email': 'ssacul@mail.ru'},
    {'name': 'Profile 80', 'start_balance': 0, 'email': 'gloriaair@mail.ru'},
    {'name': 'Profile 81', 'start_balance': 0, 'email': 'tinjust@mail.ru'},
    {'name': 'Profile 82', 'start_balance': 0, 'email': 'christossian@mail.ru'},
    {'name': 'Profile 83', 'start_balance': 0, 'email': 'adelinnna@inbox.ru'},
    {'name': 'Profile 84', 'start_balance': 0, 'email': 'hhanahn@mail.ru'},
    {'name': 'Profile 85', 'start_balance': 0, 'email': 'mmigge@mail.ru'},
    {'name': 'Profile 86', 'start_balance': 0, 'email': 'olioliv@bk.ru'},
    {'name': 'Profile 87', 'start_balance': 0, 'email': 'nancyycan@mail.ru'},
    {'name': 'Profile 88', 'start_balance': 0, 'email': 'morganno@bk.ru'},
    {'name': 'Profile 89', 'start_balance': 0, 'email': 'cyrusuc@mail.ru'},
    {'name': 'Profile 90', 'start_balance': 0, 'email': 'chloeei@mail.ru'},
    {'name': 'Profile 91', 'start_balance': 0, 'email': 'austinno@bk.ru'},
    {'name': 'Profile 92', 'start_balance': 0, 'email': 'dieggoron@mail.ru'},
    {'name': 'Profile 93', 'start_balance': 0, 'email': 'elelelearnor@mail.ru'},
    {'name': 'Profile 94', 'start_balance': 0, 'email': 'fionari@bk.ru'},
    {'name': 'Profile 95', 'start_balance': 0, 'email': 'gavinci@bk.ru'},
    {'name': 'Profile 96', 'start_balance': 0, 'email': 'helehen@mail.ru'},
    {'name': 'Profile 97', 'start_balance': 0, 'email': 'marisiaa@bk.ru'},
    {'name': 'Profile 98', 'start_balance': 0, 'email': 'lukecoinn@mail.ru'},
    {'name': 'Profile 99', 'start_balance': 0, 'email': 'brooookee@mail.ru'},
    {'name': 'Profile 100', 'start_balance': 0.0002511, 'email': 'arsavit@gmail.com'}
]

# PROFILES = [
#     {'name': 'Profile 1', 'start_balance': 0.00003777, 'email': 'tigrenok.kisa13@gmail.com'},
#     {'name': 'Profile 2', 'start_balance': 0.00003497, 'email': 'arsavit1@gmail.com'},
#     {'name': 'Profile 3', 'start_balance': 0.00002648, 'email': 'arsavit.tigrenok@gmail.com'},
#     {'name': 'Profile 4', 'start_balance': 0.0000239,  'email': 'voropaev.vladimir94@gmail.com'},
#     {'name': 'Profile 5', 'start_balance': 0.00006368, 'email': 'andreykirov721109@gmail.com'},
#     {'name': 'Profile 6', 'start_balance': 0.00005459, 'email': 'yavgrniy.prostokov@gmail.com'},
#     {'name': 'Profile 7', 'start_balance': 0.00001588, 'email': 'vanykurochkin123@gmail.com'},
#     {'name': 'Profile 8', 'start_balance': 0.00003089, 'email': 'dansherizz@gmail.com'},
#     {'name': 'Profile 9', 'start_balance': 0.00003847, 'email': 'fedfedkalkal@gmail.com'},
#     {'name': 'Profile 11', 'start_balance': 0.00006734, 'email': 'palka4813@gmail.com'},
#     {'name': 'Profile 12', 'start_balance': 0.00001865, 'email': 'psina4813@gmail.com'},
#     {'name': 'Profile 13', 'start_balance': 0.00004051, 'email': 'stasenkovladislav15@gmail.com'},
#     {'name': 'Profile 14', 'start_balance': 0.00010628, 'email': '16kisa@gmail.com'},
#     {'name': 'Profile 15', 'start_balance': 0.00009175, 'email': '177kisa@gmail.com'},
#     {'name': 'Profile 16', 'start_balance': 0.00004659, 'email': '18lissa18@gmail.com'},
#     {'name': 'Profile 17', 'start_balance': 0.0000318, 'email': 'maksimavramcik3@gmail.com'},
#     {'name': 'Profile 18', 'start_balance': 0.00001283, 'email': '20vovavo20@gmail.com'},
#     {'name': 'Profile 23', 'start_balance': 0.0002511, 'email': 'arsavit@gmail.com'},
#     {'name': 'Profile 24', 'start_balance': 0, 'email': 'ligusermakova@gmail.com'},
#     {'name': 'Profile 25', 'start_balance': 0, 'email': 'tunuevacuentaya01@gmail.com'},
#     {'name': 'Profile 26', 'start_balance': 0, 'email': 'socpublic2k19@gmail.com'},
#     {'name': 'Profile 27', 'start_balance': 0, 'email': 'unik10102020@gmail.com'},
#     {'name': 'Profile 28', 'start_balance': 0, 'email': 'urievvaran@gmail.com'},
#     {'name': 'Profile 29', 'start_balance': 0, 'email': 'kirrilbiskup@gmail.com'},
#     {'name': 'Profile 30', 'start_balance': 0, 'email': 'ppooommyyy@gmail.com'},
#     {'name': 'Profile 31', 'start_balance': 0, 'email': 'socpublic6996@gmail.com'},
#     {'name': 'Profile 32', 'start_balance': 0, 'email': 'banatoli399@gmail.com'},
# ]
