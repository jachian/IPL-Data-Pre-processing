# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 06:51:38 2020

@author: HUB HUB
"""

#global imports
# import numpy as np
import pandas as pd


#####################################################################################################################
#
# This function is used for loading csv documents into Pandas dataframes
#
# Arguments - file_name - The name of the file to load
#           - delimiter - the character delimiter in quites that we want to divide file by.
#
# Returns - data - The pandas dataframe with the content loaded
#
##################################################################################################################
def load_data(file_name, delimit):
    
    #read into a data-frame
    data = pd.read_csv(file_name, delimiter = delimit)
    
    #convert the datframe to anumpy array and return
    #return data.values
    return data




#####################################################################################################################
#
# This function is the initial Data proeporcessing - Taking the CSV files and and colating them into a
# single document
#
# Arguments - None
#
# Returns - 
#
##############################################################################################################
def pre_process():
    
    head = ['Innings', 'Over/Ball', 'Batting', 'Batsman', 'Non-Striker', 'Bowler', 'Runs-off-bat', 'Extras', 'Wicket', 'Dismissed']
    meta_columns = ['Team', 'Team1', 'Gender', 'Season', 'Date', 'Competition', 'Match_Number', 'Venue', 'City', 'Toss_Winner', 'Toss_Decision', 'Player_of_match', 'Umpire', 'Umpire1', 'Reserve_Umpire', 'TV_Umpire', 'Match_Referee', 'Winner', 'Winner_Runs']
    
    head = head + meta_columns
    
    #create blank dataframe to put data in ###################################################
    ipl_df = pd.DataFrame(columns = head)  
    
    #load current dataframes and put content into the ipl_df dataframe #########################
    game_df = []
    meta_df = []
    
    for i in range(1136591, 1136621):
        game_df = pd.read_csv(str(i) + "-A.csv")
        meta_df = pd.read_csv(str(i) + ".csv")
        
        #get game rows
        game_rows = get_df_rows(game_df, meta_df)
        
        #insert the rows into the ipl dataframe
        index = len(ipl_df)
        
        for j in range(0, len(game_rows)):
            #now we add the row to the dataframe
            ipl_df.loc[index] = game_rows[j]
            
            index = index + 1
        
    
    for i in range(1175356, 1175373):
        game_df = pd.read_csv(str(i) + "-A.csv")
        meta_df = pd.read_csv(str(i) + ".csv")
        
        #get game rows
        game_rows = get_df_rows(game_df, meta_df)
        
        #insert the rows into the ipl dataframe
        index = len(ipl_df)
        
        for j in range(0, len(game_rows)):
            #now we add the row to the dataframe
            ipl_df.loc[index] = game_rows[j]
            
            index = index + 1
        

    for i in range(1178393, 1178432):
        game_df = pd.read_csv(str(i) + "-A.csv")
        meta_df = pd.read_csv(str(i) + ".csv")
        
        #get game rows
        game_rows = get_df_rows(game_df, meta_df)
        
        #insert the rows into the ipl dataframe
        index = len(ipl_df)
        
        for j in range(0, len(game_rows)):
            #now we add the row to the dataframe
            ipl_df.loc[index] = game_rows[j]
            
            index = index + 1
            
   
    for i in range(1181764, 1181765):
        game_df = pd.read_csv(str(i) + "-A.csv")
        meta_df = pd.read_csv(str(i) + ".csv")
        
        #get game rows
        game_rows = get_df_rows(game_df, meta_df)
        
        #insert the rows into the ipl dataframe
        index = len(ipl_df)
        
        for j in range(0, len(game_rows)):
            #now we add the row to the dataframe
            ipl_df.loc[index] = game_rows[j]
            
            index = index + 1         
    
    for i in range(1181766, 1181769):
        game_df = pd.read_csv(str(i) + "-A.csv")
        meta_df = pd.read_csv(str(i) + ".csv")
        
        #get game rows
        game_rows = get_df_rows(game_df, meta_df)
        
        #insert the rows into the ipl dataframe
        index = len(ipl_df)
        
        for j in range(0, len(game_rows)):
            #now we add the row to the dataframe
            ipl_df.loc[index] = game_rows[j]
            
            index = index + 1
            
        
        
    export_csv = ipl_df.to_csv(r'C:\Users\HUB HUB\Google Drive\Data Science\Data Mining\Project\IPL-1.csv', index = None, header=True)
    
    return ipl_df


    

def get_df_rows(game_df, meta_df):
    
    rows = []       # used to keep rows
    for i in range(0, len(game_df)):
        
        if (game_df.iloc[i][0] == "ball"):
            ro = list(game_df.iloc[i][1:11])
            
            #append the meta data
            ro.append(meta_df.iloc[0][1])
            ro.append(meta_df.iloc[1][1])
            ro.append(meta_df.iloc[2][1])
            ro.append(int(meta_df.iloc[3][1]))
            ro.append(meta_df.iloc[4][1])
            ro.append(meta_df.iloc[5][1])
            ro.append(int(meta_df.iloc[6][1]))
            ro.append(meta_df.iloc[7][1])
            ro.append(meta_df.iloc[8][1])
            ro.append(meta_df.iloc[9][1])
            ro.append(meta_df.iloc[10][1])
            ro.append(meta_df.iloc[11][1])
            ro.append(meta_df.iloc[12][1])
            ro.append(meta_df.iloc[13][1])
            ro.append(meta_df.iloc[14][1])
            ro.append(meta_df.iloc[15][1])
            ro.append(meta_df.iloc[16][1])
            ro.append(meta_df.iloc[17][1])
            ro.append(int(meta_df.iloc[18][1]))
            # ro.append(meta_df.iloc[19][1])         
            
            rows.append(ro)
        else:
            ro = game_df.iloc[i][0].split(',')
            
            ro1 = []
            ro1.append(int(ro[1]))
            ro1.append(float(ro[2]))
            ro1.append(ro[3])
            ro1.append(ro[4])
            ro1.append(ro[5])
            ro1.append(ro[6])
            ro1.append(int(ro[7]))
            ro1.append(int(ro[8]))
            ro1.append(ro[9])
            ro1.append(ro[10])
            
            #append the meta data
            ro1.append(meta_df.iloc[0][1])
            ro1.append(meta_df.iloc[1][1])
            ro1.append(meta_df.iloc[2][1])
            ro1.append(int(meta_df.iloc[3][1]))
            ro1.append(meta_df.iloc[4][1])
            ro1.append(meta_df.iloc[5][1])
            ro1.append(int(meta_df.iloc[6][1]))
            ro1.append(meta_df.iloc[7][1])
            ro1.append(meta_df.iloc[8][1])
            ro1.append(meta_df.iloc[9][1])
            ro1.append(meta_df.iloc[10][1])
            ro1.append(meta_df.iloc[11][1])
            ro1.append(meta_df.iloc[12][1])
            ro1.append(meta_df.iloc[13][1])
            ro1.append(meta_df.iloc[14][1])
            ro1.append(meta_df.iloc[15][1])
            ro1.append(meta_df.iloc[16][1])
            ro1.append(meta_df.iloc[17][1])
            ro1.append(int(meta_df.iloc[18][1]))
            # ro1.append(meta_df.iloc[19][1])           
            
            #now we append to rows
            rows.append(ro1)
        
    
    return rows



def insert_rows1(ipl_df, game_rows, meta_df):
    
    r = []
    
    for i in range(0, len(game_rows)):
        r = []
        # get the row
        row = game_rows[i]
        
        #append the meta data
        row.append(meta_df.iloc[0][1])
        row.append(meta_df.iloc[1][1])
        row.append(meta_df.iloc[2][1])
        row.append(int(meta_df.iloc[3][1]))
        row.append(meta_df.iloc[4][1])
        row.append(meta_df.iloc[5][1])
        row.append(int(meta_df.iloc[6][1]))
        row.append(meta_df.iloc[7][1])
        row.append(meta_df.iloc[8][1])
        row.append(meta_df.iloc[9][1])
        row.append(meta_df.iloc[10][1])
        row.append(meta_df.iloc[11][1])
        row.append(meta_df.iloc[12][1])
        row.append(meta_df.iloc[13][1])
        row.append(meta_df.iloc[14][1])
        row.append(meta_df.iloc[15][1])
        row.append(meta_df.iloc[16][1])
        row.append(meta_df.iloc[17][1])
        row.append(int(meta_df.iloc[18][1]))
        row.append(meta_df.iloc[19][1])
        
        #now we add the row to the dataframe
        #ipl_df.loc[len(ipl_df)] = row
        
        print("row length == " +str(len(row)))
        print(row)
    
    
    return ipl_df




#####################################################################################################################
#
# This function is the second process inf function used in the second transformation iteration to
# normalise the categorical data of the CSV sheet so that. categorical data could be visualised in addition to
# numerical data.
#
# Arguments - None
#
# Returns - An updated dataframe
#
##############################################################################################################
def pre_process1():
    
    #read the IPL csv as a dataframe    
    ipl_df = pd.read_csv("IPL-1.csv", delimiter = ",")
    
    #read each row and make updates#################################################

    head = ['Innings', 'Over/Ball', 'Batting', 'Batsman', 'Non-Striker', 'Bowler', 'Runs-off-bat', 'Extras', 'Wicket', 'Wicket_Type', 'Dismissed', 'Team', 'Team1', 'Gender', 'Season', 'Date', 'Competition', 'Match_Number', 'Venue', 'City', 'Toss_Winner', 'Toss_Decision', 'Player_of_match', 'Umpire', 'Umpire1', 'Reserve_Umpire', 'TV_Umpire', 'Match_Referee', 'Winner', 'Winner_Runs']
    

    #create blank dataframe to put data in ###################################################
    new_ipl_df = pd.DataFrame(columns = head)
    
    for i in range(0, len(ipl_df)):
        # get the content to place
        df_row = list(ipl_df.loc[i])
        
        row = df_row[0:8]
        
        if(df_row[8] == '""'):
            print("len of row 8 == " +str(len(df_row[8])))
            row.append(0)         # update 8th position
            row.append("")        # update 9th position wicket type
            row.append("")        # update 10th dismissed
        else:
            print("Type of row 8 == " +str(df_row[8]))
            row.append(1)   # update 8the position
            row.append(df_row[8])  #update 9th position - wicket type
            row.append(df_row[9])  #update 10th position - dismissed     
        
        # row.append(df_row[10:len(df_row)])
        
        for j in range(10, len(df_row)):
            row.append(df_row[j])
        
        # now insert the row into our new data frame
        print("row lenght == " +str(len(row)))
        print(row)
        print("head length == " +str(len(head)))
        print(head)
        
        new_ipl_df.loc[i] = row
    
    
    export_csv = new_ipl_df.to_csv(r'C:\Users\HUB HUB\Google Drive\Data Science\Data Mining\Project\IPL-2.csv', index = None, header=True)
    
    return new_ipl_df



#####################################################################################################################
#
# This function is the thrid process function used generate a smaller CVS with streamined win data
# normalise the categorical data of the CSV sheet so that. categorical data could be visualised in addition to
# numerical data.
#
# Arguments - None
#
# Returns - An updated dataframe
#
##############################################################################################################
def pre_process2():
    
    #read the IPL csv as a dataframe    
    ipl_df = pd.read_csv("IPL-2.csv", delimiter = ",")
    
    #read each row and make updates#################################################

    head = ['VS', 'Team', 'Team1', 'Season', 'Date', 'Competition', 'Match_Number', 'Venue', 'City', 'Toss_Winner', 'Toss_Decision', 'Player_of_match', 'Umpire', 'Umpire1', 'Reserve_Umpire', 'TV_Umpire', 'Match_Referee', 'Winner', 'Loser', 'Winner_Runs']
    

    #create blank dataframe to put data in ###################################################
    new_ipl_df = pd.DataFrame(columns = head)
    
    #set up variable to check against
    team = " "
    team1 = " "
    date = " "
    season = -2
    match_number = -2
    
    #index of new dataframe 
    j = 0
    
    for i in range(0, len(ipl_df)):

        
        test = (match_number != ipl_df.iloc[i][17])
        
        if test == True:
           print("team:- " +str(team)+ " === " +str(ipl_df.iloc[i][11]))
           print("team1:- " +str(team1)+ " === " +str(ipl_df.iloc[i][12]))
           print("date:- " +str(date)+ " === " +str(ipl_df.iloc[i][15]))
           print("season:- " +str(season)+ " === " +str(ipl_df.iloc[i][14]))
           print("match_number:- " +str(match_number)+ " === " +str(ipl_df.iloc[i][17]))
        
        
        
        if (test == True):
            entry = [ipl_df.iloc[i][11] + "_vs_" + ipl_df.iloc[i][12] + "_" + ipl_df.iloc[i][15],
                     ipl_df.iloc[i][11], 
                     ipl_df.iloc[i][12], 
                     ipl_df.iloc[i][14],     # season  
                     ipl_df.iloc[i][15],     # date
                     ipl_df.iloc[i][16],     #competition
                     ipl_df.iloc[i][17],     #match number
                     ipl_df.iloc[i][18],     #venue
                     ipl_df.iloc[i][19],     #city
                     ipl_df.iloc[i][20],     # toss_winner
                     ipl_df.iloc[i][21],     # toss_decision
                     ipl_df.iloc[i][22],     # player of the match
                     ipl_df.iloc[i][23],     # umpire
                     ipl_df.iloc[i][24],     # umpire1
                     ipl_df.iloc[i][25],     # reserve_umpire
                     ipl_df.iloc[i][26],     # TV umpire
                     ipl_df.iloc[i][27]]     # match referee
                     # ipl_df.iloc[i][28]]     # winner
            
            # Setting winner and Loser entries
            if (ipl_df.iloc[i][28] == 'tie'):
                entry.append("Tie")
                entry.append("Tie")
            else:
                if(ipl_df.iloc[i][28] == ipl_df.iloc[i][11]):     
                   entry.append(ipl_df.iloc[i][12])
                   entry.append(ipl_df.iloc[i][11])
                else:
                   entry.append(ipl_df.iloc[i][11])
                   entry.append(ipl_df.iloc[i][12])
                
            
            entry.append(ipl_df.iloc[i][29])
            
            #add the new entry to the new dataframe
            new_ipl_df.loc[j] = entry
            j = j + 1
            
            #print("Row #" +str(j - 1)+ " added == ")
            #print(str(entry))
        
            
        #end outer if
        # team = ipl_df.get_value(i, 11, takeable = True)
        # team1 = ipl_df.get_value(i, 12, takeable = True)
        # season = ipl_df.get_value(i, 14, takeable = True)
        # date = ipl_df.get_value(i, 15, takeable = True)
        match_number = ipl_df.get_value(i, 17, takeable = True)
        
        # print("Row i == " +str(i))
        # print("Row j == " +str(j))
        #print("team == " +str(team))
        #print("team1 == " +str(team1))
        #print("season == " +str(season))
        #print("date == " +str(date))
        #print("match_number == " +str(match_number))
        
    
    # end for  ###########################
    
    export_csv = new_ipl_df.to_csv(r'C:\Users\HUB HUB\Google Drive\Data Science\Data Mining\Project\IPL-3.csv', index = None, header=True)
    
    return new_ipl_df


def pre_process3():
    
    #read the IPL csv as a dataframe    
    ipl_df = pd.read_csv("IPL-2.csv", delimiter = ",")
    
    #read each row and make updates#################################################

    head = ['Innings', 'Over/Ball', 'Batting', 'Fielding', 'Batsman', 'Non-Striker', 'Bowler', 'Runs-off-bat', 'Extras', 'Wicket', 'Wicket_Type', 'Dismissed', 'VS', 'Team', 'Team1', 'Gender', 'Season', 'Date', 'Competition', 'Match_Number', 'Venue', 'City', 'Toss_Winner', 'Toss_Decision', 'Player_of_match', 'Umpire', 'Umpire1', 'Reserve_Umpire', 'TV_Umpire', 'Match_Referee', 'Winner', 'Lost', 'Winner_Runs']
    

    #create blank dataframe to put data in ###################################################
    new_df = pd.DataFrame(columns = head)
    
    for i in range(0, len(ipl_df)):
        
        entry = [ipl_df.iloc[i][0],     # innings
                 ipl_df.iloc[i][1],     # ball/over
                 ipl_df.iloc[i][2],     # batting
                 " ",                   # Fielding
                 ipl_df.iloc[i][3],     # Batsman
                 ipl_df.iloc[i][4],      # Non-striker
                 ipl_df.iloc[i][5],      # bowler
                 ipl_df.iloc[i][6],      #runs off bat
                 ipl_df.iloc[i][7],     #extras
                 ipl_df.iloc[i][8],     #wicket
                 ipl_df.iloc[i][9],     #wicket type
                 ipl_df.iloc[i][10],    #dissmissed
                 " ",                   # VS
                 ipl_df.iloc[i][11],    #team1
                 ipl_df.iloc[i][12],    #team2
                 ipl_df.iloc[i][13],    #gender
                 ipl_df.iloc[i][14],    #season
                 ipl_df.iloc[i][15],    #date
                 ipl_df.iloc[i][16],    # competition
                 ipl_df.iloc[i][17],    #match number 
                 ipl_df.iloc[i][18],    #venue
                 ipl_df.iloc[i][19],    # city
                 ipl_df.iloc[i][20],    #toss winner
                 ipl_df.iloc[i][21],    # toss dec
                 ipl_df.iloc[i][22],    # Player of match
                 ipl_df.iloc[i][23],    #umpire
                 ipl_df.iloc[i][24],    #umpire1
                 ipl_df.iloc[i][25],    #reserve umpire
                 ipl_df.iloc[i][26],    #TV umpire
                 ipl_df.iloc[i][27],    #match referee
                 ipl_df.iloc[i][28],    #winner
                 " ",                   #Lost
                 ipl_df.iloc[i][29]]     #winner runs
        
        #dd missing content to the entry array
        if(ipl_df.iloc[i][2] == ipl_df.iloc[i][11]):       #if batting == team1
            entry[3] = ipl_df.iloc[i][12]
        else:
            entry[3] = ipl_df.iloc[i][11]
        
        #set loser
        if(ipl_df.iloc[i][28] == ipl_df.iloc[i][11]):       #if winner == team1
            entry[31] = ipl_df.iloc[i][12]
        else:
            entry[31] = ipl_df.iloc[i][11]
        
        #set VS
        entry[12] = ipl_df.iloc[i][11] + '_vs_' + ipl_df.iloc[i][12] + '_s_' +str(ipl_df.iloc[i][14])+ '_m_' +str(ipl_df.iloc[i][17])
        
        #add the new entry to the new dataframe
        new_df.loc[i] = entry
        
        print("entry 1 added....")
        
    
    # end for  ###########################
    
    export_csv = new_df.to_csv(r'C:\Users\HUB HUB\Google Drive\Data Science\Data Mining\Project\IPL-2-1.csv', index = None, header=True)
    
    return new_df




def pre_process4():
    
    #read the IPL csv as a dataframe    
    ipl_df = pd.read_csv("IPL-2-1.csv", delimiter = ",")
    
    #read each row and make updates#################################################

    head = ['Innings', 'Over/Ball', 'Batting', 'Fielding', 'Batsman', 'Non-Striker', 'Bowler', 'Runs-off-bat', 'Extras', 'Wicket', 'Wicket_Type', 'Dismissed', 'VS', 'Team', 'Team1', 'Gender', 'Season', 'Date', 'Competition', 'Match_Number', 'Venue', 'City', 'Toss_Winner', 'Toss_Loser', 'Toss_Decision', 'Player_of_match', 'Umpire', 'Umpire1', 'Reserve_Umpire', 'TV_Umpire', 'Match_Referee', 'Winner', 'Lost', 'Winner_Runs']
    

    #create blank dataframe to put data in ###################################################
    new_df = pd.DataFrame(columns = head)
    
    for i in range(0, len(ipl_df)):
        
        entry = [ipl_df.iloc[i][0],     # innings
                 ipl_df.iloc[i][1],     # ball/over
                 ipl_df.iloc[i][2],     # batting
                 ipl_df.iloc[i][3],     # Batsman
                 ipl_df.iloc[i][4],      # Non-striker
                 ipl_df.iloc[i][5],      # bowler
                 ipl_df.iloc[i][6],      #runs off bat
                 ipl_df.iloc[i][7],     #extras
                 ipl_df.iloc[i][8],     #wicket
                 ipl_df.iloc[i][9],     #wicket type
                 ipl_df.iloc[i][10],    #dissmissed
                 ipl_df.iloc[i][11],    #team1
                 ipl_df.iloc[i][12],    #team2
                 ipl_df.iloc[i][13],    #gender
                 ipl_df.iloc[i][14],    #season
                 ipl_df.iloc[i][15],    #date
                 ipl_df.iloc[i][16],    # competition
                 ipl_df.iloc[i][17],    #match number 
                 ipl_df.iloc[i][18],    #venue
                 ipl_df.iloc[i][19],    # city
                 ipl_df.iloc[i][20],    #toss winner
                 ipl_df.iloc[i][21],    # toss dec
                 ipl_df.iloc[i][22],    # Player of match
                 " ",                   #umpire
                 ipl_df.iloc[i][23],    #umpire1
                 ipl_df.iloc[i][24],    #reserve umpire
                 ipl_df.iloc[i][25],    #TV umpire
                 ipl_df.iloc[i][26],    #match referee
                 ipl_df.iloc[i][27],    #winner
                 ipl_df.iloc[i][28],
                 ipl_df.iloc[i][29],
                 ipl_df.iloc[i][30],
                 ipl_df.iloc[i][31],
                 ipl_df.iloc[i][32]]
        
        
        #dd missing content to the entry array
        if(ipl_df.iloc[i][13] == ipl_df.iloc[i][22]):       #if batting == team1
            entry[23] = ipl_df.iloc[i][14]
        else:
            entry[23] = ipl_df.iloc[i][13]
        
        
        #add the new entry to the new dataframe
        new_df.loc[i] = entry
        
        print("entry 1 added....")
        
    
    # end for  ###########################
    export_csv = new_df.to_csv(r'C:\Users\HUB HUB\Google Drive\Data Science\Data Mining\Project\IPL-2-2.csv', index = None, header=True)
    
    return new_df




#####################################################################################################################
#
# This function is the thrid process function used generate a smaller CVS with streamined win data
# normalise the categorical data of the CSV sheet so that. categorical data could be visualised in addition to
# numerical data.
#
# Arguments - None
#
# Returns - An updated dataframe
#
##############################################################################################################
def pre_process5():
    
    #read the IPL csv as a dataframe    
    ipl_df = pd.read_csv("IPL-3.csv", delimiter = ",")
    
    #read each row and make updates#################################################

    head = ['VS', 'Team', 'Team1', 'Season', 'Date', 'Competition', 'Match_Number', 'Venue', 'City', 'Toss_Winner', 'Toss_Loser', 'Toss_Decision', 'Player_of_match', 'Umpire', 'Umpire1', 'Reserve_Umpire', 'TV_Umpire', 'Match_Referee', 'Winner', 'Loser', 'Winner_Runs']
    

    #create blank dataframe to put data in ###################################################
    new_ipl_df = pd.DataFrame(columns = head)
    
    
    for i in range(0, len(ipl_df)):
        entry = [ipl_df.iloc[i][0],      # VS
                 ipl_df.iloc[i][1],      # Team 
                 ipl_df.iloc[i][2],      # Team1 
                 ipl_df.iloc[i][3],      # season  
                 ipl_df.iloc[i][4],      # date
                 ipl_df.iloc[i][5],      #competition
                 ipl_df.iloc[i][6],      #match number
                 ipl_df.iloc[i][7],      #venue
                 ipl_df.iloc[i][8],      #city
                 ipl_df.iloc[i][9],      # toss_winner
                 " ",                    # toss_loser
                 ipl_df.iloc[i][10],     # toss_decision
                 ipl_df.iloc[i][11],     # player of the match
                 ipl_df.iloc[i][12],     # umpire
                 ipl_df.iloc[i][13],     # umpire1
                 ipl_df.iloc[i][14],     # reserve_umpire
                 ipl_df.iloc[i][15],     # TV umpire
                 ipl_df.iloc[i][16],     # match referee
                 ipl_df.iloc[i][17],     # winner
                 ipl_df.iloc[i][18],     # Loser
                 ipl_df.iloc[i][19]]     # Winner runs
        
        if(ipl_df.iloc[i][1] == ipl_df.iloc[i][9]):
            entry[10] = ipl_df.iloc[i][2]
        else:
            entry[10] = ipl_df.iloc[i][1]
        
        
        new_ipl_df.loc[i] = entry
        # end for  ###########################
    
    export_csv = new_ipl_df.to_csv(r'C:\Users\HUB HUB\Google Drive\Data Science\Data Mining\Project\IPL-3-1.csv', index = None, header=True)
    
    return new_ipl_df


        

    
    

    
    
            
    

