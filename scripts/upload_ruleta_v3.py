import sys, json, urllib.request
sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {"X-Shopify-Access-Token": "TU_SHOPIFY_TOKEN"}

url = "https://maxipiel.myshopify.com/admin/api/2024-01/themes/144344481892/assets.json?asset[key]=layout/theme.liquid"
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req) as r:
    data = json.load(r)

content = data['asset']['value']
lines = content.split('\n')

start = None
end = None
for i, l in enumerate(lines):
    if '<!-- RULETA MAXIPIEL v2 -->' in l:
        start = i
    if start and i > start and '</script>' in l and end is None:
        end = i + 1

print(f"Ruleta block: lines {start+1} to {end}")

NEW_RULETA = '''    <!-- RULETA MAXIPIEL v2 -->
    <div id="mx-overlay" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:99999;align-items:center;justify-content:center;padding:15px;">
      <div style="position:relative;background:#fff;border-radius:22px;padding:28px 22px 22px;max-width:380px;width:100%;text-align:center;box-shadow:0 24px 64px rgba(0,0,0,0.45);">

        <button onclick="mxClose()" style="position:absolute;top:14px;right:16px;background:none;border:none;font-size:26px;cursor:pointer;color:#bbb;line-height:1;padding:0;">&times;</button>

        <h2 style="margin:0 0 3px;font-size:21px;color:#8B1A1A;font-weight:900;">&#127920; ¡GIRA Y GANA!</h2>
        <p style="margin:0 0 14px;color:#777;font-size:12px;">Ingresa tu WhatsApp y obtén un descuento exclusivo</p>

        <div style="position:relative;width:240px;margin:0 auto 14px;">
          <div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);width:0;height:0;border-left:10px solid transparent;border-right:10px solid transparent;border-top:20px solid #8B1A1A;z-index:10;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.3));"></div>
          <canvas id="mx-wheel" width="240" height="240" style="border-radius:50%;box-shadow:0 4px 20px rgba(0,0,0,0.3);display:block;"></canvas>
        </div>

        <div id="mx-state-form">
          <input id="mx-phone" type="tel" placeholder="Tu WhatsApp (10 digitos)"
            style="width:100%;padding:12px;border:2px solid #ddd;border-radius:10px;font-size:15px;text-align:center;box-sizing:border-box;margin-bottom:10px;outline:none;"
            maxlength="10" oninput="this.value=this.value.replace(/\D/g,\x27\x27)">
          <button onclick="mxSpin()"
            style="width:100%;padding:13px;background:linear-gradient(135deg,#8B1A1A,#C0392B);color:#fff;border:none;border-radius:10px;font-size:16px;font-weight:bold;cursor:pointer;letter-spacing:1px;">
            ¡GIRAR LA RULETA!
          </button>
          <p style="font-size:11px;color:#ccc;margin:8px 0 0;">Al participar aceptas recibir ofertas por WhatsApp</p>
        </div>

        <div id="mx-state-result" style="display:none;">
          <div id="mx-confetti-area" style="position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;overflow:hidden;border-radius:22px;"></div>
          <div style="background:#f9f9f9;border-radius:14px;padding:16px;margin-bottom:12px;">
            <p style="margin:0 0 4px;font-size:14px;color:#666;">&#127881; ¡Felicidades! Ganaste:</p>
            <p id="mx-prize-name" style="margin:0 0 10px;font-size:22px;font-weight:900;color:#8B1A1A;"></p>
            <p style="margin:0 0 6px;font-size:12px;color:#999;">Usa este codigo al pagar:</p>
            <div style="background:#fff;border:2px dashed #8B1A1A;border-radius:10px;padding:12px;margin-bottom:10px;">
              <span id="mx-prize-code" style="font-size:22px;font-weight:900;color:#8B1A1A;letter-spacing:3px;"></span>
            </div>
            <button id="mx-copy-btn" onclick="mxCopy()" style="background:#27AE60;color:#fff;border:none;padding:9px 22px;border-radius:8px;cursor:pointer;font-size:14px;font-weight:bold;">Copiar codigo</button>
          </div>
          <button onclick="mxClose()" style="width:100%;padding:12px;background:#222;color:#fff;border:none;border-radius:10px;font-size:15px;cursor:pointer;font-weight:bold;">Ir a la tienda</button>
        </div>

      </div>
    </div>

    <script>
    (function() {
      var COOKIE = 'mx_spin=1';
      var shown = false;
      var wonCode = '';

      var prizes = [
        { label: '5% OFF',       code: 'RUEDA5',        color: '#2980B9', weight: 30 },
        { label: 'Envio Gratis', code: 'MAXIPIELENVIO', color: '#8E44AD', weight: 20 },
        { label: '10% OFF',      code: 'RUEDA10',       color: '#C0392B', weight: 25 },
        { label: '15% OFF',      code: 'RUEDA15',       color: '#27AE60', weight: 15 },
        { label: 'Envio Gratis', code: 'MAXIPIELENVIO', color: '#8B1A1A', weight:  7 },
        { label: '20% OFF',      code: 'RUEDA20',       color: '#E67E22', weight:  3 }
      ];
      var totalWeight = prizes.reduce(function(s,p){ return s+p.weight; }, 0);
      var n = prizes.length;
      var arc = (2 * Math.PI) / n;
      var spinning = false;

      function weightedRandom() {
        var r = Math.random() * totalWeight;
        for (var i = 0; i < prizes.length; i++) { r -= prizes[i].weight; if (r <= 0) return i; }
        return prizes.length - 1;
      }

      function draw(rot) {
        var canvas = document.getElementById('mx-wheel');
        if (!canvas) return;
        var ctx = canvas.getContext('2d');
        var cx = canvas.width/2, cy = canvas.height/2, r = cx - 4;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        prizes.forEach(function(p, i) {
          var a1 = rot + i*arc, a2 = a1 + arc;
          ctx.beginPath(); ctx.moveTo(cx,cy); ctx.arc(cx,cy,r,a1,a2); ctx.closePath();
          ctx.fillStyle = p.color; ctx.fill();
          ctx.strokeStyle = '#fff'; ctx.lineWidth = 2; ctx.stroke();
          ctx.save(); ctx.translate(cx,cy); ctx.rotate(a1+arc/2);
          ctx.textAlign = 'right'; ctx.fillStyle = '#fff'; ctx.font = 'bold 11px Arial';
          ctx.fillText(p.label, r-8, 4); ctx.restore();
        });
        ctx.beginPath(); ctx.arc(cx,cy,18,0,2*Math.PI); ctx.fillStyle='#fff'; ctx.fill();
      }

      function setState(s) {
        ['form','result'].forEach(function(id) {
          var el = document.getElementById('mx-state-' + id);
          if (el) el.style.display = (id === s) ? 'block' : 'none';
        });
      }

      function showOverlay() {
        if (shown || document.cookie.indexOf(COOKIE) > -1) return;
        shown = true;
        var ov = document.getElementById('mx-overlay');
        if (!ov) return;
        ov.style.display = 'flex';
        setState('form');
        draw(0);
      }

      if (window.location.pathname === '/cart') { setTimeout(showOverlay, 800); }

      var observer = new MutationObserver(function() {
        var selectors = ['cart-drawer','#CartDrawer','[data-cart-drawer]','.cart-drawer','.drawer--cart'];
        selectors.forEach(function(sel) {
          var el = document.querySelector(sel);
          if (!el) return;
          var open = el.hasAttribute('open') || el.getAttribute('aria-hidden')==='false' ||
                     el.classList.contains('active') || el.classList.contains('open') || el.classList.contains('is-open');
          if (open) setTimeout(showOverlay, 500);
        });
      });
      observer.observe(document.body, { attributes: true, childList: true, subtree: true });
      document.addEventListener('cart:open', function() { setTimeout(showOverlay, 400); });
      document.addEventListener('on:cart-drawer:open', function() { setTimeout(showOverlay, 400); });

      window.mxSpin = function() {
        if (spinning) return;
        var phone = document.getElementById('mx-phone').value.replace(/\D/g,'');
        var inp = document.getElementById('mx-phone');
        if (phone.length < 10) {
          inp.style.borderColor = '#e74c3c';
          inp.placeholder = 'Ingresa tus 10 digitos';
          return;
        }
        inp.style.borderColor = '#27AE60';
        spinning = true;

        var prizeIndex = weightedRandom();
        var prize = prizes[prizeIndex];
        wonCode = prize.code;

        fetch('https://primary-production-dc7a.up.railway.app/webhook/ruleta-maxipiel', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ phone: '52'+phone, premio: prize.label, codigo: prize.code })
        }).catch(function(){});

        var targetRot = -Math.PI/2 - prizeIndex*arc - arc/2;
        var norm = ((targetRot % (2*Math.PI)) + 2*Math.PI) % (2*Math.PI);
        var finalRot = norm + 8*2*Math.PI;
        var start = performance.now();
        var duration = 5200;

        function animate(now) {
          var t = Math.min((now-start)/duration, 1);
          var ease = 1 - Math.pow(1-t, 4);
          draw(finalRot * ease);
          if (t < 1) { requestAnimationFrame(animate); }
          else {
            spinning = false;
            document.cookie = COOKIE + ';max-age='+(60*60*24*60)+';path=/';
            document.getElementById('mx-prize-name').textContent = prize.label;
            document.getElementById('mx-prize-code').textContent = prize.code;
            setState('result');
            launchConfetti();
          }
        }
        requestAnimationFrame(animate);
      };

      function launchConfetti() {
        var area = document.getElementById('mx-confetti-area');
        if (!area) return;
        var colors = ['#8B1A1A','#C0392B','#F39C12','#27AE60','#2980B9','#8E44AD','#fff'];
        for (var i = 0; i < 60; i++) {
          (function(idx) {
            setTimeout(function() {
              var c = document.createElement('div');
              var size = 6 + Math.random()*8;
              c.style.cssText = 'position:absolute;width:'+size+'px;height:'+size+'px;background:'+colors[Math.floor(Math.random()*colors.length)]+';border-radius:'+(Math.random()>.5?'50%':'2px')+';top:-10px;left:'+(Math.random()*100)+'%;';
              area.appendChild(c);
              var dx=(Math.random()-.5)*80, dy=80+Math.random()*200, rot=Math.random()*720, s2=performance.now();
              function fall(now2) {
                var t=Math.min((now2-s2)/1800,1);
                c.style.transform='translate('+dx*t+'px,'+dy*t+'px) rotate('+rot*t+'deg)';
                c.style.opacity=String(1-t);
                if(t<1) requestAnimationFrame(fall); else c.remove();
              }
              requestAnimationFrame(fall);
            }, idx*25);
          })(i);
        }
      }

      window.mxCopy = function() {
        var btn = document.getElementById('mx-copy-btn');
        var restore = function() { btn.textContent = 'Copiar codigo'; btn.style.background='#27AE60'; };
        navigator.clipboard.writeText(wonCode).then(function() {
          btn.textContent = 'Copiado!'; btn.style.background='#1a7a40';
          setTimeout(restore, 2000);
        }).catch(function() {
          var tmp=document.createElement('textarea'); tmp.value=wonCode;
          document.body.appendChild(tmp); tmp.select(); document.execCommand('copy'); tmp.remove();
          btn.textContent = 'Copiado!'; setTimeout(restore, 2000);
        });
      };

      window.mxClose = function() {
        var ov = document.getElementById('mx-overlay');
        if (ov) ov.style.display = 'none';
      };
    })();
    </script>'''

new_lines = lines[:start] + [NEW_RULETA] + lines[end:]
new_content = '\n'.join(new_lines)

payload = json.dumps({"asset": {"key": "layout/theme.liquid", "value": new_content}}).encode('utf-8')
put_req = urllib.request.Request(
    "https://maxipiel.myshopify.com/admin/api/2024-01/themes/144344481892/assets.json",
    data=payload,
    headers={**HEADERS, "Content-Type": "application/json"},
    method="PUT"
)
with urllib.request.urlopen(put_req) as r:
    resp = json.load(r)
    print("Subido OK:", resp['asset']['updated_at'])
