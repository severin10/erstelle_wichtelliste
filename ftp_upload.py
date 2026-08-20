#!/usr/bin/env python
# coding: utf-8
"""Laedt den Inhalt von output/ per FTP(S) auf einen Webserver hoch.

Zugangsdaten stehen in ftp_config.ini (siehe ftp_config.ini.example).
"""
import configparser
import ftplib
import os
import sys

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "ftp_config.ini")
LOCAL_DIR = os.path.join(os.path.dirname(__file__), "output")


def load_config(path=CONFIG_FILE):
    config = configparser.ConfigParser()
    if not config.read(path, encoding="utf-8"):
        sys.exit(
            f"Konfigurationsdatei nicht gefunden: {path}\n"
            f"Bitte ftp_config.ini.example nach ftp_config.ini kopieren und ausfuellen."
        )
    return config["ftp"]


def connect(cfg):
    use_tls = cfg.getboolean("use_tls", fallback=True)
    ftp = ftplib.FTP_TLS() if use_tls else ftplib.FTP()
    ftp.connect(cfg["host"], cfg.getint("port", fallback=21))
    ftp.login(cfg["user"], cfg["password"])
    if use_tls:
        ftp.prot_p()
    return ftp


def ensure_remote_dir(ftp, remote_dir):
    for part in remote_dir.strip("/").split("/"):
        if not part:
            continue
        try:
            ftp.cwd(part)
        except ftplib.error_perm:
            ftp.mkd(part)
            ftp.cwd(part)


def upload_dir(ftp, local_dir):
    for name in sorted(os.listdir(local_dir)):
        local_path = os.path.join(local_dir, name)
        if os.path.isfile(local_path):
            with open(local_path, "rb") as f:
                ftp.storbinary(f"STOR {name}", f)
            print(f"hochgeladen: {name}")


def main():
    if not os.path.isdir(LOCAL_DIR):
        sys.exit(f"Ordner nicht gefunden: {LOCAL_DIR}. Zuerst die Webseite generieren.")

    cfg = load_config()
    ftp = connect(cfg)
    try:
        remote_dir = cfg.get("remote_dir", fallback="").strip()
        if remote_dir:
            ensure_remote_dir(ftp, remote_dir)
        upload_dir(ftp, LOCAL_DIR)
    finally:
        ftp.quit()

    print("Upload abgeschlossen.")


if __name__ == "__main__":
    main()
