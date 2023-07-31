import random


def test_del_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 1:
        app.groups.add_new_group("my gr")
    old_list = app.groups.get_group_list()
    app.groups.delete_group(0)
    new_list = app.groups.get_group_list()
    old_list.remove(old_list[0])
    assert sorted(old_list) == sorted(new_list)
