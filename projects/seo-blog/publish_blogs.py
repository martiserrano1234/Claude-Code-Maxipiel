# -*- coding: utf-8 -*-
import urllib.request
import json

TOKEN = "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"
DOMAIN = "maxipiel.myshopify.com"
BLOG_ID = 92607283300

def publish_article(article_data):
    url = f"https://{DOMAIN}/admin/api/2024-01/blogs/{BLOG_ID}/articles.json"
    payload = json.dumps({"article": article_data}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("X-Shopify-Access-Token", TOKEN)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["article"]["id"], result["article"]["title"]
    except urllib.error.HTTPError as e:
        print("Error:", e.code, e.read().decode("utf-8"))
        raise

# ── Blog 1 ──────────────────────────────────────────────────────────────────
blog1 = {
    "title": "Piel Genuina vs Cuero Sintético: ¿Cuál Elegir para tu Proyecto?",
    "author": "Maxipiel",
    "tags": "piel genuina, cuero sintético, tapicería, marroquinería, guías",
    "published": True,
    "metafields": [
        {
            "key": "description_tag",
            "value": "¿No sabes si usar piel genuina o cuero sintético para tu proyecto de tapicería o marroquinería? Te explicamos las diferencias clave para que elijas con confianza.",
            "type": "single_line_text_field",
            "namespace": "global"
        }
    ],
    "body_html": """
<p>Si trabajas en tapicería, marroquinería o fabricación de calzado, seguro te has hecho esta pregunta más de una vez. En el mercado hay materiales que se ven muy parecido, pero a la hora de trabajarlos — y a la hora de que el cliente los usa — la diferencia es enorme.</p>
<p>En esta guía te explicamos todo lo que necesitas saber para elegir bien.</p>

<h2>¿Qué es la piel genuina?</h2>
<p>La piel genuina (también llamada cuero natural o cuero real) viene del cuero animal — principalmente bovino, aunque también hay de cerdo, borrego y cabra. Pasa por un proceso de curtido que puede ser vegetal, mineral (cromo) o combinado.</p>
<p>Lo que la hace especial es que es un material vivo: tiene poros naturales, respira, se adapta al calor y, con el tiempo, desarrolla una pátina que la hace ver y sentirse mejor cuanto más la usas.</p>

<h2>¿Qué es el cuero sintético (PU o PVC)?</h2>
<p>El cuero sintético — también conocido como cuero PU, polipiel o leatherette — es un tejido recubierto con poliuretano o cloruro de polivinilo. No viene de ningún animal: es un plástico diseñado para imitar la apariencia del cuero real.</p>
<p>A primera vista puede ser difícil distinguirlo, especialmente en fotografías. Pero en la mano y en el trabajo diario, las diferencias son inmediatas.</p>

<h2>Diferencias clave: piel genuina vs cuero sintético</h2>

<h3>Durabilidad</h3>
<p><strong>Piel genuina:</strong> Con el cuidado básico (limpieza y acondicionamiento ocasional), una pieza de piel genuina puede durar décadas. Los tapiceros veteranos conocen sillones con 20 o 30 años de uso que siguen en buen estado.</p>
<p><strong>Cuero sintético:</strong> Suele despostillarse, cuartearse o pelarse después de 3 a 7 años de uso regular, especialmente en zonas de roce constante como los apoyabrazos o el asiento del conductor.</p>

<h3>Apariencia con el tiempo</h3>
<p><strong>Piel genuina:</strong> Envejece con gracia. Desarrolla un brillo natural (pátina) que muchos consideran más atractivo que cuando era nueva.</p>
<p><strong>Cuero sintético:</strong> Con el tiempo pierde color de forma irregular, se pela y puede verse descuidado incluso si se limpia con frecuencia.</p>

<h3>Transpirabilidad</h3>
<p><strong>Piel genuina:</strong> Tiene poros naturales que permiten cierta circulación de aire. Esto se nota especialmente en tapicería de automóviles y muebles de uso diario.</p>
<p><strong>Cuero sintético:</strong> No respira. En climas cálidos o en verano, puede volverse pegajoso e incómodo.</p>

<h3>Facilidad de trabajo</h3>
<p><strong>Piel genuina:</strong> Se corta, cose y estira de forma predecible. Acepta bien el pegamento y las costuras aguantan sin rasgarse. Los tapiceros con experiencia generalmente la prefieren por el control que ofrece.</p>
<p><strong>Cuero sintético:</strong> Más fácil de trabajar en proyectos simples, pero puede estirarse de forma irregular y es más difícil de coser en curvas cerradas.</p>

<h3>Precio</h3>
<p><strong>Piel genuina:</strong> Tiene un costo mayor, pero la relación calidad-precio a largo plazo es superior porque no hay que reemplazarla.</p>
<p><strong>Cuero sintético:</strong> Más barato al inicio, pero si el cliente necesita reemplazarlo en 4-5 años, el costo total termina siendo mayor.</p>

<h2>¿Cuándo conviene usar cada uno?</h2>
<p><strong>Usa piel genuina cuando:</strong></p>
<ul>
  <li>El proyecto es de alta gama o el cliente quiere algo que dure muchos años</li>
  <li>Es tapicería automotriz en un vehículo de uso diario</li>
  <li>Es un mueble de sala o comedor que se usa constantemente</li>
  <li>El cliente quiere un acabado que mejore con el tiempo</li>
  <li>Estás fabricando artículos de marroquinería (bolsas, carteras, cinturones)</li>
</ul>
<p><strong>El cuero sintético puede funcionar cuando:</strong></p>
<ul>
  <li>El presupuesto del cliente es muy limitado y lo entiende</li>
  <li>Es un proyecto temporal o de corto plazo</li>
  <li>El artículo tendrá uso muy ocasional</li>
</ul>

<h2>¿Cómo distinguirlos rápido?</h2>
<p>Si tienes una muestra en mano, aquí van tres pruebas rápidas:</p>
<ol>
  <li><strong>Prueba del agua:</strong> Una gota de agua sobre piel genuina se absorbe lentamente. En sintético, el agua rueda sin penetrar.</li>
  <li><strong>Prueba del calor:</strong> Frota la superficie con el pulgar por 10 segundos. La piel genuina se calienta y se siente más suave. El sintético se siente igual.</li>
  <li><strong>Reverso:</strong> La piel genuina tiene un reverso fibroso o aterciopelado (la carne). El sintético tiene un tejido de tela en el reverso.</li>
</ol>

<h2>Conclusión</h2>
<p>Para proyectos de tapicería y marroquinería profesional, la piel genuina no tiene competencia real. Es el material que tus clientes van a agradecer durante años y el que te va a dar la reputación de hacer trabajo de calidad.</p>
<p>Si buscas piel genuina al mayoreo con los mejores precios, en <strong>Maxipiel</strong> tenemos stock disponible para tapicería de muebles, tapicería automotriz, marroquinería y calzado. Entregamos en León y enviamos a todo México.</p>
<p><a href="https://maxipiel.com.mx/collections/materia-prima">Ver catálogo de piel genuina →</a></p>
<p><em>¿Tienes dudas sobre qué tipo de piel es la mejor para tu proyecto específico? Escríbenos — con gusto te orientamos.</em></p>
"""
}

# ── Blog 2 ──────────────────────────────────────────────────────────────────
blog2 = {
    "title": "Cómo Elegir el Grosor de Piel para Tapicería Automotriz",
    "author": "Maxipiel",
    "tags": "tapicería automotriz, grosor de piel, cuero para carro, guías",
    "published": True,
    "handle": "grosor-piel-tapiceria-automotriz",
    "metafields": [
        {
            "key": "description_tag",
            "value": "¿Qué grosor de piel necesitas para tapizar asientos de carro? Guía práctica para tapiceros automotrices: calibres, usos y recomendaciones de Maxipiel.",
            "type": "single_line_text_field",
            "namespace": "global"
        }
    ],
    "body_html": """
<p>Una de las preguntas más frecuentes que recibimos de tapiceros automotrices es: <em>¿qué grosor de piel debo usar?</em> La respuesta corta es: depende de la zona del vehículo. La respuesta larga es esta guía.</p>

<h2>¿Por qué importa el grosor en tapicería automotriz?</h2>
<p>El grosor de la piel (también llamado calibre) afecta directamente tres cosas:</p>
<ul>
  <li><strong>Durabilidad:</strong> Una piel muy delgada en una zona de alto roce se va a desgastar rápido.</li>
  <li><strong>Facilidad de trabajo:</strong> Una piel muy gruesa es difícil de trabajar en curvas y costuras cerradas.</li>
  <li><strong>Acabado final:</strong> El grosor incorrecto puede hacer que el tapizado se vea abultado o flojo.</li>
</ul>

<h2>Grosores más comunes y sus usos</h2>

<h3>0.6 mm a 0.8 mm — Piel delgada</h3>
<p>Ideal para:</p>
<ul>
  <li>Tableros y consolas donde la piel solo es decorativa</li>
  <li>Paneles de puertas en zonas sin contacto frecuente</li>
  <li>Revestimientos interiores de techo</li>
</ul>
<p>Este calibre es muy manejable, dobla fácil y se pega bien. No es recomendable para asientos porque no aguanta el roce diario.</p>

<h3>0.9 mm a 1.1 mm — Grosor estándar</h3>
<p>El más usado en tapicería automotriz. Ideal para:</p>
<ul>
  <li>Asientos delanteros y traseros</li>
  <li>Apoyabrazos centrales</li>
  <li>Respaldos de asiento</li>
</ul>
<p>Ofrece el mejor balance entre durabilidad y facilidad de trabajo. Cose bien a máquina, aguanta el uso diario y se ve profesional.</p>

<h3>1.2 mm a 1.4 mm — Grosor resistente</h3>
<p>Para zonas de alto desgaste o vehículos de trabajo:</p>
<ul>
  <li>Asiento del conductor en taxis, camionetas o vehículos de reparto</li>
  <li>Fundas de volante</li>
  <li>Tapizado de camiones y autobuses</li>
</ul>
<p>Más difícil de coser en curvas cerradas. Se recomienda aguja gruesa (110/18 o 120/19) y hilo encerado.</p>

<h3>1.5 mm o más — Piel gruesa</h3>
<p>No es común en tapicería automotriz estándar. Se usa principalmente en proyectos custom o en zonas muy específicas que requieren rigidez, como bases de asiento estructurales.</p>

<h2>Tabla de referencia rápida</h2>
<table>
  <thead>
    <tr><th>Zona del vehículo</th><th>Grosor recomendado</th></tr>
  </thead>
  <tbody>
    <tr><td>Tablero / consola decorativa</td><td>0.6 – 0.8 mm</td></tr>
    <tr><td>Paneles de puerta</td><td>0.8 – 1.0 mm</td></tr>
    <tr><td>Asientos estándar</td><td>0.9 – 1.1 mm</td></tr>
    <tr><td>Asiento conductor (uso intensivo)</td><td>1.2 – 1.4 mm</td></tr>
    <tr><td>Volante</td><td>1.0 – 1.2 mm</td></tr>
    <tr><td>Techo interior</td><td>0.6 – 0.8 mm</td></tr>
  </tbody>
</table>

<h2>Otros factores a considerar además del grosor</h2>

<h3>Acabado de la superficie</h3>
<p>La piel con acabado liso resiste mejor la suciedad y es más fácil de limpiar — ideal para vehículos de trabajo. La piel con textura (napa, corrugado) se ve más premium pero puede acumular polvo en los poros.</p>

<h3>Curtido</h3>
<p>Para tapicería automotriz se recomienda piel curtida al cromo. Es más flexible, resistente a la humedad y mantiene mejor el color con el tiempo que la piel curtida vegetal.</p>

<h3>Color</h3>
<p>Los colores oscuros (negro, café oscuro, gris) disimulan mejor el desgaste y la suciedad en zonas de alto uso. Los colores claros se ven más elegantes pero requieren más mantenimiento.</p>

<h2>Consejos de instalación según el grosor</h2>
<ul>
  <li>Para piel de 0.6–0.8 mm: usa pegamento de contacto en tableros y superficies lisas. No necesita mucha tensión.</li>
  <li>Para piel de 0.9–1.1 mm: cose con aguja 90/14 o 100/16, hilo de nylon o poliéster encerado.</li>
  <li>Para piel de 1.2 mm o más: usa aguja 110/18, reduce la velocidad de la máquina en curvas y humedece ligeramente la piel si es muy rígida.</li>
</ul>

<h2>¿Dónde conseguir piel para tapicería automotriz en México?</h2>
<p>En <strong>Maxipiel</strong> tenemos piel genuina en diferentes calibres, acabados y colores — disponible al mayoreo. Entregamos en León, Guanajuato y enviamos a todo el país por paquetería.</p>
<p><a href="https://maxipiel.com.mx/collections/materia-prima">Ver piel para tapicería automotriz →</a></p>
<p><em>¿No estás seguro qué calibre es el correcto para tu proyecto? Escríbenos y te asesoramos sin compromiso.</em></p>
"""
}

# ── Blog 3 ──────────────────────────────────────────────────────────────────
blog3 = {
    "title": "¿Cuánta Piel Necesitas para Tapizar un Sillón? Guía Práctica",
    "author": "Maxipiel",
    "tags": "tapicería, cuánta piel, sillón, muebles, guías, calculadora",
    "published": True,
    "handle": "cuanta-piel-necesito-tapizar-sillon",
    "metafields": [
        {
            "key": "description_tag",
            "value": "Aprende a calcular cuánta piel genuina necesitas para tapizar un sillón, sofá o silla. Guía práctica con medidas reales para tapiceros.",
            "type": "single_line_text_field",
            "namespace": "global"
        }
    ],
    "body_html": """
<p>Una de las dudas más comunes antes de comprar piel es: <em>¿cuánto necesito?</em> Pedir de más es desperdiciar dinero. Pedir de menos es quedarte a medias en el trabajo. Esta guía te da las medidas reales para los muebles más comunes.</p>

<h2>¿Cómo se mide la piel?</h2>
<p>La piel se vende por <strong>pie cuadrado</strong> (ft²) en México. Una hoja estándar de piel bovina tiene entre 40 y 60 pies cuadrados, dependiendo del tamaño del animal.</p>
<p>Para calcular cuánto necesitas, debes sumar el área de todas las superficies a tapizar y agregar un <strong>10–15% de margen</strong> por cortes, desperdicios y errores.</p>

<h2>Tabla de referencia: ¿cuánta piel por mueble?</h2>

<h3>Silla individual</h3>
<table>
  <thead>
    <tr><th>Tipo de silla</th><th>Piel aproximada</th></tr>
  </thead>
  <tbody>
    <tr><td>Silla de comedor (asiento y respaldo)</td><td>3 – 5 ft²</td></tr>
    <tr><td>Silla con brazos (tipo office)</td><td>8 – 12 ft²</td></tr>
    <tr><td>Silla bergère completa</td><td>15 – 20 ft²</td></tr>
  </tbody>
</table>

<h3>Sillón individual</h3>
<table>
  <thead>
    <tr><th>Tipo</th><th>Piel aproximada</th></tr>
  </thead>
  <tbody>
    <tr><td>Sillón pequeño sin brazos</td><td>15 – 20 ft²</td></tr>
    <tr><td>Sillón estándar con brazos</td><td>25 – 35 ft²</td></tr>
    <tr><td>Sillón reclinable (lazy boy)</td><td>35 – 45 ft²</td></tr>
    <tr><td>Sillón de oreja (bergère grande)</td><td>40 – 50 ft²</td></tr>
  </tbody>
</table>

<h3>Sofá</h3>
<table>
  <thead>
    <tr><th>Tamaño</th><th>Piel aproximada</th></tr>
  </thead>
  <tbody>
    <tr><td>Sofá de 2 plazas</td><td>50 – 65 ft²</td></tr>
    <tr><td>Sofá de 3 plazas (estándar)</td><td>70 – 90 ft²</td></tr>
    <tr><td>Sofá esquinero (L)</td><td>100 – 130 ft²</td></tr>
    <tr><td>Sofá cama</td><td>80 – 100 ft²</td></tr>
  </tbody>
</table>

<h2>¿Cómo calcular tú mismo?</h2>
<p>Si el mueble no está en la tabla, sigue estos pasos:</p>
<ol>
  <li><strong>Mide cada superficie</strong> que vas a tapizar (en centímetros): largo × ancho.</li>
  <li><strong>Convierte a pies cuadrados:</strong> divide el resultado entre 929 (1 ft² = 929 cm²).</li>
  <li><strong>Suma todas las superficies.</strong></li>
  <li><strong>Agrega 15%</strong> de margen para cortes y desperdicios.</li>
</ol>
<p><strong>Ejemplo:</strong> Respaldo de 90 cm × 80 cm = 7,200 cm² ÷ 929 = 7.75 ft². Con 15% de margen: 7.75 × 1.15 = <strong>8.9 ft²</strong> para ese respaldo.</p>

<h2>Tips para no quedarte corto</h2>
<ul>
  <li><strong>Siempre pide un poco más.</strong> Es mejor tener un sobrante que interrumpir el trabajo a la mitad. Una hoja extra vale mucho menos que retrasar la entrega al cliente.</li>
  <li><strong>Pide de la misma partida.</strong> Los lotes de piel pueden variar ligeramente en tono. Si necesitas más después, puede que el color no coincida exactamente.</li>
  <li><strong>Considera el patrón.</strong> Si la piel tiene textura o patrón direccional (como algunas pieles grabadas), necesitarás más material para que las piezas queden alineadas.</li>
  <li><strong>Muebles con botones o capitoné</strong> requieren hasta un 20% más de piel por el material que se "come" el plisado.</li>
</ul>

<h2>¿Cuánta piel para un juego de sala completo?</h2>
<p>Si vas a tapizar un juego de sala (sofá de 3 plazas + 2 sillones), estima:</p>
<ul>
  <li>Sofá 3 plazas: ~80 ft²</li>
  <li>2 sillones estándar: ~60 ft² (30 c/u)</li>
  <li>Total: <strong>140 ft² aprox.</strong> — 3 hojas de piel de tamaño estándar (45–50 ft² c/u)</li>
</ul>

<h2>Compra tu piel en Maxipiel</h2>
<p>En <strong>Maxipiel</strong> vendemos piel genuina al mayoreo en León, Guanajuato, con envíos a todo México. Tenemos diferentes acabados, calibres y colores para tapicería de muebles, automotriz y marroquinería.</p>
<p><a href="https://maxipiel.com.mx/collections/materia-prima">Ver catálogo y precios →</a></p>
<p><em>¿Tienes un proyecto específico y no sabes cuánto pedir? Escríbenos con las medidas y te ayudamos a calcular exactamente lo que necesitas.</em></p>
"""
}

# ── Publicar los 3 ──────────────────────────────────────────────────────────
for i, blog in enumerate([blog1, blog2, blog3], 1):
    article_id, title = publish_article(blog)
    print(f"OK Blog {i} publicado - ID: {article_id} | {title}")
