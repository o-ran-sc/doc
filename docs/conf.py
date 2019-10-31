from docs_conf.conf import *

branch = 'latest'

linkcheck_ignore = [
      'http://localhost',
]

intersphinx_mapping = {}
intersphinx_mapping['doc'] = ('https://o-ran-sc-doc.readthedocs.io/projects/o-ran-sc-doc/en/%s' % branch, None)
intersphinx_mapping['portal-ric-dashboard'] = ('https://o-ran-sc-doc.readthedocs.io/projects/o-ran-sc-portal-ric-dashboard/en/%s' % branch, None)
