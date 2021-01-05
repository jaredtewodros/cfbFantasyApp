# Iain Muir
# iam9ez

# from bs4 import BeautifulSoup
# import pandas as pd
# import requests

POWER_FIVE = [
    ('Atlantic Coast Conference', 'ACC'),
    ('Big 12', 'Big%2012'),
    ('Big 10', 'Big%20Ten'),
    ('South Eastern Conference', 'SEC'),
    ('Pacific-12', 'Pac-12')
]

POWER_FIVE_TEAMS = [
    'Notre Dame',
    'Clemson',
    'Miami',
    'North Carolina',
    'NC State',
    'Boston College',
    'Pittsburgh',
    'Virginia Tech',
    'Virginia',
    'Wake Forest',
    'Georgia Tech',
    'Louisville',
    'Florida State',
    'Duke',
    'Syracuse',
    'Florida',
    'Georgia',
    'Missouri',
    'Kentucky',
    'Tennessee',
    'South Carolina',
    'Vanderbilt',
    'Alabama',
    'Texas A&M',
    'Auburn',
    'LSU',
    'Ole Miss',
    'Arkansas',
    'Mississippi State',
    'Washington',
    'Stanford',
    'Oregon',
    'Oregon State',
    'California',
    'Washington State',
    'USC',
    'Colorado',
    'Utah',
    'Arizona State',
    'UCLA',
    'Arizona',
    'Ohio State',
    'Indiana',
    'Penn State',
    'Maryland',
    'Rutgers',
    'Michigan',
    'Michigan State',
    'Northwestern',
    'Iowa',
    'Wisconsin',
    'Minnesota',
    'Nebraska',
    'Purdue',
    'Illinois',
    'Iowa State',
    'Oklahoma',
    'Oklahoma State',
    'Texas',
    'TCU',
    'West Virginia',
    'Kansas State',
    'Texas Tech',
    'Baylor',
    'Kansas'
]

ACC = [['Notre Dame',
        '501',
        'https://assets-sports.thescore.com/football/team/501/small_logo.png'],
       ['Clemson',
        '158',
        'https://assets-sports.thescore.com/football/team/158/small_logo.png'],
       ['Miami',
        '405',
        'https://assets-sports.thescore.com/football/team/405/small_logo.png'],
       ['North Carolina',
        '472',
        'https://assets-sports.thescore.com/football/team/472/small_logo.png'],
       ['NC State',
        '476',
        'https://assets-sports.thescore.com/football/team/476/small_logo.png'],
       ['Boston College',
        '100',
        'https://assets-sports.thescore.com/football/team/100/small_logo.png'],
       ['Pittsburgh',
        '526',
        'https://assets-sports.thescore.com/football/team/526/small_logo.png'],
       ['Virginia Tech',
        '689',
        'https://assets-sports.thescore.com/football/team/689/small_logo.png'],
       ['Virginia',
        '686',
        'https://assets-sports.thescore.com/football/team/686/small_logo.png'],
       ['Wake Forest',
        '694',
        'https://assets-sports.thescore.com/football/team/694/small_logo.png'],
       ['Georgia Tech',
        '257',
        'https://assets-sports.thescore.com/football/team/257/small_logo.png'],
       ['Louisville',
        '369',
        'https://assets-sports.thescore.com/football/team/369/small_logo.png'],
       ['Florida State',
        '237',
        'https://assets-sports.thescore.com/football/team/237/small_logo.png'],
       ['Duke',
        '202',
        'https://assets-sports.thescore.com/football/team/202/small_logo.png'],
       ['Syracuse',
        '625',
        'https://assets-sports.thescore.com/football/team/625/small_logo.png']]

