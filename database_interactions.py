import shelve
import string
import random


def add_to_db(lindy_class):
    letters = string.ascii_lowercase
    key = ''.join(random.choice(letters) for i in range(8))
    lindy_class.key = key
    # print(lindy_class.key)
    with shelve.open('listing_db') as db:
        db[key] = lindy_class


def remove_from_db(entry_id):
    with shelve.open('listing_db') as db:
        db.pop(entry_id)


def get_lindy_items():
    lindy_item_list = []
    with shelve.open('listing_db') as db:
        keys = list(db.keys())
        # print(keys)
        if keys is not None:
            for k in keys:
                lindy_item_list.append(db[k])
    return lindy_item_list


def view_db():
    keys = None
    with shelve.open('listing_db') as db:
        keys = list(db.keys())
        # print(keys)
        for k in keys:
            lindy_item = db[k]
            lindy_item.print_stuff()


def update_entry(lindy_obj):
    key = lindy_obj.key
    with shelve.open('listing_db') as db:
        db[key] = lindy_obj
