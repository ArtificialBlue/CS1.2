from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  def add_song(self, title):
    newest_song = Song(title)
    newest_song.set_next_song(self.__first_song)
    self.__first_song = newest_song



  # TODO: Create a method called find_song that searches for whether a song exits
  # in the playlist and returns its index. The method has one parameters, title, 
  # which is the title of the song to be searched for. If the song is found, 
  # return its index.

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


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

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
          previous.set_next_song(current.get_next_song())
          print("Centered Song selected and removed.")
          break

        


        


  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    length = 0
    current = self.__first_song

    while current != None:
      length += 1
      current = current.get_next_song()
    return length



  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current = self.__first_song
    index = 1
    while current != None:
      print( f'{str(index)}. {current}')
      current = current.get_next_song()
      index += 1


  