BIG_TWELVE = [['Iowa State',
               '307',
               'https://assets-sports.thescore.com/football/team/307/small_logo.png'],
              ['Oklahoma',
               '509',
               'https://assets-sports.thescore.com/football/team/509/small_logo.png'],
              ['Oklahoma State',
               '510',
               'https://assets-sports.thescore.com/football/team/510/small_logo.png'],
              ['Texas',
               '634',
               'https://assets-sports.thescore.com/football/team/634/small_logo.png'],
              ['TCU',
               '628',
               'https://assets-sports.thescore.com/football/team/628/small_logo.png'],
              ['West Virginia',
               '716',
               'https://assets-sports.thescore.com/football/team/716/small_logo.png'],
              ['Kansas State',
               '329',
               'https://assets-sports.thescore.com/football/team/329/small_logo.png'],
              ['Texas Tech',
               '642',
               'https://assets-sports.thescore.com/football/team/642/small_logo.png'],
              ['Baylor',
               '81',
               'https://assets-sports.thescore.com/football/team/81/small_logo.png'],
              ['Kansas',
               '328',
               'https://assets-sports.thescore.com/football/team/328/small_logo.png']]


BIG_TEN = [['Ohio State',
            '507',
            'https://assets-sports.thescore.com/football/team/507/small_logo.png'],
           ['Indiana',
            '303',
            'https://assets-sports.thescore.com/football/team/303/small_logo.png'],
           ['Penn State',
            '521',
            'https://assets-sports.thescore.com/football/team/521/small_logo.png'],
           ['Maryland',
            '388',
            'https://assets-sports.thescore.com/football/team/388/small_logo.png'],
           ['Rutgers',
            '550',
            'https://assets-sports.thescore.com/football/team/550/small_logo.png'],
           ['Michigan',
            '407',
            'https://assets-sports.thescore.com/football/team/407/small_logo.png'],
           ['Michigan State',
            '408',
            'https://assets-sports.thescore.com/football/team/408/small_logo.png'],
           ['Northwestern',
            '493',
            'https://assets-sports.thescore.com/football/team/493/small_logo.png'],
           ['Iowa',
            '306',
            'https://assets-sports.thescore.com/football/team/306/small_logo.png'],
           ['Wisconsin',
            '748',
            'https://assets-sports.thescore.com/football/team/748/small_logo.png'],
           ['Minnesota',
            '418',
            'https://assets-sports.thescore.com/football/team/418/small_logo.png'],
           ['Nebraska',
            '457',
            'https://assets-sports.thescore.com/football/team/457/small_logo.png'],
           ['Purdue',
            '534',
            'https://assets-sports.thescore.com/football/team/534/small_logo.png'],
           ['Illinois',
            '298',
            'https://assets-sports.thescore.com/football/team/298/small_logo.png']]

SEC = [['Florida',
        '233',
        'https://assets-sports.thescore.com/football/team/233/small_logo.png'],
       ['Georgia',
        '255',
        'https://assets-sports.thescore.com/football/team/255/small_logo.png'],
       ['Missouri',
        '429',
        'https://assets-sports.thescore.com/football/team/429/small_logo.png'],
       ['Kentucky',
        '333',
        'https://assets-sports.thescore.com/football/team/333/small_logo.png'],
       ['Tennessee',
        '630',
        'https://assets-sports.thescore.com/football/team/630/small_logo.png'],
       ['South Carolina',
        '573',
        'https://assets-sports.thescore.com/football/team/573/small_logo.png'],
       ['Vanderbilt',
        '684',
        'https://assets-sports.thescore.com/football/team/684/small_logo.png'],
       ['Alabama',
        '40',
        'https://assets-sports.thescore.com/football/team/40/small_logo.png'],
       ['Texas A&M',
        '635',
        'https://assets-sports.thescore.com/football/team/635/small_logo.png'],
       ['Auburn',
        '67',
        'https://assets-sports.thescore.com/football/team/67/small_logo.png'],
       ['LSU',
        '370',
        'https://assets-sports.thescore.com/football/team/370/small_logo.png'],
       ['Ole Miss',
        '425',
        'https://assets-sports.thescore.com/football/team/425/small_logo.png'],
       ['Arkansas',
        '59',
        'https://assets-sports.thescore.com/football/team/59/small_logo.png'],
       ['Mississippi State',
        '427',
        'https://assets-sports.thescore.com/football/team/427/small_logo.png']]


