

def test_first_group(app):
    app.open_main_page()
    app.group.open_page()
    app.group.delete_first()
    app.group.return_to_groups_page()
