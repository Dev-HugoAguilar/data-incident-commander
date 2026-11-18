# Datos: fuente, licencia y límites

## Origen

`web/data.json` contiene un snapshot de **World Development Indicators** del
Banco Mundial para México, años 2019–2025.

| Campo | Valor |
|---|---|
| `dataset_id` | `WB-WDI-MEX-2019-2025-v1` |
| Cobertura | México (`MEX`), 2019–2025 |
| Observaciones | 21 (3 indicadores × 7 años) |
| Fecha del snapshot | 2026-11-15 |
| Licencia | **CC BY 4.0** |

## Indicadores

| Código | Indicador | Unidad |
|---|---|---|
| `NY.GDP.MKTP.KD.ZG` | Crecimiento del PIB real | % anual |
| `FP.CPI.TOTL.ZG` | Inflación al consumidor | % anual |
| `SL.UEM.TOTL.ZS` | Desempleo total · estimación OIT | % de la fuerza laboral |

Cada indicador incluye en `sources` su título, la URL del indicador, la URL de la
API de origen con el filtro exacto (`format=json&date=2019:2025`) y su definición
publicada. Reproducir la descarga es una petición por indicador:

```bash
curl "https://api.worldbank.org/v2/country/MEX/indicator/NY.GDP.MKTP.KD.ZG?format=json&date=2019:2025"
```

## Atribución

> World Development Indicators, Banco Mundial. Datos bajo CC BY 4.0.
> Se cita el código de indicador, la unidad y el periodo en cada vista.

Este repositorio no incluye un archivo `LICENSE` propio. Las condiciones de la
fuente se respetan y se documentan aquí; cualquier reutilización del snapshot
debe conservar la atribución al Banco Mundial.

## Qué es sintético

Las fallas de los tres escenarios (`missing`, `duplicate`, `schema`) son
*fixtures* creadas para la demostración. Se inyectan en una copia temporal y
nunca modifican el archivo ni el snapshot de origen. **No son incidentes
reportados por el Banco Mundial ni defectos del snapshot publicado.**

## Límites de interpretación

- Es un extracto de tres indicadores, no una serie económica completa.
- `SL.UEM.TOTL.ZS` es una estimación modelada de la OIT: no mide informalidad,
  subempleo ni calidad del empleo.
- La inflación corresponde al índice general de precios al consumidor, no al
  componente subyacente ni a la meta del banco central.
- Los valores son anuales; no sostienen conclusiones de corto plazo.
- Un archivo incompleto se rechaza al cargar (`SnapshotError`): el servicio exige
  21 observaciones y sus fuentes, en lugar de aceptar un snapshot parcial.
