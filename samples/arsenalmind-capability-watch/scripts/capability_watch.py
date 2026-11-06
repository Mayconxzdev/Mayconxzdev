#!/usr/bin/env python3
"""Radar aberto, somente metadados públicos; sem instalação/execução de terceiros.
Execução: py scripts/capability_watch.py scan --query 'coding agent' --query 'MCP security'
Offline: py scripts/capability_watch.py report
Testes: py -m unittest discover -s tests_v23 -v
"""
from __future__ import annotations
import argparse, datetime as dt, html, json, os, re, sqlite3, sys, time
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

UA='ArsenalMind-CapabilityWatch/2.3 (metadata-only; no-auto-install)'
SEEDS=["agent skills", "AI agent quality assurance", "MCP tools", "software engineering automation", "AI evaluation", "agent security", "open source creative tools", "developer productivity", "workflow orchestration", "accessibility testing", "AI video generation", "agent interoperability", "data quality", "computer use agents"]
CUTOFF_DAYS=14

def data_home():
    root=os.environ.get('ARSENALMIND_DATA_DIR')
    if root: return Path(root).expanduser()/'capability-watch'
    if sys.platform=='win32': return Path(os.environ.get('LOCALAPPDATA',str(Path.home()/'AppData'/'Local')))/'ArsenalMind'/'capability-watch'
    return Path(os.environ.get('XDG_STATE_HOME',str(Path.home()/'.local'/'state')))/'arsenalmind'/'capability-watch'

def fetch(url,timeout=9):
    if urlparse(url).hostname not in ('api.github.com','hn.algolia.com'): raise ValueError('Host nao permitido')
    req=Request(url,headers={'User-Agent':UA,'Accept':'application/json'})
    with urlopen(req,timeout=timeout) as res:
        size=min(1_000_000,int(res.headers.get('Content-Length','1000000') or '1000000'))
        raw=res.read(size+1)
        if len(raw)>1_000_000: raise ValueError('Resposta maior que limite')
        return json.loads(raw)

def github_items(obj):
    out=[]
    for r in obj.get('items',[])[:25]:
        name=r.get('full_name')
        if not name or r.get('fork') or r.get('archived'): continue
        out.append({'id':'gh:'+name.lower(),'title':name,'url':r.get('html_url',''),'description':(r.get('description') or '')[:400],
                    'source':'github-search','stars':int(r.get('stargazers_count',0)),'forks':int(r.get('forks_count',0)),
                    'updated':r.get('pushed_at'),'created':r.get('created_at'),'language':r.get('language') or '',
                    'license':((r.get('license') or {}).get('spdx_id') or 'UNKNOWN'),
                    'open_issues':r.get('open_issues_count',0),'homepage':r.get('homepage') or ''})
    return out

def hn_items(obj):
    out=[]
    for h in obj.get('hits',[])[:20]:
        title=html.unescape(h.get('title') or h.get('story_title') or '').strip()
        u=h.get('url') or h.get('story_url')
        if not title or not u or not u.startswith('https://'):continue
        uid=str(h.get('objectID') or u)
        out.append({'id':'hn:'+uid,'title':title[:180],'url':u,'description':'Discussao na comunidade Hacker News — nao verificado',
                    'source':'hacker-news','stars':None,'points':h.get('points') or 0,'comments':h.get('num_comments') or 0,
                    'updated':h.get('created_at'),'created':h.get('created_at'),'license':'UNKNOWN'})
    return out

def initdb(db):
    db.execute('create table if not exists sightings (id text primary key, title text, url text, source text, description text, first_seen text, last_seen text, stars integer, previous_stars integer, previous_seen text, payload text)')
    db.execute('create table if not exists runs (started text, result text, queries text, errors text)')

def record(db,records,at):
    count=0
    for r in records:
        old=db.execute('select first_seen,stars,last_seen,previous_stars,previous_seen from sightings where id=?',(r['id'],)).fetchone()
        # Distinguish delta observed in this tool from guessed popularity trends.
        first=old[0] if old else at
        prev_stars=old[1] if old else None
        prev_seen=old[2] if old else None
        db.execute('insert or replace into sightings values(?,?,?,?,?,?,?,?,?,?,?)',
                   (r['id'],r['title'],r['url'],r['source'],r.get('description',''),first,at,r.get('stars'),prev_stars,prev_seen,json.dumps(r,ensure_ascii=False)))
        count+=1
    db.commit();return count

def clean_terms(text):
    # Never submit raw private project text. Only explicit CLI queries or generic seeds.
    raw=str(text).lower()
    for secret in ('password','token=','api_key','sk-','ghp_','@'):
        if secret in raw: raise ValueError('Consulta pode conter um segredo')
    s=re.sub(r'[^\w\s+.-]',' ',text,flags=re.U).strip()
    if not s or len(s)>110: raise ValueError('Consulta vazia ou longa demais')
    return s

