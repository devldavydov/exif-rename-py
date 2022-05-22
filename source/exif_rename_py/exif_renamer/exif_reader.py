from datetime import datetime
from pathlib import Path

import PIL.Image

from exif_rename_py.exif_renamer.exceptions import ExifTagDoesNotExistsException


class ExifReader:
    EXIF_TAG_DATETIMEORIGINAL = 36867

    @classmethod
    def get_datetimeoriginal(cls, image_file_path: Path) -> datetime:
        with PIL.Image.open(image_file_path) as img:
            return datetime.strptime(cls._get_tag(img, cls.EXIF_TAG_DATETIMEORIGINAL), '%Y:%m:%d %H:%M:%S')

    @classmethod
    def _get_tag(cls, img: PIL.Image.Image, tag_code: int) -> str:
        try:
            return img._getexif()[tag_code]
        except Exception:
            raise ExifTagDoesNotExistsException()
