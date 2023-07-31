

def test_add_group(app):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group("my gr")
    new_list = app.groups.get_group_list()
    old_list.append("my gr")
    assert sorted(old_list) == sorted(new_list)
