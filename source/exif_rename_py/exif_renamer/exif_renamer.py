import os
import sys
from pathlib import Path

from exif_rename_py.exif_renamer.exceptions import ExifTagDoesNotExistsException
from exif_rename_py.exif_renamer.exif_reader import ExifReader
from exif_rename_py.exif_renamer.exif_renamer_settings import ExifRenamerSettings


class ExifRenamer:
    def __init__(self, settings: ExifRenamerSettings):
        self._settings = settings
        self._duplicates = {}
        self._total = 0

    def run(self) -> None:
        for path in self._settings.images_path.glob('**/*'):
            if path.is_dir() or not path.suffix.upper().endswith('.JPG'):
                continue

            try:
                img_cr_date = ExifReader.get_datetimeoriginal(path)
            except ExifTagDoesNotExistsException:
                self._print_err(f'!!! EXIF tag DateTimeOriginal does not exists in image {path}')
                continue

            self._safe_rename_file(path, path.parent / f"{img_cr_date.strftime('%Y%m%d_%H%M%S')}.jpg")

        if not self._settings.dry_run:
            print(f'Finished. Total renamed: {self._total}')
        else:
            print('Dry run finished')

    def _safe_rename_file(self, src: Path, dst: Path) -> None:
        if dst.exists():
            ind = self._duplicates.get(dst, 1) + 1
            self._duplicates[dst] = ind
            dst = dst.parent / f'{dst.stem}_{ind}.jpg'
        try:
            if not self._settings.dry_run:
                os.rename(src, dst)
                self._total += 1
            print(f'Move {src} -> {dst}')
        except Exception as ex:
            self._print_err(f'!!! Move failed {src} -> {dst}, {ex}')

    @staticmethod
    def _print_err(*args, **kwargs) -> None:
        print(*args, file=sys.stderr, **kwargs)
