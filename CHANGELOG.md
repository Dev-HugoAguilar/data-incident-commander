# Historial de cambios

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y
las versiones usan [Versionado Semántico](https://semver.org/lang/es/).

## [1.0.0] — 2026-11-26

### Añadido

- Primera publicación como repositorio independiente.
- Aplicación estática con el recorrido completo del incidente: diagnóstico,
  dependencias afectadas, comparación de remediaciones, matriz de validaciones,
  traza por carriles y plan de cuarentena.
- Tres escenarios deterministas (`missing`, `duplicate`, `schema`) que inyectan
  la falla solo en una copia en memoria.
- Servicio de dominio con runs efímeros, aprobación humana obligatoria y recibo
  de simulación.
- Bloqueo explícito de la imputación (`forward`) como plan no aprobable.
- Verificación de integridad del archivo fuente mediante SHA-256.
- Ocho pruebas de dominio sin red, sin base de datos y sin credenciales.
- Integración continua que ejecuta las pruebas y verifica que no se publicen
  credenciales.

### Nota

El repositorio se extrae del portafolio de datos de Hugo Aguilar. La capa HTTP
permanece en el repositorio de infraestructura `portfolio-api`.
