def test_url_minifier():
    minify_url = minify("www.google.com")
    expected = "MQ=="
    assert expected == minify_url
