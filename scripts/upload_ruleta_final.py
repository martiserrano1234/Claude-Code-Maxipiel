import sys, json, urllib.request
sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {"X-Shopify-Access-Token": "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"}
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

print(f"Bloque ruleta: {start+1} a {end}")

NEW_RULETA = (
    "    <!-- RULETA MAXIPIEL v2 -->\n"
    "    <div id=\"mx-overlay\" style=\"display:none;position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:99999;align-items:center;justify-content:center;padding:15px;\">\n"
    "      <div style=\"position:relative;background:#fff;border-radius:22px;padding:28px 22px 22px;max-width:380px;width:100%;text-align:center;box-shadow:0 24px 64px rgba(0,0,0,0.45);\">\n"
    "        <button onclick=\"mxClose()\" style=\"position:absolute;top:14px;right:16px;background:none;border:none;font-size:26px;cursor:pointer;color:#bbb;line-height:1;padding:0;\">&times;</button>\n"
    "        <h2 style=\"margin:0 0 3px;font-size:21px;color:#8B1A1A;font-weight:900;\">&#127920; ¡GIRA Y GANA!</h2>\n"
    "        <p style=\"margin:0 0 14px;color:#777;font-size:12px;\">Ingresa tu WhatsApp y obtén un descuento exclusivo</p>\n"
    "        <div style=\"position:relative;width:240px;margin:0 auto 14px;\">\n"
    "          <div style=\"position:absolute;top:-12px;left:50%;transform:translateX(-50%);width:0;height:0;border-left:10px solid transparent;border-right:10px solid transparent;border-top:20px solid #8B1A1A;z-index:10;\"></div>\n"
    "          <canvas id=\"mx-wheel\" width=\"240\" height=\"240\" style=\"border-radius:50%;box-shadow:0 4px 20px rgba(0,0,0,0.3);display:block;\"></canvas>\n"
    "        </div>\n"
    "        <div id=\"mx-state-form\">\n"
    "          <input id=\"mx-phone\" type=\"tel\" placeholder=\"Tu WhatsApp (10 digitos)\" style=\"width:100%;padding:12px;border:2px solid #ddd;border-radius:10px;font-size:15px;text-align:center;box-sizing:border-box;margin-bottom:10px;outline:none;\" maxlength=\"10\">\n"
    "          <button onclick=\"mxSpin()\" style=\"width:100%;padding:13px;background:linear-gradient(135deg,#8B1A1A,#C0392B);color:#fff;border:none;border-radius:10px;font-size:16px;font-weight:bold;cursor:pointer;\">¡GIRAR LA RULETA!</button>\n"
    "          <p style=\"font-size:11px;color:#ccc;margin:8px 0 0;\">Al participar aceptas recibir ofertas por WhatsApp</p>\n"
    "        </div>\n"
    "        <div id=\"mx-state-checking\" style=\"display:none;padding:20px 0;\">\n"
    "          <div style=\"font-size:32px;margin-bottom:8px;\">&#9203;</div>\n"
    "          <p style=\"color:#555;font-size:15px;margin:0;\">Un momento...</p>\n"
    "        </div>\n"
    "        <div id=\"mx-state-result\" style=\"display:none;\">\n"
    "          <div id=\"mx-confetti-area\" style=\"position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;overflow:hidden;border-radius:22px;\"></div>\n"
    "          <div style=\"background:#f9f9f9;border-radius:14px;padding:16px;margin-bottom:12px;\">\n"
    "            <p style=\"margin:0 0 4px;font-size:14px;color:#666;\">&#127881; ¡Felicidades! Ganaste:</p>\n"
    "            <p id=\"mx-prize-name\" style=\"margin:0 0 10px;font-size:22px;font-weight:900;color:#8B1A1A;\"></p>\n"
    "            <p style=\"margin:0 0 6px;font-size:12px;color:#999;\">Usa este codigo al pagar:</p>\n"
    "            <div style=\"background:#fff;border:2px dashed #8B1A1A;border-radius:10px;padding:12px;margin-bottom:10px;\">\n"
    "              <span id=\"mx-prize-code\" style=\"font-size:22px;font-weight:900;color:#8B1A1A;letter-spacing:3px;\"></span>\n"
    "            </div>\n"
    "            <button id=\"mx-copy-btn\" onclick=\"mxCopy()\" style=\"background:#27AE60;color:#fff;border:none;padding:9px 22px;border-radius:8px;cursor:pointer;font-size:14px;font-weight:bold;\">Copiar codigo</button>\n"
    "          </div>\n"
    "          <button onclick=\"mxClose()\" style=\"width:100%;padding:12px;background:#222;color:#fff;border:none;border-radius:10px;font-size:15px;cursor:pointer;font-weight:bold;\">Ir a la tienda</button>\n"
    "        </div>\n"
    "        <div id=\"mx-state-used\" style=\"display:none;padding:10px 0;\">\n"
    "          <div style=\"font-size:40px;margin-bottom:8px;\">&#128683;</div>\n"
    "          <p style=\"font-size:16px;font-weight:bold;color:#8B1A1A;margin:0 0 8px;\">Ya participaste anteriormente</p>\n"
    "          <p style=\"font-size:13px;color:#777;margin:0 0 14px;\">Solo se permite un giro por numero de WhatsApp.</p>\n"
    "          <button onclick=\"mxClose()\" style=\"width:100%;padding:12px;background:#222;color:#fff;border:none;border-radius:10px;font-size:15px;cursor:pointer;font-weight:bold;\">Ir a la tienda</button>\n"
    "        </div>\n"
    "      </div>\n"
    "    </div>\n"
    "    <script>\n"
    "    (function() {\n"
    "      var COOKIE = 'mx_spin=1';\n"
    "      var WEBHOOK = 'https://primary-production-dc7a.up.railway.app/webhook/ruleta-maxipiel-v2';\n"
    "      var shown = false, wonCode = '', spinning = false;\n"
    "      var prizes = [\n"
    "        { label: '5% OFF',       color: '#2980B9' },\n"
    "        { label: 'Envio Gratis', color: '#8E44AD' },\n"
    "        { label: '10% OFF',      color: '#C0392B' },\n"
    "        { label: '15% OFF',      color: '#27AE60' },\n"
    "        { label: 'Envio Gratis', color: '#8B1A1A' },\n"
    "        { label: '20% OFF',      color: '#E67E22' }\n"
    "      ];\n"
    "      var n = prizes.length, arc = (2*Math.PI)/n;\n"
    "      function draw(rot) {\n"
    "        var canvas=document.getElementById('mx-wheel'); if(!canvas) return;\n"
    "        var ctx=canvas.getContext('2d'), cx=canvas.width/2, cy=canvas.height/2, r=cx-4;\n"
    "        ctx.clearRect(0,0,canvas.width,canvas.height);\n"
    "        prizes.forEach(function(p,i){\n"
    "          var a1=rot+i*arc,a2=a1+arc;\n"
    "          ctx.beginPath();ctx.moveTo(cx,cy);ctx.arc(cx,cy,r,a1,a2);ctx.closePath();\n"
    "          ctx.fillStyle=p.color;ctx.fill();ctx.strokeStyle='#fff';ctx.lineWidth=2;ctx.stroke();\n"
    "          ctx.save();ctx.translate(cx,cy);ctx.rotate(a1+arc/2);\n"
    "          ctx.textAlign='right';ctx.fillStyle='#fff';ctx.font='bold 11px Arial';\n"
    "          ctx.fillText(p.label,r-8,4);ctx.restore();\n"
    "        });\n"
    "        ctx.beginPath();ctx.arc(cx,cy,18,0,2*Math.PI);ctx.fillStyle='#fff';ctx.fill();\n"
    "      }\n"
    "      function setState(s) {\n"
    "        ['form','checking','result','used'].forEach(function(id){\n"
    "          var el=document.getElementById('mx-state-'+id);\n"
    "          if(el) el.style.display=(id===s)?'block':'none';\n"
    "        });\n"
    "      }\n"
    "      function showOverlay() {\n"
    "        if(shown||document.cookie.indexOf(COOKIE)>-1) return;\n"
    "        shown=true;\n"
    "        var ov=document.getElementById('mx-overlay'); if(!ov) return;\n"
    "        ov.style.display='flex'; setState('form'); draw(0);\n"
    "      }\n"
    "      if(window.location.pathname==='/cart'){setTimeout(showOverlay,800);}\n"
    "      var observer=new MutationObserver(function(){\n"
    "        ['cart-drawer','#CartDrawer','[data-cart-drawer]','.cart-drawer','.drawer--cart'].forEach(function(sel){\n"
    "          var el=document.querySelector(sel);if(!el)return;\n"
    "          var open=el.hasAttribute('open')||el.getAttribute('aria-hidden')==='false'||el.classList.contains('active')||el.classList.contains('open')||el.classList.contains('is-open');\n"
    "          if(open)setTimeout(showOverlay,500);\n"
    "        });\n"
    "      });\n"
    "      observer.observe(document.body,{attributes:true,childList:true,subtree:true});\n"
    "      document.addEventListener('cart:open',function(){setTimeout(showOverlay,400);});\n"
    "      document.addEventListener('on:cart-drawer:open',function(){setTimeout(showOverlay,400);});\n"
    "      window.mxSpin=function(){\n"
    "        if(spinning)return;\n"
    "        var phone=document.getElementById('mx-phone').value.replace(/\\D/g,'');\n"
    "        var inp=document.getElementById('mx-phone');\n"
    "        if(phone.length<10){inp.style.borderColor='#e74c3c';inp.placeholder='Ingresa tus 10 digitos';return;}\n"
    "        inp.style.borderColor='#27AE60'; spinning=true; setState('checking');\n"
    "        fetch(WEBHOOK,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:'52'+phone})})\n"
    "        .then(function(r){return r.json();})\n"
    "        .then(function(res){\n"
    "          if(res.status==='already_used'){spinning=false;setState('used');return;}\n"
    "          wonCode=res.code||''; var lbl=res.prize_label||'';\n"
    "          var idx=0; for(var i=0;i<prizes.length;i++){if(prizes[i].label===lbl){idx=i;break;}}\n"
    "          setState('form');document.getElementById('mx-state-form').style.display='none';\n"
    "          spinWheel(idx,lbl,wonCode);\n"
    "        }).catch(function(){spinning=false;setState('form');});\n"
    "      };\n"
    "      function spinWheel(idx,label,code){\n"
    "        var tr=-Math.PI/2-idx*arc-arc/2,norm=((tr%(2*Math.PI))+2*Math.PI)%(2*Math.PI),fr=norm+8*2*Math.PI;\n"
    "        var st=performance.now(),dur=5200;\n"
    "        function animate(now){var t=Math.min((now-st)/dur,1),e=1-Math.pow(1-t,4);draw(fr*e);\n"
    "          if(t<1){requestAnimationFrame(animate);}else{\n"
    "            spinning=false;document.cookie=COOKIE+';max-age='+(60*60*24*60)+';path=/';\n"
    "            document.getElementById('mx-prize-name').textContent=label;\n"
    "            document.getElementById('mx-prize-code').textContent=code;\n"
    "            setState('result');launchConfetti();}}\n"
    "        requestAnimationFrame(animate);\n"
    "      }\n"
    "      function launchConfetti(){\n"
    "        var area=document.getElementById('mx-confetti-area');if(!area)return;\n"
    "        var colors=['#8B1A1A','#C0392B','#F39C12','#27AE60','#2980B9','#8E44AD','#fff'];\n"
    "        for(var i=0;i<60;i++){(function(idx){setTimeout(function(){\n"
    "          var c=document.createElement('div'),sz=6+Math.random()*8;\n"
    "          c.style.cssText='position:absolute;width:'+sz+'px;height:'+sz+'px;background:'+colors[Math.floor(Math.random()*colors.length)]+';border-radius:'+(Math.random()>.5?'50%':'2px')+';top:-10px;left:'+(Math.random()*100)+'%;';\n"
    "          area.appendChild(c);\n"
    "          var dx=(Math.random()-.5)*80,dy=80+Math.random()*200,rot=Math.random()*720,s2=performance.now();\n"
    "          function fall(n2){var t=Math.min((n2-s2)/1800,1);c.style.transform='translate('+dx*t+'px,'+dy*t+'px) rotate('+rot*t+'deg)';c.style.opacity=String(1-t);if(t<1)requestAnimationFrame(fall);else c.remove();}\n"
    "          requestAnimationFrame(fall);\n"
    "        },idx*25);})(i);}\n"
    "      }\n"
    "      window.mxCopy=function(){\n"
    "        var btn=document.getElementById('mx-copy-btn');\n"
    "        var restore=function(){btn.textContent='Copiar codigo';btn.style.background='#27AE60';};\n"
    "        navigator.clipboard.writeText(wonCode).then(function(){btn.textContent='Copiado!';btn.style.background='#1a7a40';setTimeout(restore,2000);}).catch(function(){var tmp=document.createElement('textarea');tmp.value=wonCode;document.body.appendChild(tmp);tmp.select();document.execCommand('copy');tmp.remove();btn.textContent='Copiado!';setTimeout(restore,2000);});\n"
    "      };\n"
    "      window.mxClose=function(){var ov=document.getElementById('mx-overlay');if(ov)ov.style.display='none';};\n"
    "    })();\n"
    "    </script>"
)

new_lines = lines[:start] + [NEW_RULETA] + lines[end:]
new_content = '\n'.join(new_lines)

payload = json.dumps({"asset":{"key":"layout/theme.liquid","value":new_content}}).encode('utf-8')
put_req = urllib.request.Request(
    "https://maxipiel.myshopify.com/admin/api/2024-01/themes/144344481892/assets.json",
    data=payload, headers={**HEADERS,"Content-Type":"application/json"}, method="PUT"
)
with urllib.request.urlopen(put_req) as r:
    resp = json.load(r)
    print("Subido OK:", resp['asset']['updated_at'])
