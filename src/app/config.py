"""Configuración mínima del servicio de respuesta a incidentes de datos.

El servicio solo necesita una ruta: el *snapshot* de observaciones que valida
en modo lectura. Este módulo la resuelve sin depender del backend del
portafolio y sin leer secretos.

Decisiones deliberadas:

- ``env_file=None``: nunca se descubre un ``.env`` del sistema. Los valores
  llegan por argumento o por variable de entorno explícita.
- ``extra="ignore"``: variables ajenas al servicio no rompen la carga.
- Las rutas del repositorio se derivan de ``__file__`` para que el proyecto
  funcione en cualquier clon, sin rutas absolutas.
"""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

#: Raíz del repositorio (``src/app/config.py`` → tres niveles arriba).
REPO_ROOT = Path(__file__).resolve().parents[2]
#: Aplicación estática incluida en el repositorio.
WEB_APP = REPO_ROOT / "web"
#: Documentación y material de apoyo.
DOCS_DIR = REPO_ROOT / "docs"


class Settings(BaseSettings):
    """Ajustes del servicio.

    Todos los campos tienen un valor por omisión válido para un clon limpio.
    """

    model_config = SettingsConfigDict(
        env_file=None,
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )

    #: Ruta del snapshot WDI. Se abre en modo lectura y su digest se publica en
    #: ``/health``; el servicio nunca lo reescribe.
    incident_data_path: str = str(WEB_APP / "data.json")
