# https://online.rockarsenal.ru/rockwotalk?9288
# https://prod-3-90-240-207.wostreaming.net/foxnewsradio-foxnewsradioaac-imc?session-id=27881d84449d0ac4c1a13fcf9f4dc5ef
import vlc

# URL of the radio station you want to play
radio_url = "https://prod-3-90-240-207.wostreaming.net/foxnewsradio-foxnewsradioaac-imc?session-id=27881d84449d0ac4c1a13fcf9f4dc5ef"

# create a VLC instance
vlc_instance = vlc.Instance('--no-xlib')

# create a new media player
player = vlc_instance.media_player_new()

# create a new media object with the URL
media = vlc_instance.media_new(radio_url)

# set the media player's media object
player.set_media(media)

# play the media
player.play()

# wait for the user to stop the program
input("Press enter to stop playback...")

# stop the media player
player.stop()
