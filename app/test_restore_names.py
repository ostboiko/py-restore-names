from app.restore_names import restore_names


def test_restore_names_with_none_first_names() -> str:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Alice",
            "last_name": "Johnson",
            "full_name": "Alice Johnson",
        },
    ]

    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Alice",
            "last_name": "Johnson",
            "full_name": "Alice Johnson",
        },
    ]
