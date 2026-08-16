#!/usr/bin/env python
# coding: utf-8
import random
import pprint
import os
from pathlib import Path

from html_generator import WichtelHtmlGenerator

def clear_output():
    out_folder = Path('output')

    for f in out_folder.iterdir():
        if f.is_file():
            f.unlink()

clear_output()

with open('personen.txt', 'r', encoding='utf-8') as f:
    TEILNEHMER = f.read().splitlines()

KREISE = 1

print(f"Teilnehmer: {len(TEILNEHMER)}, Kreise: {KREISE}")


random.shuffle(TEILNEHMER)
TEILNEHMER

wichtel = TEILNEHMER[-1:] + TEILNEHMER[:-1]
liste = dict(zip(TEILNEHMER, wichtel))

# pprint.pp(liste)  # kann zu Debug-Zwecken auskommentiert werden; zeigt die Paarungen an.

def generate_html():
    generator = WichtelHtmlGenerator(output_dir="output")
    generator.generate(liste)


generate_html()