PAC_TWELVE = [['Washington',
               '699',
               'https://assets-sports.thescore.com/football/team/699/small_logo.png'],
              ['Stanford',
               '616',
               'https://assets-sports.thescore.com/football/team/616/small_logo.png'],
              ['Oregon',
               '514',
               'https://assets-sports.thescore.com/football/team/514/small_logo.png'],
              ['Oregon State',
               '515',
               'https://assets-sports.thescore.com/football/team/515/small_logo.png'],
              ['California',
               '118',
               'https://assets-sports.thescore.com/football/team/118/small_logo.png'],
              ['Washington State',
               '703',
               'https://assets-sports.thescore.com/football/team/703/small_logo.png'],
              ['USC',
               '676',
               'https://assets-sports.thescore.com/football/team/676/small_logo.png'],
              ['Colorado',
               '164',
               'https://assets-sports.thescore.com/football/team/164/small_logo.png'],
              ['Utah',
               '677',
               'https://assets-sports.thescore.com/football/team/677/small_logo.png'],
              ['Arizona State',
               '58',
               'https://assets-sports.thescore.com/football/team/58/small_logo.png'],
              ['UCLA',
               '664',
               'https://assets-sports.thescore.com/football/team/664/small_logo.png'],
              ['Arizona',
               '57',
               'https://assets-sports.thescore.com/football/team/57/small_logo.png']]

POINT_MAP = {
    'Passing': {
        'TD': 4.0,
        'YDS': 0.04,
        'INT': -2.0,
    },
    'Rushing': {
        'TD': 6.0,
        'YDS': 0.1,
        'FUM(L)': -2.0
    },
    'Receiving': {
        'TD': 6.0,
        'YDS': 0.1,
        'FUM(L)': -2.0
    },
    'Kicking': {
        'PAT': 1.0,
        'Miss': -1.0,
        'Made': {
            100: 6.0,
            59: 5.0,
            49: 4.0,
            39: 3.0,
        }
    },
    'Defending': {
        'TD': 6.0,
        'INT': 2.0,
        'FUMR': 2.0,
        # 'Block': 2.0,
        # 'Safety': 2.0,
        'SACKS': 1.0,
        'PA': {
            0: 5.0,
            6: 4.0,
            13: 3.0,
            17: 1.0,
            27: 0.0,
            34: -1.0,
            45: -3.0,
            100: -5.0,
        },
        'Yards': {}
    },
    '2-PT Conversion': 2.0,
    'Kick Returning': 6.0,
    'Punt Returning': 6.0,
}

# TODO Custom Point Scalar (PPR)

POINT_SCALAR = [
    4.0,    # Passing TD        0
    0.04,   # Passing YDS       1
    -2.0,   # INT               2
    6.0,    # Receiving TD      3
    0.1,    # Receiving YDS     4
    -2.0,   # FUM(L)            5
    6.0,    # Rushing TD        6
    0.1,    # Rushing YDS       7
    1.0,    # PAT               8
    -1.0,   # Miss              9
    3.0,    # FG                10
    6.0,    # TD                11
    2.0,    # FUM(R)            12
    2.0,    # INT               13
    1.0     # SACK              14
]


# ------------------------ SCRAPE CONFERENCES ------------------------
#
# for c, l in zip(POWER_FIVE, [ACC, BIG_TWELVE, BIG_TEN, SEC, PAC_TWELVE]):
#     url = 'https://www.thescore.com/ncaaf/standings/' + c[1]
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     for t in soup.find('div', class_='standings').find_all('a'):
#         link = t['href']
#         id_ = link[link.rfind('/') + 1:]
#         team = t.div.div
#         name = team.text
#         name = name[(1 if name[1].isalpha() else 2):]
#         logo = team.span.img['src']
#         l.append([name, id_, logo])
#     print(l)
