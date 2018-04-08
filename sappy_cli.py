from sappy import Decoder
import time
import argparse


def main():


    p = argparse.ArgumentParser()

    p.add_argument(
        'path',
        help="path to the ROM to play",
        # dest="song_path"
    )
    p.add_argument(
        'song_table',
        help="address of song table in rom. must be a hexadecimal number",
        # dest="song_table"
    )
    p.add_argument(
        'song_num',
        # dest="song_num"
    )
    args = p.parse_args()

    # exit()
    dec = Decoder()
    
    print("Playing: ", args.path.split('\\')[-1], " Song number: ", args.song_num)
    print()
    print()

    try:
        dec.play_song(
            args.path,
            int(args.song_num),
            int(args.song_table, 16)
        )


    except KeyboardInterrupt:
        print("Exiting...")
        dec.stop_song()
        exit(0)
if __name__ == "__main__":
    main()
