import requests
from lindy_class import LindyListing
import database_interactions as dbi


def add_listing():
    url = input('please input URL of listing: ')  # Python 3
    try:
        lindy = LindyListing(url)
        lindy.print_stuff()
        lindy.nickname = input('please set a nickname or hit enter to leave blank: ')  # Python 3

        dbi.add_to_db(lindy)
    except ValueError:
        print('ERROR: invalid url --PROGRAM STOPPED')


def refresh_all():
    list_ings = dbi.get_lindy_items()
    for lindy in list_ings:
        lindy.update()
        dbi.update_entry(lindy)


if __name__ == "__main__":
    while True:
        text = input('would you like to view(v) add(a), delete(d), refresh(r) or quit(q): ')
        if text == 'q':
            break
        if text == 'v':
            dbi.view_db()
        if text == 'r':
            refresh_all()
        if text == 'a':
            add_listing()
        if text == 'd':
            my_id = input('please enter the entry id to remove from list: ')
            dbi.remove_from_db(my_id)

