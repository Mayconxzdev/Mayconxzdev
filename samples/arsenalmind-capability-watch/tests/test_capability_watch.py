import importlib.util, json, sqlite3, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('watch',ROOT/'scripts'/'capability_watch.py')
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)

class CapabilityWatchTests(unittest.TestCase):
 def test_repo_import(self):
  items=w.github_items({'items':[{'full_name':'foo/bar','html_url':'https://github.com/foo/bar','description':'MCP skills','stargazers_count':4,'fork':False,'archived':False}, {'full_name':'bad/fork','fork':True}]})
  self.assertEqual(len(items),1)
  self.assertEqual(items[0]['stars'],4)
 def test_hn_import(self):
  self.assertEqual(len(w.hn_items({'hits':[{'objectID':'123','title':'Promising tool','url':'https://example.org/foo'}]})),1)
 def test_secret_rejection(self):
  for s in ('token=1234','sk-abc','foo@example.org','api_key=secret',''):
   with self.subTest(s=s):
    with self.assertRaises(ValueError): w.clean_terms(s)
 def test_temporal_growth_not_invented(self):
  with tempfile.TemporaryDirectory() as d:
   db=sqlite3.connect(Path(d)/'watch.sqlite');w.initdb(db)
   record={'id':'gh:a/b','title':'a/b','url':'https://github.com/a/b','description':'tech','source':'github-search','stars':20}
   w.record(db,[record],'2026-10-27T00:00:00+00:00')
   self.assertIsNone(w.report(db)[0]['observed_star_gain_per_day'])
   record['stars']=30;w.record(db,[record],'2026-10-28T00:00:00+00:00')
   self.assertEqual(w.report(db)[0]['observed_star_gain_per_day'],10.0)
   self.assertEqual(w.report(db)[0]['installation'],'NOT_INSTALLED')
   db.close()
 def test_never_install_and_path_restriction(self):
  script=(ROOT/'scripts'/'capability_watch.py').read_text()
  self.assertNotIn('subprocess.run(',script)
  with self.assertRaises(ValueError): w.fetch('http://localhost/shell')
 def test_evidence_metadata_only(self):
  with tempfile.TemporaryDirectory() as d:
   db=sqlite3.connect(Path(d)/'watch.sqlite');w.initdb(db)
   w.record(db,[{'id':'hn:7','title':'Tool','url':'https://example.com/a','source':'hacker-news','description':'cool','stars':None}],'2026-10-29T00:00:00+00:00')
   r=w.report(db)[0]
   self.assertEqual(r['verification'],'UNVERIFIED');self.assertEqual(r['security'],'NOT_SCANNED')
   db.close()
if __name__=='__main__':unittest.main()