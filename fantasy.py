"""
Iain Muir, iam9ez

"""

from cfbFantasyApp.constants import POWER_FIVE, ACC, SEC, PAC_TWELVE, BIG_TEN, BIG_TWELVE
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


class League:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.member_info = {}

        self.year = 2020    # TODO Make Dynamic
        self.week = self.current_week()

    def standings(self):
        pass

    @staticmethod
    def draft():
        # d = Draft()
        pass

    def current_week(self):
        today = datetime.today()
        url = 'https://api.collegefootballdata.com/calendar?year=' + str(self.year)
        schedule = requests.get(url=url).json()
        for week in schedule:
            start = datetime.strptime(week['firstGameStart'][:10], '%Y-%m-%d')
            end = datetime.strptime(week['lastGameStart'][:10], '%Y-%m-%d')
            if start < today < end:
                return week['seasonType'], week['week']

    def send_invite(self):
        pass


class Draft:
    def __init__(self):
        pass

    def upload_results(self):
        pass


class Member:
    def __init__(self):
        pass

    def member_history(self):
        pass


class FantasyTeam:
    def __init__(self):
        pass


class FantasyPlayer:
    def __init__(self):
        pass


class FreeAgent(FantasyPlayer):
    def __init__(self):
        FantasyPlayer.__init__(self)

    def available_by_pos(self):
        """
        Query each individual position
        """
        pass


# def loop_players(player, c, team_name, color):
#     link = player['href']
#     id_ = link[link.rfind('/') + 1:]
#     name = player.find('div', class_='TeamRosterPlayer__name--2BQjT').text
#     number = player.find('div', class_='TeamRosterPlayer__number--2l0W1').text
#     position = player.find('div', class_='TeamRosterPlayer__position--232Fk').text
#
#     try:
#         head_shot = player.div.span.div.span.img['src']
#     except AttributeError:
#         head_shot = player.div.span.div.div.div.text
#
#     return [c, team_name, name, number, position, id_, head_shot, color]
#
#
# def loop_teams(conf, team):
#     team_name = team[0]
#     url = 'https://www.thescore.com/ncaaf/teams/' + team[1] + '/roster'
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     roster = soup.find('div', class_='TeamRoster__container--1J_hp')
#     color = roster.find('div', class_='PlayerHeadshot__headshotBackground--1uvpo')['style']
#
#     return list(map(lambda p: loop_players(p, conf, team_name, color), roster.find_all('a')))
#
#
# def update_rosters2():
#     """
#     Scrape all rosters of every team in the Power Five Conferences
#
#     EXPENSIVE: Two-minute runtime (7,500 players)
#     """
#
#     start = time.time()
#
#     players = []
#     for conference, info in zip([ACC, SEC, PAC_TWELVE, BIG_TEN, BIG_TWELVE], POWER_FIVE):
#         c = info[0]
#         rosters = list(map(lambda t: loop_teams(c, t), conference))
#         players += rosters
#
#     df = pd.DataFrame(players)
#     df.to_csv('rosters_copy.csv')
#
#     print('Finished in %s seconds' % round(time.time() - start, 4))


def update_rosters():
    """
    Scrape all rosters of every team in the Power Five Conferences

    EXPENSIVE: Two-minute runtime (7,500 players)
    """

    start = time.time()

    players = []
    for conference, info in zip([ACC, SEC, PAC_TWELVE, BIG_TEN, BIG_TWELVE], POWER_FIVE):
        c = info[0]
        for team in conference:
            team_name = team[0]
            url = 'https://www.thescore.com/ncaaf/teams/' + team[1] + '/roster'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            roster = soup.find('div', class_='TeamRoster__container--1J_hp')
            color = roster.find('div', class_='PlayerHeadshot__headshotBackground--1uvpo')['style']
            for player in roster.find_all('a'):
                link = player['href']
                id_ = link[link.rfind('/') + 1:]
                name = player.find('div', class_='TeamRosterPlayer__name--2BQjT').text
                number = player.find('div', class_='TeamRosterPlayer__number--2l0W1').text
                position = player.find('div', class_='TeamRosterPlayer__position--232Fk').text

                try:
                    head_shot = player.div.span.div.span.img['src']
                except AttributeError:
                    head_shot = player.div.span.div.div.div.text

                players.append([c, team_name, name, number, position, id_, head_shot, color])

    df = pd.DataFrame(players)
    df.to_csv('rosters_copy.csv')

    print('Finished in %s seconds' % round(time.time() - start, 4))


league = League('LOEG')
print(league.name, league.week)
