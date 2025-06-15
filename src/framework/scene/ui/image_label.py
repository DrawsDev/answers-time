from typing import Tuple, Optional
from src.framework.enums import *
from src.framework.application import Application
from src.framework.scene.ui import PrimitiveImage

class ImageLabel(PrimitiveImage):
    def __init__(
        self, 
        app: Application, 
        path: Optional[str] = None, 
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0,
        scale_factor: float = 1.0
    ) -> None:
        super().__init__(app, path, position, anchor, z_index, scale_factor)
