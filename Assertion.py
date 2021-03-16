import re


def parse1(query: str) -> dict:
    params = re.findall(r'([^?=&]+)=([^=&]+)', query)
    res = dict()
    for key, val in params:
        res.setdefault(key, val)
    return res


if __name__ == '__main__':
    assert parse1('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse1('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse1('http://example.com/') == {}
    assert parse1('http://example.com/?') == {}
    assert parse1('http://example.com/?name=Dima') == {'name': 'Dima'}


