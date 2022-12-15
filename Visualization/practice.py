import curses
from curses import wrapper


def main(main_screen):

    main_screen.addstr("Press any key...")
    main_screen.refresh()

    c = main_screen.getch()

    curses.endwin()

    # Convert the key to ASCII and print ordinal value
    print("You pressed %s which is keycode %d." % (chr(c), c))

    curses.nocbreak()   # Turn off cbreak mode
    curses.echo()       # Turn echo back on
    curses.curs_set(1)  # Turn cursor back on
    # If initialized like `my_screen = curses.initscr()`

    #raise Exception


wrapper(main)
