# erstelle_wichtelliste

Ihr seid eine Familie oder ein Freundeskreis, der sich untereinander beschenken will, möchtet aber das klassische Losziehen vereinfachen? Oder ihr seid nicht am gleichen Ort und möchtet eure Tradition trotzdem weiterführen?

Dieses python-Script erstellt anhand der Namen in **personen.txt** eine zufällige Paarung mit Wichtel und beschenkter Person und gibt diese anschliessend per HTML aus, für jeden Wichtel eine eigene Seite.

Damit die zu beschendenke (und zu überraschende Person) nicht aus Versehen angezeigt wird, ist sie erst nach einem Klick sichtbar.

Die Seiten sind nicht geschützt, es funktioniert auf Vertrauensbasis der Teilnehmer. Somit könnte ein Teilnehmer sich seine Überraschung verderben und bei den a

# Voraussetzungen
1. Python 3.12 (oder ähnlich) vorhanden auf deinem System
1. Ein Webserver für statische HTML-Dateien, um das Resultat der Losziehung mit den Teilnehmern zu teilen.

# Anleitung

1. Du hast Python 3.12 oder ähnlich auf deinem System installiert.
1. Klone das Repo.
1. Fülle die Datei **personen.txt** mit den gewünschten Teilnehmernamen aus und speichere sie.
1. Führe `python wichtellist.py` aus.

Im Ordner `output` wurde nun für jeden Teilnehmer eine html-Datei erstellt plus eine Datei **index.html**

Lade die Dateien auf deinen Webserver hoch und verschicke die Links dazu. Dafür kannst du entweder deinen gewohnten FTP-Client verwenden oder das mitgelieferte Upload-Script, siehe nächster Abschnitt.

# Upload per FTP

**ftp_upload.py** lädt den kompletten Inhalt von `output/` automatisch per FTP(S) auf deinen Webserver hoch, sodass du die Dateien nicht manuell per FTP-Client übertragen musst.

1. Kopiere **ftp_config.ini.example** zu **ftp_config.ini** (falls diese Datei noch nicht existiert).
1. Trage in **ftp_config.ini** deine Zugangsdaten ein:
   - `host`: Adresse deines FTP-Servers
   - `port`: FTP-Port (Standard: 21)
   - `user` / `password`: dein FTP-Zugang
   - `remote_dir`: Zielverzeichnis auf dem Server (leer lassen für das Wurzelverzeichnis); wird bei Bedarf automatisch angelegt
   - `use_tls`: `true` für eine verschlüsselte FTPS-Verbindung (empfohlen, sofern dein Provider das unterstützt)
1. Führe `python ftp_upload.py` aus.

Das Script lädt alle Dateien aus `output/` (die HTML-Seiten sowie **style.css**) auf den Server hoch und meldet jede erfolgreich übertragene Datei.

`ftp_config.ini` enthält dein Passwort im Klartext und ist deshalb per **.gitignore** von der Versionskontrolle ausgeschlossen – sie sollte nicht geteilt oder eingecheckt werden.

# Screenhots

Index, für alle Teilnehmer:
![Index-Seite](screenshots/index.png)

Seite für Emma, zugeklappt:
![Seite für Emma, zugeklappt](screenshots/Emma_geschlossen.png)

Seite für Emma, aufgeklickt:
![Seite für Emma, offen](screenshots/Emma_aufgedeckt.png)