# Mastering Nuxt - personal notes

## Install the dependencies

To edit this content yourself, you need to install the required dependencies. It
is preferable to use a virtual environment (virtualenv) using ``pip`` or even
better, the ``poetry`` dependency manager.

To install poetry, use the following command in your UNIX shell 

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

It is then very easy to install the dependencies with

```bash
poetry install
```

## Loading the virtual environment

To activate the virtual environment, use 

```bash
poetry shell
```

## Rendering the docs with autoreload

To efficiently write the documentation, it is useful to have near-instant
feedback and rendering. This can be achieved with 

```bash
make livehtml
```

This will launch a dev server with "autoreload" on each save.
 
## Generating the online HTML version

To compile the documentation into HTML, there are many useful rules defined in
the root ``Makefile``, use 

```bash
make html
```


To build the HTML documentation (static Website that can be uploaded pretty much
anywhere), 

## Generating the PDF

Through LaTeX, Sphinx allows to generate a PDF from the documentation source
instead of only the HTML version. This requires a proper LaTeX distribution to
be installed in the PATH. Under Linux, you can use the following commands:

```bash
sudo apt update
sudo apt-get install texlive-latex-extra texlive-lang-english texlive-fonts-recommended latexmk
```

Once LaTeX is installed, you can build the LaTeX documentation into the
`build/latex` directory with 

```bash
make pdf
```

You can get the generated PDF with 

```bash
make getpdf
```

This will just copy the PDF from `build/latex` to the root directory of the
documentation for easy access.


