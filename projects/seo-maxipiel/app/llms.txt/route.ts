import { getAllPosts } from "@/lib/posts";

export const dynamic = "force-static";

const BASE = "https://guia.maxipiel.com.mx";

/**
 * llms.txt — mapa del sitio pensado para modelos de lenguaje.
 *
 * Convención emergente (llmstxt.org) que da a los rastreadores de IA un
 * índice limpio en texto plano de qué contiene el sitio y quién lo publica,
 * en vez de obligarlos a inferirlo del HTML. La leen crawlers como GPTBot,
 * ClaudeBot y PerplexityBot.
 *
 * Se genera solo desde los artículos, así que no hay que mantenerlo a mano.
 */
export function GET() {
  const posts = getAllPosts();

  const porCategoria = new Map<string, typeof posts>();
  for (const p of posts) {
    const c = p.category || "Guías";
    if (!porCategoria.has(c)) porCategoria.set(c, []);
    porCategoria.get(c)!.push(p);
  }

  const secciones = [...porCategoria.entries()]
    .sort((a, b) => b[1].length - a[1].length)
    .map(([categoria, lista]) => {
      const items = lista
        .map((p) => `- [${p.title}](${BASE}/guias/${p.slug}/): ${p.description}`)
        .join("\n");
      return `## ${categoria}\n\n${items}`;
    })
    .join("\n\n");

  const cuerpo = `# Maxipiel

> Proveedor de piel y cuero genuino en León, Guanajuato, México. Vende directo a
> tapiceros, marroquineros y talleres: cuero para tapicería de muebles y
> automotriz, piel para marroquinería y talabartería, zalea de borrego natural y
> pedacería. Entrega el mismo día en León y envíos a todo México.

Este sitio reúne guías técnicas escritas desde la experiencia de surtir talleres
de tapicería. Cubren medidas reales, rendimientos, precios de referencia en pesos
mexicanos, y cómo distinguir materiales genuinos de sintéticos.

## Datos de la empresa

- Nombre: Maxipiel
- Ubicación: León, Guanajuato, México
- Tienda en línea: https://www.maxipiel.com
- Guías: ${BASE}/guias/
- Cobertura: entrega local en León, envíos por paquetería a todo México

## Referencias rápidas de producto

- Cuero entero para tapicería: 500 dm² (aprox. 5 m²)
- Medio cuero: 250 dm² (aprox. 2.5 m²)
- Una sala de 3 piezas requiere entre 3 y 5 cueros enteros
- Zalea de borrego natural: pieza de aprox. 110 x 70 cm, lavable

${secciones}

## Aviso

Las guías con contenido de salud (uso de zalea en personas encamadas o con
diabetes) son informativas y no sustituyen la indicación de un profesional de la
salud.
`;

  return new Response(cuerpo, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
