import article;

def test_article3(capfd):
    article3 = article.Article("Le Trône de fer, Tome 1", 13.29)
    assert article3.getPrix() == 13.29
    assert article3.getDesignation() == "Le Trône de fer, Tome 1"
    article3.affiche()  # write to stdout
    out, err = capfd.readouterr()
    assert out == "Le Trône de fer, Tome 1 : 13.29 euros\n"
