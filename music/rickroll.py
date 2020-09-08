import microbit
import music

notes = [
    'r4:4', 'bb3:4', 'c4:4', 'db:4', 'eb:4', 'c:6', 'bb3:2', 'ab:16',
    'r4:12', 'bb3:4', 'c4:4', 'db4:4', 'bb3:4', 'r4:4', 'ab3:4', 'ab4:4',
    'ab4:4', 'eb4:16', 'r4:4', 'bb3:4',
    'bb3:4', 'c4:4', 'db4:4', 'eb4:4', 'r4:4', 'c4:4',
    'bb3:4', 'bb', 'ab:12', 'r4:8', 'bb3:4',
    'bb', 'c4', 'db', 'bb3', 'ab', 'eb4', 'eb',
    'eb', 'f', 'eb:8', 'r4:8', 'db:24',
    'eb:4', 'f', 'db', 'eb', 'eb',
    'eb', 'f', 'eb', 'ab3', 'ab3:12', 'r4:4',
    'r4:8', 'bb3:4', 'c4', 'dd', 'bb3:8', 'eb4:4',
    'f', 'eb:8', 'r4:4', 'ab3:2', 'bb', 'dd4', 'bb3', 'f4:4', 'f:6',
    'eb:8', 'r4:4', 'ab3:2', 'bb1', 'db4:2', 'bb3', 'eb4:4', 'eb:6',
    'db:4', 'c', 'bb3', 'ab:2', 'bb1', 'db4:2', 'bb3', 'db4:8',
    'eb4:4', 'c:8', 'ab3:4', 'r4:4', 'ab3', 'eb4', 'r4:4', 'db:8',
    'r4:8', 'ab3:4', 'bb:2', 'db4', 'bb3:4', 'f4', 'f:6',
    'eb4:8', 'r4:4', 'ab3', 'bb:2', 'db4', 'bb3:4', 'ab4', 'c',
    'db:6', 'c:2', 'bb3:4', 'ab:2', 'bb:1', 'db4:2', 'bb3:4', 'db4:8', 'eb:4',
    'c:6', 'bb3:2', 'ab:8', 'ab:4', 'eb4:8', 'db:24'
]
music.set_tempo(ticks=8)
music.set_tempo(bpm=113)


while True:
    if microbit.button_a.is_pressed():
        music.play(notes)
        
#press button a to play
