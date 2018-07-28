from app import minify


def test_url_minifier():
    minify_url = minify("www.google.com")
    expected = "MQ=="
    assert expected == minify_url

def test_url_with_two_url():
    minify_url = minify("www.google.com")
    expected = "MQ=="
    assert expected == minify_url

    minify_url = minify("www.google.com")
    expected = "Mg=="
    assert expected == minify_url
