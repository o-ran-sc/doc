.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. index rst file


O-RAN SC Projects
=================

RAN Intelligent Controller Applications (RICAPP)
------------------------------------------------
RICAPP includes open source sample xAPPs and platform applications that can we used for integration, testing, and demonstrations.

More detailed function documentation can be found as follow:

* :doc:`Alarm Go Library <ric-plt-alarm-go:index>`
* :doc:`Admission Control xAPP <ric-app-admin:index>`
* :doc:`GS-lite Stream Processing Engine <com-gs-lite:index>`
* :doc:`HelloWorld xAPP  <ric-app-hw:index>`
* :doc:`KPI monitoring <ric-app-kpimon:index>`
* :doc:`QoE Predictor xApp <ric-app-qp:index>`
* :doc:`RIC APP ML <ric-app-ml:index>`
* :doc:`RIC Measurement Campaign (MC) xApp <ric-app-mc:index>`
* :doc:`Traffic Steering xAPP <ric-app-ts:index>`


Near Realtime RAN Intelligent Controller (RIC)
----------------------------------------------
This project a initial RIC Platform to support xAPPs with limited support for O1, A1, and E2 interfaces.

More detailed function documentation can be found as follow:

* :doc:`A1 <ric-plt-a1:index>`
* :doc:`ASN.1 Documents <ric-plt-asn1-documents:index>`
* :doc:`DBAAS <ric-plt-dbaas:index>`
* :doc:`E2 <ric-plt-e2:index>`
* :doc:`E2MGR <ric-plt-e2mgr:index>`
* :doc:`GOLOG <com-golog:index>`
* :doc:`Jaegeradapter <ric-plt-jaegeradapter:index>`
* :doc:`LOG <com-log:index>`
* :doc:`nodeb-rnib <ric-plt-nodeb-rnib:index>`
* :doc:`PYLOG <com-pylog:index>`
* :doc:`Reasouce Status Manager <ric-plt-resource-status-manager:index>`
* :doc:`RIC Message Router <ric-plt-lib-rmr:index>`
* :doc:`Routing Manager <ric-plt-rtmgr:index>`
* :doc:`Shared Data Layer (SDL) in C++ <ric-plt-sdl:index>`
* :doc:`Shared Data Layer (SDL) in Go <ric-plt-sdlgo:index>`
* :doc:`Streaming Protobufs <ric-plt-streaming-protobufs:index>`
* :doc:`Subscription Manager <ric-plt-submgr:index>`
* :doc:`Tracelibcpp <ric-plt-tracelibcpp:index>`
* :doc:`Tracelibgo <ric-plt-tracelibgo:index>`
* :doc:`Vespamgr <ric-plt-vespamgr:index>`
* :doc:`xapp-frame <ric-plt-xapp-frame:index>`
* :doc:`xAPP C++ <ric-plt-xapp-frame-cpp:index>`
* :doc:`xApp Python <ric-plt-xapp-frame-py:index>`


Non-RealTime RAN Intelligent Controller (NONRTRIC)
--------------------------------------------------
Non-RT RIC focus on feature functionality of A1-interface (consumer and provider), and closed-loop use cases. The Non-RT RIC project will also work together with the OAM project to align activities on a case-by-case base for O1 interfaces. Project should focus on use cases supported in ONAP. The work should be sponsored in O-RAN and initial code contributions in O-RAN SC. Interoperability with ONAP should be aligned between the standards and will follow initial contributions in this project.

More detailed function documentation can be found as follow:

* :doc:`A1 Interface Simulator <sim-a1-interface:index>`
* :doc:`Non-RT RIC Components <nonrtric:index>`

   + A1 Policy Management Service
   + A1 Controller
   + A1-Enrichment Information Coordinator
   + rApp catalogue

* :doc:`Non-RT RIC Control Panel <nonrtric-controlpanel:index>`


Operations and Maintenance (OAM)
--------------------------------
The O-RAN-SC-OAM project provides reference implementation according to the O-RAN OAM (WG1) documents. In addition we provide a common MnS-Consumer for development and module test purposes. The assumption is that the projects for the ManagedElements can concentrate on the more important user-plane.

More detailed function documentation can be found as follow:

* :doc:`OAM Operation and Maintenance <oam:index>`
* :doc:`RIC Dashboard <portal-ric-dashboard:index>`


O-RAN Central Unit (OCU)
------------------------
The OCU is target an initial software deliverable with limited functionality. Focus on aa basic E2 interface to enable initial integration testing between RIC and OCU.

More detailed function documentation can be found as follow:

.. * :doc:`Open LTE <scp-ocu-openlte:index>`

* :doc:`5G NR <scp-ocu-5gnr:index>`


O-RAN Distributed Unit High Layers (ODUHIGH)
--------------------------------------------
Focus on initial L2 functional blocks based on seed code contributions.

More detailed function documentation can be found as follow:

* :doc:`O-DU Layer 2 <o-du-l2:index>`


O-RAN Distributed Unit Low Layers (ODULOW)
------------------------------------------
Focus on initial L1 functional blocks based on seed code contributions.

More detailed function documentation can be found as follow:

* :doc:`O-DU Layer 1 <o-du-phy:index>`


Infrastructure (INF)
--------------------
Initial building blocks for infrastructure to run O-RAN NF components.

More detailed function documentation can be found as follow:

* :doc:`Realtime Platform <pti-rtp:index>`


Simulations(SIM)
----------------
Initial simulators used for testing O-RAN NF interfaces.

More detailed function documentation can be found as follow:

* :doc:`SIM/O1-Interface <sim-o1-interface:index>`


Integration and Testing (INT)
-----------------------------
The integration and test effort will focus on testing the requirements documented in each release. This will focus on end to end test and use case testing.

INF Testing shall primarily be done on the Akraino-REC (Radio Edge Cloud) blueprint. While Non-RT RIC and O1 interface testing will primarily use ONAP components.

More detailed function documentation can be found as follow:

* :doc:`IT-DEP <it-dep:index>`
* :doc:`IT-DEV <it-dev:index>`
* :doc:`IT-OTF <it-otf:index>`
* :doc:`IT-TEST <it-test:index>`




