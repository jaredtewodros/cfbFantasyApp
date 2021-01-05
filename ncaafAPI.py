"""
Iain Muir, iam9ez

ENDPOINTS:
explored
    • /roster
    • /games/players (game stats)
look into
    • /calendar (week starts/end dates  | includes postseason – weeks reset)
    • /games (games and results – by week or for the season | by team or by conference
    • /stats/player/season (season totals)
    • /teams (team info – id, name, abbrev, conf, div, color, logos
    • /stats/season (team stat totals – useful for ranking...?)

"""

from cfbFantasyApp.constants import POWER_FIVE_TEAMS, POINT_SCALAR
# from pprint import pprint
import pandas as pd
import requests
import time
import os

week = 14
year = 2020


def all_players():
    """
    ~ 10 second run-time
    """
    start = time.time()

    if not os.path.exists('/Users/iainmuir/PycharmProjects/Desktop/fantasyCollegeFootball/rosters2.csv'):
        rosters = []
        for t in POWER_FIVE_TEAMS:
            name = t.replace(' ', '%20').replace('&', '%26')
            url = 'https://api.collegefootballdata.com/roster?team=' + name + '&year=' + str(year)
            r = requests.get(url=url)
            if r.status_code == 200:
                data = r.json()
                list(map(lambda p: rosters.append([p['team'], p['first_name'] + ' ' + p['last_name'], p['id'],
                                                   p['position'], p['jersey'], p['year'], p['height'], p['weight'],
                                                   p['home_city'], p['home_state'], p['home_country']])
                         if p['first_name'] is not None
                         else [None],
                         data[:-1]))

                # df = pd.DataFrame(roster)
                # master.append(df, ignore_index=True)

            else:
                continue

        df = pd.DataFrame(
            rosters,
            columns=['team', 'name', 'id', 'position', 'jersey', 'team', 'height', 'weight',
                     'homeCity', 'homeState', 'homeCountry'],
        )

        df.to_csv('rosters2.csv')

    else:
        df = pd.read_csv('/Users/iainmuir/PycharmProjects/Desktop/fantasyCollegeFootball/rosters2.csv')
        print(df)

    print('Finished in %s seconds' % round(time.time() - start, 4))


def loop_stats(matrix, categories):
    """

    :argument
    :argument
    :return

    """

    for category in categories:  # n = 9
        for type_ in category['types']:
            if category['name'] == 'punting':
                break
            elif category['name'] in ['defensive', 'puntReturns', 'kickReturns', 'interceptions']:
                index = 11 if type_['name'] == 'TD' else 14 if type_['name'] == 'SACKS' else None
                if index is not None:
                    matrix['DST'][index] += sum([float(a['stat']) for a in type_['athletes']])
                index = None
            elif category['name'] == 'receiving':
                index = 3 if type_['name'] == 'TD' else 4 if type_['name'] == 'YDS' else None
            elif category['name'] == 'rushing':
                index = 6 if type_['name'] == 'TD' else 7 if type_['name'] == 'YDS' else None
            elif category['name'] == 'passing':
                index = 0 if type_['name'] == 'TD' else 1 if type_['name'] == 'YDS' else 2 if type_['name'] == 'INT' \
                    else None
            elif category['name'] == 'fumbles':
                index = 5 if type_['name'] == 'LOST' else 12 if type_['name'] == 'REC' else None
                if index == 12:
                    matrix['DST'][index] += sum([float(a['stat']) for a in type_['athletes']])
                    index = None
            elif category['name'] == 'kicking':
                for a in type_['athletes']:
                    if type_['name'] == 'XP':
                        xp = a['stat']
                        makes = float(xp[:xp.find('/')])
                        matrix[a['name']][8] = makes
                        matrix[a['name']][9] += float(xp[xp.find('/') + 1:]) - makes
                    elif type_['name'] == 'FG':
                        fg = a['stat']
                        makes = float(fg[:fg.find('/')])
                        matrix[a['name']][8] = makes
                        matrix[a['name']][9] += float(fg[fg.find('/') + 1:]) - makes
                index = None
            else:
                print(category['name'])
                print('Unrecognized Category \n Exiting now...')
                exit(0)

            if index is not None:
                for a in type_['athletes']:
                    try:
                        matrix[a['name'].replace(' Jr.', '').replace(' IV', '').
                               replace(' III', '').replace(' II', '')][index] = float(a['stat'])
                    except KeyError:
                        try:
                            matrix[a['name'].replace(' Jr.', '').replace(' IV', '').
                                   replace(' III', '').replace(' II', '')] = [0 for _ in range(len(POINT_SCALAR))]
                            matrix[a['name'].replace(' Jr.', '').replace(' IV', '').
                                   replace(' III', '').replace(' II', '')][index] = float(a['stat'])
                        except KeyError:
                            if a['name'] == ' Team' or index == 5:
                                continue
                            print(category['name'], type_['name'], index, a['name'])

            else:
                continue

        # print(category['name'])
        # for t in category['types']:                    # n = 3-5
        #     print('\t' + t['name'])
        #     for a in t['athletes']:                   # n = 1-15
        #         print('\t\t' + a['name'])
        #         print('\t\t' + a['stat'])

    return matrix


