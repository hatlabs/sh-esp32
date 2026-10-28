# SH-ESP32 documentation

Source of the [Sailor Hat with ESP32 (SH-ESP32)](https://docs.hatlabs.fi/sh-esp32) documentation site, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). The documentation is written in English; translations are in progress.

## Building

```sh
uv sync
uv run mkdocs serve
```

`uv run mkdocs build --strict` produces the site in `site/`. Pushes to `main` deploy it to GitHub Pages.

## License

Copyright © 2021–2026 Hat Labs Oy.

Everything in this repository is licensed under [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0), with these exceptions:

- A directory that contains its own license file is licensed under that file.
- Hardware design files reproduced here, such as schematic PDFs, are licensed under the license of the hardware design they come from. The SH-ESP32 schematics are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

### Trademarks

The licenses above do not grant any rights to the Hat Labs name and logo, or to the product names SH-ESP32 and Sailor Hat, which are trademarks of Hat Labs Oy. You may use the names to refer to Hat Labs and its products, but not in a way that suggests endorsement by Hat Labs or that your work is an official Hat Labs product.
