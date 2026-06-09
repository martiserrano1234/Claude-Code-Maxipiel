// Heartbeat continuo para Sofía y Claude en Miniverse
// Corre: node heartbeat.mjs

const URL = 'http://localhost:4321/api/heartbeat';

const agents = [
  {
    agent: 'sofia',
    name: 'Sofía',
    state: 'working',
    task: 'Atendiendo clientes de Maxipiel',
    energy: 0.9,
    color: '#FF6B35',
  },
  {
    agent: 'claude',
    name: 'Claude',
    state: 'thinking',
    task: 'Analizando datos de ventas',
    energy: 1.0,
    color: '#7C3AED',
  },
];

async function sendHeartbeats() {
  for (const agent of agents) {
    try {
      const res = await fetch(URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(agent),
      });
      const data = await res.json();
      if (data.ok) {
        console.log(`[${new Date().toLocaleTimeString()}] ✓ ${agent.name} — ${agent.state}`);
      }
    } catch (e) {
      console.error(`[${new Date().toLocaleTimeString()}] ✗ ${agent.name} — servidor no disponible`);
    }
  }
}

console.log('🎮 Heartbeat iniciado — Sofía y Claude activos en Miniverse');
console.log('   Ctrl+C para detener\n');

// Enviar inmediatamente al arrancar
sendHeartbeats();

// Luego cada 30 segundos
setInterval(sendHeartbeats, 30_000);
