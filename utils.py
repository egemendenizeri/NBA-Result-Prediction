import numpy as np
import sqlite3
import pandas as pd

teams = ["CHA","PHI","TOR","BOS","CLE","IND","WSH","MIL","MIA","DET","NY","CHI","ORL","BKN","ATL","HOU","GS","POR","NO","MIN","SA","OKC","DEN","LAC","UTA","LAL","SAC","DAL","PHX","MEM"]
dic = {"atl":"Atlanta","bkn": "Brooklyn" ,"bos": "Boston", "cha":"Charlotte", "chi":"Chicago", "cle": "Cleveland", "dal": "Dallas", "den": "Denver", "det":"Detroit","gs":"Golden State", "hou": "Houston", "ind":"Indiana","lac":"LA", "lal": "Los Angeles","mem": "Memphis","mia":"Miami","mil":"Milwaukee","min":"Minnesota","no":"New Orleans","ny":"New York","okc":"Oklahoma City","orl":"Orlando","phi":"Philadelphia","phx":"Phoenix","por":"Portland","sa":"San Antonio","sac":"Sacramento","tor":"Toronto","utah":"Utah","uta":"Utah","wsh":"Washington" }

def get_schedule(cursor,team):
    # This method gets the schedule of a team from schedule_scores.db
    # It requires a cursor connected to the schedule_scores.db
    # And it requires the name of the team whose schedule wanted to be fetched

    cursor.execute("SELECT * FROM {}".format(team.lower()))

    # Method return the data as a list
    return cursor.fetchall()

def get_all_schedules(cursor):
    # This method gets the schedule of each team from schedule_scores.db
    # It requires the cursor connected to the schedule_scores.db

    schedules = {}
    for team in teams:
        schedules[team.lower()] = get_schedule(cursor,team)

    # Method return the data as a list
    return schedules

def get_stats(cursor,team):
    # This method gets the stats of a team from team_stats.db
    # It requires a cursor connected to the team_stats.db
    # And it requires the name of the team whose stats wanted to be fetched

    cursor.execute("SELECT * FROM {}".format(team.lower()))

    # Method return the data as a list
    return cursor.fetchall()

def get_all_stats(cursor):
    # This method gets the schedule of each team from schedule_scores.db
    # It requires the cursor connected to the schedule_scores.db

    stats = {}
    for team in teams:
        stats[team.lower()] = get_stats(cursor,team)
    
    # Method return the data as a list
    return stats

def get_win_ratio(team_schedule,date):
    # This method returns the win ratio of a team at a specific date (works only for a date team has a game)
    """
    team_schedule_df = pd.DataFrame(team_schedule, columns=['Game', 'Date', 'Opponent','Home/Away(1/0)','Score','TotalScore'])
    team_schedule_df['Date'] = pd.to_datetime(team_schedule_df['Date'],format='%b %d %Y')

    row = team_schedule_df[team_schedule_df['Date'] == pd.to_datetime(date,format='%b %d %Y')]
    game_played = row["Game"].values[0]"""

    # First column of team_schedule is game number. Ex. Game 46 is 46th game of the season.
    game_played = list(filter(lambda x: x[1]==date,team_schedule))[0][0]

    # To get a meaningful Win/lose ration it is assumed that at least 15 games are needed.
    if game_played <15:
        game_played = 15

    win = 0
    for row in team_schedule[:game_played]:
        # row[-2] indicates the score of the game, Ex. -19 means the team loses the game by 19
        if row[-2]>0:
            win+=1

    return win/game_played






