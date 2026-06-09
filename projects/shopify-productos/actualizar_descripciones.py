import urllib.request, json, time

TOKEN = 'TU_SHOPIFY_TOKEN'
SHOP = 'maxipiel.myshopify.com'

# (id, nombre_color, descripcion_color, usos)
productos = [
    (8504430755940, 'Azul Aqua', 'fresco y moderno', 'interiores que llaman la atención. Ideal para tapiceros que buscan diferenciarse con un color atrevido y actual.'),
    (8504430788708, 'Café', 'cálido y versátil', 'cualquier tipo de proyecto: autos, salas, comedores. El café clásico nunca falla y siempre luce bien.'),
    (8504430854244, 'Café Oxford', 'con textura Oxford que da profundidad y carácter', 'proyectos donde quieres un acabado más sofisticado. La textura Oxford aporta personalidad sin perder elegancia.'),
    (8504430887012, 'Camel', 'beige dorado elegante', 'interiores que buscan calidez y lujo. El camel es el color de los autos premium y las salas de diseño.'),
    (8504430952548, 'Chedron Arena', 'terracota con toques de arena, muy exclusivo', 'tapicerías con carácter. Un color poco común que hace que el trabajo del tapicero destaque de inmediato.'),
    (8504430985316, 'Chedron Terracota', 'tono ladrillo cálido con gran profundidad', 'espacios con estilo rústico moderno o autos con personalidad propia. Un color que siempre genera comentarios.'),
    (8504431018084, 'Conac', 'ámbar dorado clásico de la tapicería de lujo', 'autos de colección, salas clásicas o cualquier proyecto donde el cliente quiere algo que se vea exclusivo.'),
    (8504431050852, 'Gris', 'neutro moderno, el más pedido en tapicería automotriz', 'cualquier auto o mueble moderno. El gris combina con todo y siempre luce limpio y profesional.'),
    (8502204825700, 'Gris Oscuro', 'tono profundo y sofisticado', 'interiores oscuros y elegantes. Excelente para autos deportivos o salas con estilo minimalista.'),
    (8504431083620, 'Gris Oxford', 'gris con textura Oxford para mayor distinción', 'proyectos donde el cliente quiere diferenciarse. La textura hace que el trabajo del tapicero luzca más fino.'),
    (8504431149156, 'Hueso', 'blanco roto que irradia lujo y amplitud', 'interiores de alto nivel. El hueso hace que los espacios se vean más amplios y limpios — muy pedido en autos de lujo.'),
    (8504431214692, 'King Ranch', 'acabado estilo western premium', 'tapicerías que buscan ese look texano distintivo. Un clásico que nunca pasa de moda y que los clientes reconocen de inmediato.'),
    (8504431247460, 'Miel', 'dorado cálido que recuerda a la miel natural', 'proyectos cálidos y acogedores. El miel da vida a cualquier interior y complementa madera natural perfectamente.'),
    (8504431345764, 'Negro Fondo Azul', 'negro con matices azules al cambio de luz — efecto único', 'tapicerías exclusivas donde el detalle importa. Un color que sorprende y que pocos proveedores tienen.'),
    (8504431378532, 'Negro Fondo Gris', 'negro suavizado con base gris — más cálido que el negro puro', 'interiores oscuros que no quieren verse tan severos. El fondo gris lo hace más amigable sin perder estilo.'),
    (8504431411300, 'Negro Grabado Italiano', 'negro con grabado italiano — acabado premium', 'cuando el cliente quiere lo mejor. El grabado italiano le da una textura de alta gama que distingue el trabajo.'),
    (8504431312996, 'Negro Semi-liso', 'negro clásico entre mate y brillante — el más pedido', 'todo tipo de proyectos. El negro semi-liso es el caballo de batalla del tapicero: combina con todo y siempre queda bien.'),
    (8502207152228, 'Oxblood', 'borgoña oscuro con matices rojizos — color clásico de la industria', 'tapicerías clásicas o vintage. El oxblood es un color de coleccionista que los clientes exigentes piden por nombre.'),
    (8504431509604, 'Plateado Obscuro', 'acabado metálico profundo de alto impacto visual', 'proyectos que buscan destacar. El plateado oscuro funciona muy bien en autos modificados y salas de diseño moderno.'),
    (8504431542372, 'Rojo Ferrari', 'el rojo más icónico de la industria automotriz', 'cuando el cliente quiere impactar. Intenso, vibrante y sin compromiso — el rojo que todo mundo reconoce.'),
    (8504431575140, 'Rojo Quemado', 'rojo oscuro con tonos anaranjados cálidos', 'tapicerías con personalidad. Más sofisticado que el rojo brillante, con una profundidad que luce increíble en cuero genuino.'),
    (8504431607908, 'Uva', 'morado oscuro con tonos berenjena elegantes', 'proyectos audaces y sofisticados. Un color que pocos tapiceros ofrecen y que hace que el trabajo destaque completamente.'),
    (8504431640676, 'Vino', 'borgoña profundo — clásico de la tapicería de lujo', 'salas clásicas, autos de colección o cualquier proyecto donde el cliente quiere elegancia atemporal.'),
    (8504431673444, 'Vino Chocolate', 'fusión de borgoña y tonos cacao — combinación única', 'tapicerías cálidas y originales. Un color que no se consigue en cualquier lugar y que los clientes van a recordar.'),
]


