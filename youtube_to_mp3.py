from __future__ import annotations

import argparse
import shutil
import sys
import os
from pathlib import Path

from yt_dlp import YoutubeDL


def find_ffmpeg() -> str | None:
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg

    if os.name == "nt":
        winget_root = Path.home() / "AppData" / "Local" / "Microsoft" / "WinGet" / "Packages"
        if winget_root.exists():
            matches = sorted(winget_root.glob("**/ffmpeg.exe"))
            if matches:
                return str(matches[0])

    return None


def download_as_mp3(url: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg_path = find_ffmpeg()

    if ffmpeg_path is None:
        raise SystemExit(
            "ffmpeg tidak ditemukan.\n"
            "Silakan install ffmpeg lalu pastikan perintah 'ffmpeg' tersedia di PATH."
        )

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "socket_timeout": 120,
        "retries": 10,
        "fragment_retries": 10,
        "extractor_retries": 5,
        "continuedl": True,
        "ffmpeg_location": ffmpeg_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Unduh audio dari URL YouTube lalu ubah ke MP3."
    )
    parser.add_argument("url", help="URL video YouTube")
    parser.add_argument(
        "-o",
        "--output",
        default="downloads",
        help="Folder output hasil MP3 (default: downloads)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    download_as_mp3(args.url, Path(args.output))
    print("Selesai. File MP3 disimpan di folder:", Path(args.output).resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
