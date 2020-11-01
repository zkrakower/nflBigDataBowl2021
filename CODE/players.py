import pandas as pd

data_file = "/tmp/bleh/gamesWeek1/game_2018090600.csv"
data = pd.read_csv(data_file)

football_data = data[data['displayName'] == 'Football']
play_football_data = football_data[football_data.playId == 4472]

pass_flight_data = []
pass_in_air = 0
for index, row in play_football_data.iterrows():
    # check if the pass arrives before attempting to add it so we dont include non-flight data
    if row['event'] == 'pass_arrived':
        pass_in_air = 0

    # add if the ball is in the air
    if pass_in_air:
        pass_data = {'time':row.time,'x':row.x, 'y':row.y, 'speed':row.s, 'acceleration':row.a}
        pass_flight_data.append(pass_data)

    # check if the pass has started (doing this now so we dont include stationary data)
    if row['event'] == 'pass_forward':
        pass_in_air = 1

print pass_flight_data