def hacer_descripcion(nombre_color, descripcion_color, usos):
    import urllib.parse
    nombre_color_encoded = urllib.parse.quote(nombre_color)
    return f"""<div style="font-family: sans-serif; max-width: 700px; color: #2d2d2d;">

<h2 style="color: #1a1a1a;">Cuero Top Grain {nombre_color} — Piel Genuina para Tapiceros</h2>

<p>Piel genuina de grado automotriz, {descripcion_color}. Pensada para {usos}</p>

<h3>¿Cuánto cubre cada presentación?</h3>
<ul>
  <li><strong>Medio Cuero (media hoja)</strong> — aproximadamente <strong>250 dm²</strong>. Ideal para un asiento de auto completo, una silla tapizada o proyectos chicos.</li>
  <li><strong>Cuero Entero (hoja completa)</strong> — aproximadamente <strong>500 dm²</strong>. Para sofás de 2 a 3 lugares, tapicería de auto completa o proyectos grandes.</li>
</ul>

<h3>¿Para qué sirve?</h3>
<ul>
  <li>Tapicería automotriz: asientos, tablero, puertas, volante</li>
  <li>Muebles: sofás, sillas, cabeceras, sillones</li>
  <li>Accesorios: bolsas, carteras, fundas</li>
</ul>

<h3>Características del material</h3>
<ul>
  <li>Piel genuina <strong>Top Grain</strong> — resistente y duradera para uso diario</li>
  <li>Grado automotriz: soporta calor, fricción y uso constante</li>
  <li>Fácil de limpiar y mantener</li>
  <li>Envío nacional desde León, Guanajuato</li>
</ul>

<p style="background: #f5f5f5; padding: 12px; border-radius: 6px; margin-top: 16px;">
  <strong>¿Tienes dudas sobre la cantidad o el color?</strong><br>
  Escríbenos por WhatsApp y te ayudamos a calcular exactamente lo que necesitas para tu proyecto.<br>
  <a href="https://wa.me/524791424121?text=Hola%20Maxipiel%2C%20me%20interesa%20el%20Cuero%20Top%20Grain%20{nombre_color_encoded}%2C%20%C2%BFpueden%20ayudarme%3F" style="display: inline-block; margin-top: 8px; background: #25D366; color: white; padding: 10px 18px; border-radius: 5px; text-decoration: none; font-weight: bold;">Escríbenos por WhatsApp</a><br>
  <small>Lunes a Sábado de 9am a 6pm</small>
</p>

</div>"""


print(f"Actualizando {len(productos)} productos...\n")

errores = []
for pid, color, desc_color, usos in productos:
    html = hacer_descripcion(color, desc_color, usos)
    payload = json.dumps({'product': {'id': pid, 'body_html': html}}).encode('utf-8')
    url = f'https://{SHOP}/admin/api/2024-01/products/{pid}.json'
    req = urllib.request.Request(url, data=payload, method='PUT')
    req.add_header('X-Shopify-Access-Token', TOKEN)
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req) as r:
            resp = json.load(r)
            print(f"OK: {resp['product']['title']}")
    except Exception as e:
        print(f"ERROR {pid} ({color}): {e}")
        errores.append((pid, color))
    time.sleep(0.5)

print(f"\nCompletado. Errores: {len(errores)}")
if errores:
    print("Con error:", errores)
