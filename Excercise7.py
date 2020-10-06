#Excercise 7
"""
Define a class called Songs, it will show the lyrics of a song. Its __init__()
method should have two arguments:self and lyrics. lyrics is a list. Inside your
class create a method called sing_me_a_song that prints each element of
lyrics on his own line. Define a variable:
Call the sing_me_songmehod on this variable.
"""

class Songs:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in range(len(self.lyrics)):
            print(self.lyrics[i])



happy_bday = Songs(["May god bless you, ","Have a sunshine on you,","Happy Birthday to you !"])

happy_bday.sing_me_a_song()