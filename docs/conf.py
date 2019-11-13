from docs_conf.conf import *

branch = 'latest'

linkcheck_ignore = [
      'http://localhost',
]

intersphinx_mapping = {}

intersphinx_mapping['ric-app-mc'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-mc/en/%s' % branch, None)

intersphinx_mapping['portal-ric-dashboard'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-portal-ric-dashboard/en/%s' % branch, None)

intersphinx_mapping['it-dep'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-dep/en/%s' % branch, None)
intersphinx_mapping['it-dev'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-dev/en/%s' % branch, None)
intersphinx_mapping['it-test'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-test/en/%s' % branch, None)
intersphinx_mapping['it-otf'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-otf/en/%s' % branch, None)