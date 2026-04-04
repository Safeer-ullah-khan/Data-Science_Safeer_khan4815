import pandas as pd
songs={'album':["Thriller","Back in black","The dark side of moon","The Bodygaurd","Bat out of hell"],
       'Released':[1982,1980,1973,1992,1973],
       'length':["00:42:19","00:42:11","00:42:49","00:57:44","00:46:33"]}
song_frame=pd.DataFrame(songs)
# print(song_frame)
# y=song_frame['Released']
# print(y)
# print(song_frame.iloc[2])#access third row by position through iloc function
# print(song_frame.loc[1])#acces second row by label through iloc function
# print(song_frame[['album','length']])#select column
# print(song_frame[1:4])#using range slect row
# print(song_frame['Released'].unique())
print(song_frame[song_frame['Released']>1980])#uning conditional statements