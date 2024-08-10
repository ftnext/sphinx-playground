import pytest


@pytest.mark.sphinx("html", testroot="default")
def test_example(app):
    app.build()

    assert (app.outdir / "index.html").exists()
