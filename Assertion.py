import re


def parse(query: str) -> dict:
    params = re.findall(r'([^=&?]+)=([^=&]+)', query)
    res = dict()
    for key, val in params:
        res.setdefault(key, val)
    return res


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


