import argparse
from pathlib import Path

from exif_rename_py.exif_renamer.exif_renamer_settings import ExifRenamerSettings
from exif_rename_py.exif_renamer.exif_renamer import ExifRenamer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=Path, help='JPG images dir full path')
    parser.add_argument('--dry', action='store_true', help='Dry run - only print renamed image files')

    args = parser.parse_args()
    ExifRenamer(
        ExifRenamerSettings(images_path=args.path, dry_run=args.dry)
    ).run()


if __name__ == '__main__':
    main()
