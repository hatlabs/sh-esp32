# SH-ESP32 documentation repository

This is the SH-ESP32 Jekyll documentation repository that is rendered to project documentation available at https://docs.hatlabs.fi/sh-esp32/.
SH-ESP32 is an ESP32 development board designed for the marine environment. It is available for purchase at https://hatlabs.fi.

## Contributing

You can contribute to the documentation by cloning the repository, modifying the Markdown pages, and creating a Pull Request.
Instructions for generic GitHub use can be found at [The GitHub Guides](https://guides.github.com).

The pages are rendered using [Jekyll](https://jekyllrb.com) which is the standard tool for rendering GitHub pages.
The Jekyll theme in use is [Just the Docs](https://github.com/pmarsceill/just-the-docs).
The site uses [kramdown](https://kramdown.gettalong.org/syntax.html) as its Markdown flavor.

If you want to test your modifications locally, your easiest option is to run `./docker-jekyll bundle exec jekyll serve` in the cloned directory and then browse to [0.0.0.0:4000/sh-esp32](https://0.0.0.0:4000/sh-esp32). You must have Docker pre-installed.
