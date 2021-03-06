import quickle

project = "quickle 🥒"
copyright = "2020, Jim Crist-Harif"
author = "Jim Crist-Harif"
release = version = quickle.__version__

html_theme = "alabaster"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
]
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
napoleon_numpy_docstring = True
napoleon_google_docstring = False
default_role = "obj"
pygments_style = "sphinx"

templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme_options = {
    "description": "A quicker pickle",
    "github_button": True,
    "github_count": False,
    "github_user": "jcrist",
    "github_repo": "quickle",
    "travis_button": False,
    "show_powered_by": False,
    "page_width": "960px",
    "sidebar_width": "200px",
    "code_font_size": "0.8em",
}
html_sidebars = {"**": ["about.html", "navigation.html", "help.html", "searchbox.html"]}
extlinks = {
    "issue": ("https://github.com/jcrist/quickle/issues/%s", "Issue #"),
    "pr": ("https://github.com/jcrist/quickle/pull/%s", "PR #"),
}
