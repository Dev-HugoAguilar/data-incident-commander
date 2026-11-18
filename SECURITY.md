# Política de seguridad

## Alcance

Este repositorio no se conecta a servicios externos, no procesa datos
personales, no almacena secretos y no escribe fuera del proceso. La demo se
ejecuta por completo en el navegador y el servicio de dominio solo lee un
archivo JSON incluido en el repositorio.

## Cómo reportar

Si encuentras una vulnerabilidad, usa los **avisos privados de seguridad** de
GitHub: pestaña *Security* → *Report a vulnerability*. Evita abrir un *issue*
público con detalles explotables.

Incluye, cuando aplique:

- versión o commit afectado;
- pasos mínimos para reproducir;
- impacto esperado y observable;
- cualquier mitigación que ya hayas probado.

## Compromiso de respuesta

Este es un proyecto de portafolio mantenido de forma individual. Se revisan los
reportes por orden de llegada y se responde con una evaluación inicial cuando el
reporte contiene pasos reproducibles.

## Buenas prácticas para quien despliega

- No añadas credenciales al repositorio; usa variables de entorno.
- Sirve la demo detrás de HTTPS si la expones fuera de `127.0.0.1`.
- Revisa el resultado de la verificación de credenciales de la integración
  continua antes de fusionar cambios.
