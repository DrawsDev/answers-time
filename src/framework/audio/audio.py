import os
import pygame
import pygame._sdl2.audio as sdl2_audio
from typing import Optional, Tuple

class Audio:
    def __init__(
        self,
        frequency: int = 44100,
        size: int = -16,
        channels: int = 2,
        buffer: int = 512,
        devicename: Optional[str] = None,
        allowedchanges: int = 5
    ) -> None:
        self._frequency = frequency
        self._size = size
        self._channels = channels
        self._buffer = buffer
        self._devicename = devicename
        self._allowedchanges = allowedchanges
        self.initialize()

    def initialize(self) -> None:
        try:
            pygame.mixer.init(
                self._frequency, 
                self._size, 
                self._channels, 
                self._buffer, 
                self._devicename, 
                self._allowedchanges
            )
        except:
            return

    def is_initialized(self) -> bool:
        initialized = pygame.mixer.get_init()
        return initialized      

    def get_devices(self, capture_devices: bool = False) -> Optional[Tuple[str, ...]]:
        if not self.is_initialized():
            return
        return tuple(sdl2_audio.get_audio_device_names(capture_devices))

    def set_device(self, devicename: Optional[str] = None) -> None:
        if self.is_initialized():
            pygame.mixer.quit()
        if self._devicename == devicename:
            return
        self._devicename = devicename
        self.initialize()

    def sound(self, path: str) -> Optional[pygame.mixer.Sound]:
        if not self.is_initialized():
            return
        if not os.path.exists(path):
            return
        return pygame.mixer.Sound(path)

    def play(self, sound: Optional[pygame.mixer.Sound], loops: int = 0) -> None:
        if not self.is_initialized():
            return
        if sound is None:
            return
        sound.play(loops)

__all__ = ["Audio"]