def rank(row,focus=''):
    r=json.loads(row['payload'])
    words=set(re.findall(r'[a-z0-9]+',focus.lower()))-{'and','de','para','with','the'}
    txt=(r['title']+' '+r['description']).lower()
    relevance=sum(1 for x in words if x in txt)/(len(words) or 1)
    stars=r.get('stars') or 0
    from math import log1p
    popularity=min(1,log1p(stars)/log1p(20000)) if stars else 0
    growth=None
    if row['previous_stars'] is not None and r.get('stars') is not None and row['previous_seen']:
        hours=(dt.datetime.fromisoformat(row['last_seen'])-dt.datetime.fromisoformat(row['previous_seen'])).total_seconds()/3600
        if hours>=1: growth=round((stars-row['previous_stars'])*24/hours,2)
    # signals are prioritization, not endorsement of quality/safety
    score=round(0.68*relevance+0.17*popularity+0.15*min(1,max(0,(growth or 0))/100),3)
    return score,growth,relevance

def report(db,focus='',limit=30):
    db.row_factory=sqlite3.Row
    rows=db.execute('select * from sightings').fetchall()
    results=[]
    for row in rows:
        score,growth,rel=rank(row,focus)
        item=json.loads(row['payload'])
        item.update({'first_seen':row['first_seen'],'last_seen':row['last_seen'],'observed_star_gain_per_day':growth,
                     'ranking_signal':score,'query_relevance':round(rel,3),
                     'verification':'UNVERIFIED','security':'NOT_SCANNED','installation':'NOT_INSTALLED',
                     'notes':'Sinais de atencao nao comprovam qualidade, licenca ou seguranca. Revisao e teste obrigatorios.'})
        results.append(item)
    results.sort(key=lambda x:(x['ranking_signal'],x['last_seen']),reverse=True)
    return results[:limit]

def scan(db,queries,request_budget=8):
    now=dt.datetime.now(dt.timezone.utc)
    cutoff=(now-dt.timedelta(days=CUTOFF_DAYS)).strftime('%Y-%m-%d')
    found={}; errors=[]; requests=0
    for q in queries:
        if requests>=request_budget:break
        # new repos + updated active repos; bounded, query-specific, no user data by default
        for qualifier in (f'created:>={cutoff}',f'pushed:>={cutoff}'):
            if requests>=request_budget:break
            u='https://api.github.com/search/repositories?'+urlencode({'q':q+' '+qualifier,'sort':'stars' if 'created' in qualifier else 'updated','order':'desc','per_page':15})
            requests+=1
            try:
                for r in github_items(fetch(u)):found[r['id']]=r
            except (HTTPError,URLError,TimeoutError,ValueError,OSError) as e: errors.append({'source':'github','type':type(e).__name__,'query':q})
        if requests>=request_budget:break
        u='https://hn.algolia.com/api/v1/search?'+urlencode({'query':q,'tags':'story','hitsPerPage':12,'numericFilters':f'created_at_i>{int((now-dt.timedelta(days=30)).timestamp())}'})
        requests+=1
        try:
            for r in hn_items(fetch(u)):found[r['id']]=r
        except (HTTPError,URLError,TimeoutError,ValueError,OSError) as e: errors.append({'source':'hacker-news','type':type(e).__name__,'query':q})
    now_iso=now.isoformat();count=record(db,list(found.values()),now_iso)
    db.execute('insert into runs values(?,?,?,?)',(now_iso,'partial' if errors else 'ok',json.dumps(queries),json.dumps(errors)));db.commit()
    return {'at':now_iso,'status':'partial' if errors else 'ok','sources_requested':requests,'observations':count,'errors':errors}

def main(argv=None):
    ap=argparse.ArgumentParser(description='Radar de capacidades, somente leitura web e metadados locais, nunca instala skills')
    ap.add_argument('action',choices=['scan','report','doctor'])
    ap.add_argument('--query',action='append',default=[],help='termo publico (nao inclua segredos)')
    ap.add_argument('--limit',type=int,default=30)
    ap.add_argument('--budget',type=int,default=8)
    ap.add_argument('--output',help='caminho JSON explicitamente solicitado')
    a=ap.parse_args(argv)
    if a.action=='doctor':
        print(json.dumps({'python':sys.version.split()[0],'data_home':str(data_home()),'network_for_scan':True,'automatic_install':False,'sources':['github-search','hacker-news'], 'state':'operational-code-only'},indent=2));return 0
    home=data_home();home.mkdir(parents=True,exist_ok=True)
    db=sqlite3.connect(home/'watch.sqlite');initdb(db)
    try:
        if a.action=='scan':
            # rotate generic themes to avoid permanent single category or rate-limit exhaustion
            day=dt.date.today().toordinal()
            queries=[clean_terms(q) for q in a.query] if a.query else [SEEDS[(day+i)%len(SEEDS)] for i in range(2)]
            stats=scan(db,queries,max(1,min(20,a.budget)))
        else: stats={'status':'offline_report'}
        data={'schema':'arsenalmind.capability-watch.v1','generated':dt.datetime.now(dt.timezone.utc).isoformat(),'scan':stats,'candidates':report(db,' '.join(a.query),max(1,min(100,a.limit)))}
        content=json.dumps(data,ensure_ascii=False,indent=2)
        out=Path(a.output).expanduser() if a.output else home/'latest.json'
        out.parent.mkdir(parents=True,exist_ok=True);out.write_text(content,encoding='utf-8')
        print(json.dumps({'status':stats['status'],'candidate_count':len(data['candidates']),'output':str(out),'scan':stats},ensure_ascii=False))
        return 0 if stats['status']!='partial' else 3
    finally:db.close()
if __name__=='__main__':raise SystemExit(main())