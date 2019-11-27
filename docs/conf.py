from docs_conf.conf import *

branch = 'latest'

linkcheck_ignore = [
      'http://localhost',
]

intersphinx_mapping = {}

#(near realtime)RIC app
intersphinx_mapping['ric-app-mc'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-mc/en/%s' % branch, None)
intersphinx_mapping['ric-app-ml'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-ml/en/%s' % branch, None)
intersphinx_mapping['com-gs-lite'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-com-gs-lite/en/%s' % branch, None)
intersphinx_mapping['ric-app-admin'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-admin/en/%s' % branch, None)
intersphinx_mapping['ric-app-kpimon'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-kpimon/en/%s' % branch, None)


#(near realtime)RIC platform
intersphinx_mapping['com-log'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-com-log/en/%s' % branch, None)
intersphinx_mapping['com-golog'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-com-golog/en/%s' % branch, None)
intersphinx_mapping['com-pylog'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-com-pylog/en/%s' % branch, None)
intersphinx_mapping['ric-plt-a1'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-a1/en/%s' % branch, None)
intersphinx_mapping['ric-plt-dbaas'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-dbaas/en/%s' % branch, None)
intersphinx_mapping['ric-plt-lib-rmr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-lib-rmr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-rtmgr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-rtmgr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-sdl'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-sdl/en/%s' % branch, None)
intersphinx_mapping['ric-plt-sdlgo'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-sdlgo/en/%s' % branch, None)
intersphinx_mapping['ric-plt-jaegeradapter'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-jaegeradapter/en/%s' % branch, None)
intersphinx_mapping['ric-plt-tracelibcpp'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-tracelibcpp/en/%s' % branch, None)
intersphinx_mapping['ric-plt-tracelibgo'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-tracelibgo/en/%s' % branch, None)
intersphinx_mapping['ric-plt-vespamgr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-vespamgr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-asn1-documents'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-asn1-documents/en/%s' % branch, None)
intersphinx_mapping['ric-plt-streaming-protobufs'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-streaming-protobufs/en/%s' % branch, None)

#nonrt ric
intersphinx_mapping['nonrtric'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-nonrtric/en/%s' % branch, None)

#OAM
intersphinx_mapping['portal-ric-dashboard'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-portal-ric-dashboard/en/%s' % branch, None)

#OCU
intersphinx_mapping['scp-ocu-openlte'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-scp-ocu-openlte/en/%s' % branch, None)

#ODUHIGH
intersphinx_mapping['o-du-l2'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/%s' % branch, None)

#ODULOW
intersphinx_mapping['o-du-phy'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-phy/en/%s' % branch, None)


#INF
intersphinx_mapping['pti-rtp'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-pti-rtp/en/%s' % branch, None)

#SIM
intersphinx_mapping['sim-o1-interface'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-sim-o1-interface/en/%s' % branch, None)

#INT
intersphinx_mapping['it-dep'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-dep/en/%s' % branch, None)
intersphinx_mapping['it-dev'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-dev/en/%s' % branch, None)
intersphinx_mapping['it-test'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-test/en/%s' % branch, None)
intersphinx_mapping['it-otf'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-it-otf/en/%s' % branch, None)
