import re


def parse_cookie(query: str) -> dict:
    params = re.findall(r'([^=&?;]+)=([^&;]+)', query)
    res = dict()
    for key, val in params:
        res.setdefault(key, val)
    return res


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}