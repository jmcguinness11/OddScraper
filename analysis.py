#!/usr/bin/env python2.7

from itertools import tee
import pandas as pd
import numpy as np

# read in cbb data
res_df = pd.read_csv('ncb_16_17.csv')
it = res_df.iterrows()
games = []
for team_tup, opp_tup in zip(it, it):
	team = team_tup[1]
	opp = opp_tup[1]
	#skip games with no moneyline info
	try:
		tml = int(team.ML)
		oml = int(opp.ML)
	except:
		continue
	game = []
	if tml > oml:
		game.append(team.Team)
		game.append(opp.Team)
		game.append('V')
		game.append(int(team.ML))
		game.append(int(opp.ML))
		game.append(team.Final)
		game.append(opp.Final)
		game.append(team.Final > opp.Final)
	else:
		game.append(opp.Team)
		game.append(team.Team)
		game.append('H')
		game.append(int(opp.ML))
		game.append(int(team.ML))
		game.append(opp.Final)
		game.append(team.Final)
		game.append(opp.Final > team.Final)
	games.append(game)

gdf_cols = ["und", "fav", "loc", "ML", "oppML", "und_score", "fav_score", "upset"]
games_df = pd.DataFrame(games, columns=gdf_cols) 

#percent of games that are upsets
num_upset = games_df.upset.sum()
print num_upset, games_df.size, 1.*num_upset/games_df.size

#percent of games w/ML >= 300 that are upsets
big_spread_games_df = games_df[games_df.ML >= 300]
num_upset = big_spread_games_df.upset.sum()
print num_upset, big_spread_games_df.size, 1.*num_upset/big_spread_games_df.size

#betting $100 on all games w/ML >= 300
running_total = 0
rt2 = 0
for game in big_spread_games_df.iterrows():
	game = game[1]
	if not game.upset:
		running_total -= 100
		rt2 += 100/(-1*game.oppML/100)
	else:
		running_total += game.ML
		rt2 -= 100
print running_total, rt2

#upset analysis
upset_df = games_df[games_df.upset]
