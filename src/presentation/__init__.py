"""
Módulos de interface com usuário.
Contém implementações de CLI e gerenciamento de câmera.
"""
from .cli.main_menu import MainMenu
from .camera.camera_manager import CameraManager

__all__ = ['MainMenu', 'CameraManager']