"""Ejemplo ejecutable de extremo a extremo del Data Incident Commander.

Uso::

    python examples/uso.py

Requiere el paquete instalado (``python -m pip install -e .``). Usa el snapshot
incluido en ``web/data.json``, inyecta la falla del escenario ``missing`` en una
copia en memoria, pide la aprobación humana y simula la reparación. Nada se
escribe fuera del proceso: el digest del archivo fuente se comprueba al final.
"""

from __future__ import annotations

from app.config import Settings
from app.incident_commander.service import IncidentCommander

ESCENARIO = "missing"


def main() -> int:
    comandante = IncidentCommander(Settings())

    salud = comandante.salud()
    print(f"Modo: {salud['mode']} · LLM: {salud['llm']} · Atlas: {salud['atlas']}")
    print(f"Observaciones del snapshot: {salud['observations']}")
    print(f"Digest del snapshot: {salud['source_digest']}")
    print(f"Escenarios disponibles: {', '.join(salud['scenarios'])}")

    run = comandante.crear_run(ESCENARIO)
    fallidas = [check["id"] for check in run["baseline_checks"] if not check["passed"]]
    print(f"Run: {run['run_id']} · estado: {run['status']}")
    print(f"Escenario: {run['scenario']['name']} ({run['scenario']['severity']})")
    print(f"Filas en la copia de trabajo: {run['observations_in_copy']} de {run['observations_in_source']}")
    print(f"Validaciones que fallan en la copia: {', '.join(fallidas)}")
    print(f"Plan recomendado: {run['recommended_plan']}")

    recibo = comandante.aprobar(run["run_id"], approved=True, plan_id=run["recommended_plan"])
    print(f"Estado tras aprobar: {recibo['status']}")
    print(f"Recibo: {recibo['receipt']}")
    print(f"Filas antes/después: {recibo['rows_before']} -> {recibo['rows_after']}")
    print(f"Fuente intacta: {recibo['source_unchanged']} · escrituras externas: {recibo['external_writes']}")

    # Comprobación explícita de lo que se acaba de imprimir. Antes de aprobar,
    # `human_approval_recorded` falla por definición: el run espera la decisión.
    assert salud["observations"] == 21, salud["observations"]
    assert run["observations_in_copy"] == 20, run["observations_in_copy"]
    assert fallidas == ["period_coverage", "human_approval_recorded"], fallidas
    assert recibo["status"] == "sandbox_simulation_completed", recibo["status"]
    assert recibo["receipt"].startswith("RCPT-"), recibo["receipt"]
    assert recibo["source_unchanged"] is True, recibo["source_unchanged"]
    assert recibo["external_writes"] == 0, recibo["external_writes"]

    print("OK · reparación simulada con aprobación registrada, sin escrituras")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
