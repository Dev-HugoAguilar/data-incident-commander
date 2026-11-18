# Arquitectura y límites de autoridad

## Capas

```text
┌─────────────────────────────────────────────┐
│ web/  aplicación estática                   │
│  · flujo del incidente, SVG, accesibilidad  │
│  · lee data.json, no escribe nada           │
└───────────────────┬─────────────────────────┘
                    │ mismo contrato
┌───────────────────▼─────────────────────────┐
│ src/app/incident_commander/service.py       │
│  · escenarios, copia con falla, validaciones│
│  · runs y recibos en memoria del proceso    │
│  · sin red, sin disco, sin credenciales     │
└───────────────────┬─────────────────────────┘
                    │ opcional
┌───────────────────▼─────────────────────────┐
│ portfolio-api  (repositorio aparte)         │
│  · expone el servicio por HTTP              │
└─────────────────────────────────────────────┘
```

La interfaz y el servicio son independientes: la demo funciona sin API y escucha
solo `web/data.json`. Esta separación permite demostrar el producto sin backend
y, a la vez, mantener un servicio auditable con pruebas propias.

## Flujo del incidente

1. **Carga** — el servicio lee el snapshot, valida que conserve 21 observaciones
   y sus fuentes, y calcula dos huellas: un digest canónico de las filas y el
   SHA-256 del archivo.
2. **Diagnóstico** — al crear un *run* se construye una copia con la falla
   inyectada. La copia vive solo en memoria durante la petición.
3. **Validaciones** — se evalúan reglas nombradas (`period_coverage`,
   `key_uniqueness`, `catalog_codes`, `known_indicators`,
   `human_approval_recorded`) contra el estado base y contra el candidato.
4. **Comparación** — se presentan cuatro alternativas con puntuaciones
   hipotéticas del escenario. Son una hipótesis comparativa, no una medición.
5. **Aprobación humana** — el run queda en `awaiting_human`. Aprobar exige un
   plan de la lista permitida; rechazar no tiene efecto.
6. **Simulación** — la reparación se aplica a una copia y se emite un recibo
   `RCPT-…`. El archivo fuente se vuelve a leer para comprobar que no cambió.

## Estados del run

| Estado | Significado |
|---|---|
| `awaiting_human` | Diagnóstico terminado; espera decisión. |
| `sandbox_simulation_completed` | Aprobado y simulado en memoria. |
| `rejected_no_effect` | Rechazado; sin cambios. |

Una segunda decisión sobre el mismo run produce `RunConflict`. Un plan fuera de
la lista permitida produce `PlanBlocked` y deja el run intacto.

## Modelo de autoridad

El agente puede **leer**, **diagnosticar** y **simular**. No puede escribir,
publicar, escalar ni imputar. La imputación simple (`forward`) está bloqueada a
propósito porque reemplaza un dato faltante por una suposición y convierte un
vacío verificable en un valor aparente. `external_writes` se publica en todas las
respuestas y siempre es `0`.

## Estado y persistencia

Los *runs* viven en un diccionario del proceso. Reiniciar el servicio los
elimina. No hay base de datos, ni cola, ni archivos de salida: la ausencia de
persistencia es parte del mensaje, no una limitación pendiente.

## Contrato HTTP (implementado en `portfolio-api`)

| Método | Ruta | Respuesta |
|---|---|---|
| `GET` | `/api/v1/incident-commander/health` | Salud, huellas y conteo de observaciones. |
| `GET` | `/api/v1/incident-commander/snapshot` | Resumen del snapshot y sus fuentes. |
| `POST` | `/api/v1/incident-commander/runs` | Crea un run con `{"scenario_id": "missing"}`. |
| `POST` | `/api/v1/incident-commander/runs/{run_id}/approve` | Aplica `{"approved": true, "plan_id": "quarantine"}`. |

El cuerpo de estas rutas es exactamente el diccionario que devuelven
`crear_run()` y `aprobar()` en `service.py`; la API solo añade validación de
esquema y códigos de estado.

## No objetivos

- No reemplaza un sistema de observabilidad ni un catálogo de datos.
- No ejecuta reparaciones reales ni conecta con almacenes de datos.
- No incorpora un modelo de lenguaje: la secuencia es explícita y repetible.
