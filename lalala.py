import sys, time
import threading
from playsound import playsound

write = sys.stdout.write
print('\n   ')


def hand():
    timing = [("  ", 4), ("👊", 0.5), ("👍", 0.4), ("👎", 0.4), ("✋", 0.5), ("✌️", 0.5), ("🤞", 0.5), ("👌", 0.5)
        , ("🤙", 0.5), ("🖖", 0.5)]
    for s, t in timing:
        print(s)
        time.sleep(t)
        sys.stdout.write("\033[F")


if __name__ == '__main__':
    threading.Thread(target=playsound, args=('Y2K-Lalala.mp3',)).start()
    hand()
