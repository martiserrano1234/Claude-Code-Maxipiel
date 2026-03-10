# Skill: Notificación de Sonido

## Propósito

Emitir una alerta sonora al terminar procesos largos, para que Felix sepa cuándo volver a la pantalla.

## Cuándo activar esta skill

Activa esta skill automáticamente al terminar cualquier tarea que:
- El usuario mencionó que tardaría varios minutos
- Involucre múltiples pasos secuenciales (auditorías, instalaciones, generación de workflows, análisis de ads, etc.)
- Claude estime que tardó más de 2-3 minutos en completarse

## Cómo ejecutarla

Al finalizar el proceso, corre este comando Bash **antes** de dar la respuesta final:

```bash
powershell -c "[console]::beep(1000,300); Start-Sleep -Milliseconds 100; [console]::beep(1000,300); Start-Sleep -Milliseconds 100; [console]::beep(1200,500)"
```

Esto emite 3 beeps (dos cortos + uno más largo y agudo) para llamar la atención de Felix.

## Nota

No hace falta que Felix lo pida explícitamente — es una skill pasiva que se activa sola cuando aplica.
