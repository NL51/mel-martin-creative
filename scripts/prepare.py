import json,base64
from pathlib import Path
p=Path(__file__).resolve().parent.parent
html=(p/'src/index.html').read_text()
assets={}
for f in (p/'assets').iterdir():
 assets['/assets/'+f.name]={'data':base64.b64encode(f.read_bytes()).decode(),'type':'image/png' if f.suffix=='.png' else 'image/jpeg'}
if (p/'assets/share.jpg').exists(): assets['/share.jpg']=assets['/assets/share.jpg']
(p/'worker/index.js').write_text('const HTML='+json.dumps(html)+';\nconst ASSETS='+json.dumps(assets)+';\n'+(p/'src/server.js').read_text())
(p/'.openai/hosting.json').write_text(json.dumps({'project_id':'appgprj_6ad980f4b65481919bed6c005bc9655b','d1':None,'r2':'BUCKET'},indent=2))