def game_stats(df, team):
    """
    RESPONSE:

    [
        {
            'id': #
            'teams': [
                        'school': '...'
                        'conference': '...'
                        'homeAway': '...'
                        'points': #
                        'categories': [
                                           {
                                                'name': ('defensive', 'fumbles', 'punting', 'kicking', 'puntReturns',
                                                         'kickReturns', 'receiving', 'rushing', 'passing')
                                                'types': [
                                                              {
                                                                   'name': '...'
                                                                   'athletes: [
                                                                                   'id': '#'
                                                                                   'name': '..."
                                                                                   'stat': '..."
                                                                              ]
                                                              }
                                                         ]
                                           }
                                      ]

                     ]
        }
    ]

    """

    url = 'https://api.collegefootballdata.com/games/players?year=' + str(year) + '&week=' + str(week) + \
          '&seasonType=regular&team=' + team.replace(' ', '%20').replace('&', '%26')
    r = requests.get(url=url)
    data = r.json()[0]

    team1, team2 = data['teams'][0]['school'], data['teams'][1]['school']

    # TODO Figure out naming issues
    #       • Jr. / III
    #       • CamelCase names (ex. McDonald)

    names1 = [name.strip().replace(' Jr.', '').replace(' IV', '').replace(' III', '').replace(' II', '').title()
              for name in list(df.query('team == "' + team1 + '"').name)]
    names2 = [name.strip().replace(' Jr.', '').replace(' IV', '').replace(' III', '').replace(' II', '').title()
              for name in list(df.query('team == "' + team2 + '"').name)]

    # names1 = list(df.query('team == "' + team1 + '"')['name'].str.strip().
    #               replace('Jr.', '').replace('IV', '').replace('III', '').replace('II', ''))
    # names2 = list(df.query('team == "' + team2 + '"')['name'].str.strip().
    #               replace('Jr.', '').replace('IV', '').replace('III', '').replace('II', ''))
    print(names1)
    print(names2)

    matrix1 = dict(zip(names1, [[0 for _ in range(len(POINT_SCALAR))] for _ in range(len(names1))]))
    matrix1['DST'] = [0 for _ in range(len(POINT_SCALAR))]
    matrix2 = dict(zip(names2, [[0 for _ in range(len(POINT_SCALAR))] for _ in range(len(names2))]))
    matrix2['DST'] = [0 for _ in range(len(POINT_SCALAR))]

    matrix1 = loop_stats(matrix1, data['teams'][0]['categories'])
    matrix2 = loop_stats(matrix2, data['teams'][1]['categories'])

    tm1_matrix = {}
    tm2_matrix = {}

    for pair1, pair2 in zip(matrix1.items(), matrix2.items()):
        k1, v1 = pair1
        k2, v2 = pair2

        tm1_matrix[k1] = (round(sum(list(map(lambda stat, scale: stat * scale, v1, POINT_SCALAR))), 2), v1)
        tm2_matrix[k2] = (round(sum(list(map(lambda stat, scale: stat * scale, v2, POINT_SCALAR))), 2), v2)

    return tm1_matrix, tm2_matrix


roster_df = pd.read_csv('/Users/iainmuir/PycharmProjects/Desktop/fantasyCollegeFootball/rosters2.csv')
m1, m2 = game_stats(roster_df, 'Notre Dame')
try:
    print(m2['Ian Book'])
except KeyError:
    print(m1['Ian Book'])
