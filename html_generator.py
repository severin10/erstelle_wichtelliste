#!/usr/bin/env python
# coding: utf-8
import os


class WichtelHtmlGenerator:
    """Generiert statische HTML-Seiten fuer eine Wichtel-Zuteilung."""

    def __init__(self, output_dir="output"):
        self.output_dir = output_dir

    def generate(self, zuteilung: dict):
        os.makedirs(self.output_dir, exist_ok=True)

        for geber, beschenkter in zuteilung.items():
            self._write_person_page(geber, beschenkter)

        self._write_index(zuteilung)

    def _person_filename(self, name):
        return f"{name}.html"

    def _write_person_page(self, geber, beschenkter):
        path = os.path.join(self.output_dir, self._person_filename(geber))
        with open(path, "w", encoding="utf-8") as f:
            f.write(self._person_html(geber, beschenkter))

    def _write_index(self, zuteilung):
        links = "\n".join(
            f'      <li><a href="{self._person_filename(geber)}">{geber}</a></li>'
            for geber in sorted(zuteilung)
        )
        path = os.path.join(self.output_dir, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(self._index_html(links))

    def _person_html(self, geber, beschenkter):
        return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Wichteln – {geber}</title>
<style>
  :root {{
    color-scheme: light dark;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    margin: 0;
    background: #f7f3ef;
    color: #222;
    text-align: center;
    padding: 2rem;
    box-sizing: border-box;
  }}
  h1 {{
    font-size: clamp(2.5rem, 8vw, 4.5rem);
    margin: 0 0 0.5rem;
  }}
  p.subtitle {{
    font-size: 1.1rem;
    color: #666;
    margin: 0 0 3rem;
  }}
  .reveal-box {{
    min-height: 3.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  button {{
    font-size: 1.2rem;
    padding: 0.9rem 2rem;
    border: none;
    border-radius: 999px;
    background: #b23b3b;
    color: #fff;
    cursor: pointer;
  }}
  button:hover {{
    background: #922f2f;
  }}
  #name {{
    font-size: clamp(2rem, 6vw, 3.2rem);
    font-weight: bold;
    color: #b23b3b;
    display: none;
  }}
</style>
</head>
<body>
  <h1>{geber}</h1>
  <p class="subtitle">Du beschenkst dieses Jahr …</p>
  <div class="reveal-box">
    <button id="revealBtn" onclick="reveal()">Aufdecken 🎁</button>
    <div id="name">{beschenkter}</div>
  </div>
  <script>
    function reveal() {{
      document.getElementById('revealBtn').style.display = 'none';
      document.getElementById('name').style.display = 'block';
    }}
  </script>
</body>
</html>
"""

    def _index_html(self, links):
        return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Wichteln – Übersicht</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    max-width: 30rem;
    margin: 3rem auto;
    padding: 0 1.5rem;
    color: #222;
  }}
  h1 {{
    text-align: center;
  }}
  ul {{
    list-style: none;
    padding: 0;
  }}
  li {{
    margin: 0.5rem 0;
  }}
  a {{
    display: block;
    padding: 0.8rem 1rem;
    background: #f7f3ef;
    border-radius: 0.5rem;
    text-decoration: none;
    color: #b23b3b;
    font-weight: bold;
  }}
  a:hover {{
    background: #eee0d5;
  }}
</style>
</head>
<body>
  <h1>Wichteln 🎁</h1>
  <ul>
{links}
  </ul>
</body>
</html>
"""
