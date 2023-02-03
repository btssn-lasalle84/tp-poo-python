import article;

def test_article2():
    article2 = article.Article("Le Trône de fer, Tome 1", 13.29)
    assert article2.getPrix() == 13.29
    assert article2.getDesignation() == "Le Trône de fer, Tome 1"
