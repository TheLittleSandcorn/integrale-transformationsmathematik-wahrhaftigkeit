# PUBLISHING_GUIDE.md — Anleitung zur Veröffentlichung auf GitHub

## 1. Repository anlegen

1. Auf GitHub anmelden.
2. Oben rechts auf `+` klicken.
3. `New repository` auswählen.
4. Repository-Name empfehlen:
   `integrale-transformationsmathematik-wahrhaftigkeit`
5. Beschreibung:
   `Open AI-assisted documentation dataset for Integral Transformational Mathematics and Truth-Oriented Analysis.`
6. Sichtbarkeit: zunächst `Public`, wenn du direkt offen veröffentlichen möchtest; sonst erst `Private` und nach Prüfung auf `Public`.
7. README nicht automatisch erzeugen, wenn du dieses Paket hochlädst.
8. License nicht automatisch auswählen, wenn du die enthaltene `LICENSE` nutzt.

## 2. Dateien hochladen über Weboberfläche

1. Repository öffnen.
2. `Add file` → `Upload files`.
3. Alle Dateien und Ordner aus diesem Repository-Paket hochladen.
4. Commit-Text:
   `Initial transparent documentation release`
5. Commit abschließen.

## 3. Dateien hochladen über Git CLI

```bash
git clone https://github.com/DEIN_USERNAME/integrale-transformationsmathematik-wahrhaftigkeit.git
cd integrale-transformationsmathematik-wahrhaftigkeit

# Paketinhalt in diesen Ordner kopieren, dann:
git add .
git commit -m "Initial transparent documentation release"
git branch -M main
git push origin main
```

## 4. Prüfsummen lokal prüfen

```bash
python scripts/verify_sha256.py
```

## 5. GitHub Release erstellen

1. Im Repository rechts auf `Releases` klicken.
2. `Draft a new release` auswählen.
3. Tag:
   `v0.1.0-draft`
4. Release-Titel:
   `v0.1.0-draft — Transparent documentation release`
5. Release Notes:
   Siehe `RELEASE_NOTES_v0.1.0.md`.
6. Optional: ZIP-Datei zusätzlich als Asset hochladen.

## 6. Empfohlene Beschreibung für GitHub

```text
Open AI-assisted documentation dataset and research framework for Integral Transformational Mathematics and Truth-Oriented Analysis. Includes 27 indexed work steps, TOP-content tables, formula index, era index, manifest files, and SHA-256 checksums.
```

## 7. Wissenschaftlicher Schutz vor Überclaiming

Bitte nicht schreiben:

```text
This repository proves the complete history of mathematics.
```

Besser:

```text
This repository provides a transparent, AI-assisted, versioned documentation framework for studying mathematical transformations across human history, with explicit truth-status labels and ethical limitations.
```

## 8. Nach Veröffentlichung

- Issues aktiv lassen.
- Korrekturen willkommen heißen.
- Quellenverbesserungen als Pull Requests akzeptieren.
- Versionen veröffentlichen: `v0.1.0-draft`, `v0.2.0-review`, `v1.0.0-reviewed`.
