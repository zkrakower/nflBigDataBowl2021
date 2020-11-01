# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:41:10 2020

@author: zmkra

@description: Takes the raw weekly tracking data files and splits 
    and saves them as files segmented by game. Purpose is
    to make future data loading more efficient/light-weight.
"""

# Libraries
import pandas as pd
import os

def process_weekFile2gameFile(nflDir, weeks=list(range(1,18))):        
    for w in weeks:
        # Set up landing directory for this week's games
        wkDir = nflDir+"gameFiles\\gamesWeek"+str(w)
        os.makedirs(wkDir)
        # Process this weeks file into seperate game files
        wkFile = nflDir+"week"+str(w)+".csv"
            # reading in week csv...
        df_week = pd.read_csv(wkFile)
            # get the game IDs in this week's file...
        gameIDs = list(set(df_week['gameId']))
        print("Processing Week "+str(w))
        # Process each game, save each to new csv
        for g in gameIDs:
            df_game = df_week[df_week['gameId'] == g]
            df_game.to_csv(wkDir+"\\game_"+str(g)+".csv", index=False)
            print("     Saved file for gameID: "+str(g))

# Local directory and files for tracking data
nfl_folder = "C:\\Users\\zmkra\\Documents\\NFL Kaggle\\nfl-big-data-bowl-2021\\"
process_weekFile2gameFile(nflDir=nfl_folder, weeks=list(range(1,18)))



# Adding dialog box for directory selection
#import tkinter as tk
#from tkinter import filedialog
#root = tk.Tk()
#root.withdraw()
#dir_path = filedialog.askdirectory()
