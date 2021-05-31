from docs_conf.conf import *

#branch configuration
branch = 'latest'

linkcheck_ignore = [
      'http://localhost',
]

#intershpinx mapping with other projects
intersphinx_mapping = {}

#(near realtime)RIC app
intersphinx_mapping['ric-app-mc'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-mc/en/%s' % branch, None)
intersphinx_mapping['ric-app-ml'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-ml/en/%s' % branch, None)
intersphinx_mapping['com-gs-lite'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-com-gs-lite/en/%s' % branch, None)
intersphinx_mapping['ric-app-admin'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-admin/en/%s' % branch, None)
intersphinx_mapping['ric-app-kpimon'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-kpimon/en/%s' % branch, None)
intersphinx_mapping['ric-plt-alarm-go'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-alarm-go/en/%s' % branch, None)
intersphinx_mapping['ric-app-hw'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-hw/en/%s' % branch, None)
intersphinx_mapping['ric-app-qp'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-qp/en/%s' % branch, None)
intersphinx_mapping['ric-app-ts'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-app-ts/en/%s' % branch, None)


#(near realtime)RIC platform
intersphinx_mapping['com-log'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-com-log/en/%s' % branch, None)
intersphinx_mapping['com-golog'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-com-golog/en/%s' % branch, None)
intersphinx_mapping['com-pylog'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-com-pylog/en/%s' % branch, None)
intersphinx_mapping['ric-plt-a1'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-a1/en/%s' % branch, None)
intersphinx_mapping['ric-plt-appmgr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-appmgr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-dbaas'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-dbaas/en/%s' % branch, None)
intersphinx_mapping['ric-plt-e2'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-e2/en/%s' % branch, None)
intersphinx_mapping['ric-plt-e2mgr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-e2mgr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-nodeb-rnib'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-nodeb-rnib/en/%s' % branch, None)
intersphinx_mapping['ric-plt-lib-rmr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-lib-rmr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-rtmgr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-rtmgr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-sdl'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-sdl/en/%s' % branch, None)
intersphinx_mapping['ric-plt-sdlgo'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-sdlgo/en/%s' % branch, None)
intersphinx_mapping['ric-plt-submgr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-submgr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-jaegeradapter'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-jaegeradapter/en/%s' % branch, None)
intersphinx_mapping['ric-plt-tracelibcpp'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-tracelibcpp/en/%s' % branch, None)
intersphinx_mapping['ric-plt-tracelibgo'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-tracelibgo/en/%s' % branch, None)
intersphinx_mapping['ric-plt-vespamgr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-vespamgr/en/%s' % branch, None)
intersphinx_mapping['ric-plt-xapp-frame'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-xapp-frame/en/%s' % branch, None)
intersphinx_mapping['ric-plt-asn1-documents'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-asn1-documents/en/%s' % branch, None)
intersphinx_mapping['ric-plt-streaming-protobufs'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-streaming-protobufs/en/%s' % branch, None)
intersphinx_mapping['ric-plt-resource-status-manager'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-resource-status-manager/en/%s' % branch, None)
intersphinx_mapping['ric-plt-xapp-frame'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-xapp-frame/en/%s' % branch, None)
intersphinx_mapping['ric-plt-xapp-frame-py'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-xapp-frame-py/en/%s' % branch, None)
intersphinx_mapping['ric-plt-xapp-frame-cpp'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-xapp-frame-cpp/en/%s' % branch, None)


#nonrt ric
intersphinx_mapping['nonrtric'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-nonrtric/en/%s' % branch, None)
intersphinx_mapping['nonrtric-controlpanel'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-portal-nonrtric-controlpanel/en/%s' % branch, None)
intersphinx_mapping['sim-a1-interface'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-sim-a1-interface/en/%s' % branch, None)


#OAM
intersphinx_mapping['oam'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-oam/en/%s' % branch, None)
intersphinx_mapping['portal-ric-dashboard'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-portal-ric-dashboard/en/%s' % branch, None)
intersphinx_mapping['oam-tr069-adapter'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-oam-tr069-adapter/en/%s' % branch, None)
intersphinx_mapping['oam-nf-oam-adopter'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-oam-nf-oam-adopter/en/%s' % branch, None)


#OCU
#intersphinx_mapping['scp-ocu-openlte'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-scp-ocu-openlte/en/%s' % branch, None)
intersphinx_mapping['scp-ocu-5gnr'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-scp-ocu-5gnr/en/%s' % branch, None)


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


