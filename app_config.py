# coding=utf-8

from pathlib import Path


class Config:

    Host = "0.0.0.0"
    Port = 8081

    BASE_DIR = Path(__file__).resolve().parent.parent
    # AIRTEST_IMG_DIR = BASE_DIR / '.airtest_images'
    # AIRTEST_SNAPSHOT_DIR = BASE_DIR / '.snapshots'
