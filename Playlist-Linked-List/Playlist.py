from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  def add_song(self, title):
    newest_song = Song(title)
    newest_song.set_next_song(self.__first_song)
    self.__first_song = newest_song


  def find_song(self, title):
    current_song = self.__first_song
    index = 0

    while current_song != None:
      if current_song.get_title() == title:
        return index
      if current_song.get_title() != title:
        index += 1
        current_song = current_song.get_next_song()
    index = -1
    return index

  def remove_song(self, title):
    previous = None
    current = self.__first_song
    while current != None:
      if current.get_title() != title:
        previous = current
        current = current.get_next_song()
      else:
        ##Top Case
        if previous == None:
          self.__first_song = None
          print("First Song selected and removed.")
          break
        ##Bottom Case
        elif current.get_next_song == None:
          previous.set_next_song(None)
          print("Last Song selected and removed.")
          break
        else:
        #Middle Case
          previous.set_next_song(current.get_next_song())
          print("Centered Song selected and removed.")
          break

  def length(self):
    length = 0
    current = self.__first_song

    while current != None:
      length += 1
      current = current.get_next_song()
    return length

  def print_songs(self):
    current = self.__first_song
    index = 1
    while current != None:
      print( f'{str(index)}. {current}')
      current = current.get_next_song()
      index += 1


  