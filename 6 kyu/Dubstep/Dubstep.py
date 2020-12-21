# Python 3.8, 20 March 2020


def song_decoder(song):

    return " ".join(i for i in song.split("WUB") if i != "")
