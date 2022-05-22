from dataclasses import dataclass
from pathlib import Path


@dataclass
class ExifRenamerSettings:
    images_path: Path
    dry_run: bool
