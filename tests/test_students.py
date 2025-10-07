from data.students import STUDENTS

def test_sorted_and_unique():
    # sin duplicados y ordenado alfabéticamente
    assert STUDENTS == sorted(set(STUDENTS))

def test_capitalized():
    # cada nombre debe empezar con mayúscula
    assert all(len(s) > 0 and s[0].isupper() for s in STUDENTS)
