#!/usr/bin/env python
# coding: utf-8
import os
import shutil

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
STYLESHEET = "style.css"


class WichtelHtmlGenerator:
    """Generiert statische HTML-Seiten fuer eine Wichtel-Zuteilung."""

    def __init__(self, output_dir="output"):
        self.output_dir = output_dir

    def generate(self, zuteilung: dict):
        os.makedirs(self.output_dir, exist_ok=True)

        self._write_stylesheet()

        for geber, beschenkter in zuteilung.items():
            self._write_person_page(geber, beschenkter)

        self._write_index(zuteilung)

    def _write_stylesheet(self):
        shutil.copy(
            os.path.join(STATIC_DIR, STYLESHEET),
            os.path.join(self.output_dir, STYLESHEET),
        )

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
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wichteln – {geber}</title>
<link rel="stylesheet" href="{STYLESHEET}">
</head>
<body class="person-page">
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
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wichteln – Übersicht</title>
<link rel="stylesheet" href="{STYLESHEET}">
</head>
<body class="index-page">
  <h1>Wichteln 🎁</h1>
  <ul>
{links}
  </ul>
</body>
</html>
"""
