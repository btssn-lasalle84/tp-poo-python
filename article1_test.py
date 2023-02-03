import article;

def test_article1():
    article1 = article.Article()
    assert article1.getPrix() == 0.0
    assert article1.getDesignation() == ""
