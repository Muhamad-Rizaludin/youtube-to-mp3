# YouTube ke MP3

Skrip ini mengambil audio dari URL YouTube dan mengubahnya menjadi file `mp3`.

## File

- `youtube_to_mp3.py` : program utama
- `requirements.txt` : dependensi Python

## Kebutuhan

1. Python 3.10+
2. `ffmpeg` terpasang dan tersedia di `PATH`

## Install

```powershell
pip install -r requirements.txt
```

## Cara pakai

Contoh dengan URL yang Anda berikan:

```powershell
python youtube_to_mp3.py "https://youtu.be/fxYO_oO1jXk?si=hvEZQr6l4-fARWNZ"
```

Simpan ke folder tertentu:

```powershell
python youtube_to_mp3.py "https://youtu.be/fxYO_oO1jXk?si=hvEZQr6l4-fARWNZ" -o hasil
```

## Catatan

- Program ini menghasilkan file `mp3`.
- Gunakan hanya untuk konten yang memang Anda punya hak untuk unduh / konversi.
