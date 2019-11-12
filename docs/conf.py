from docs_conf.conf import *

branch = 'latest'

linkcheck_ignore = [
      'http://localhost',
]

intersphinx_mapping = {}
intersphinx_mapping['portal-ric-dashboard'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-portal-ric-dashboard/en/%s' % branch, None)
intersphinx_mapping['it-dev'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-dev/en/%s' % branch, None)
