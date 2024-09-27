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

.. * :doc:`Alarm Go Library <ric-plt-alarm-go:index>`
.. * :doc:`Admission Control xAPP <ric-app-admin:index>`

* :doc:`Anomaly Detection xAPP <ric-app-ad:index>`
* :doc:`GS-lite Stream Processing Engine <com-gs-lite:index>`
* :doc:`HelloWorld xAPP  <ric-app-hw:index>`
* :doc:`HW-go xAPP <ric-app-hw-go:index>`
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
The O-RAN Non-RT RIC provides functionality for the A1-interface, R1-interface, and closed-loop use cases. The O-RAN SC NONRTRIC project works together with the OAM project, SMO project, AI/ML FW project and SIM project to align activities for O1 & O2 interfaces, and to provide consolidated SMO functionality. The Non-RT RIC project also provides capabilities to support rApps (Non-RT RIC Apps) and the R1 Interface. 

More detailed function documentation can be found as follow:

* :doc:`Non-RT RIC Components <nonrtric:index>`
* :doc:`A1 Interface Simulator <sim-a1-interface:index>`
* :doc:`Non-RT RIC Control Panel <nonrtric-controlpanel:index>`



Operations and Maintenance (OAM)
--------------------------------
The O-RAN-SC-OAM project provides reference implementation according to the O-RAN OAM (WG1) documents. In addition we provide a common MnS-Consumer for development and module test purposes. The assumption is that the projects for the ManagedElements can concentrate on the more important user-plane.

More detailed function documentation can be found as follow:

* :doc:`NF OAM Adopter <oam-nf-oam-adopter:index>`
* :doc:`Non-RT RIC Control Panel <nonrtric-controlpanel:index>`
* :doc:`OAM Operation and Maintenance <oam:index>`
* :doc:`RIC Dashboard <portal-ric-dashboard:index>`
* :doc:`TR069 Adapter <oam-tr069-adapter:index>`


O-RAN Central Unit (OCU)
------------------------
The OCU is target an initial software deliverable with limited functionality. Focus on a basic E2 interface to enable initial integration testing between RIC and OCU.

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
* :doc:`RTP O2 <pti-o2:index>`


Simulations(SIM)
----------------
Initial simulators used for testing O-RAN NF interfaces.

More detailed function documentation can be found as follow:

* :doc:`SIM/A1-Interface <sim-a1-interface:index>`
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


Service Managerment and Orgestration(SMO)
-----------------------------------------
The SMO project implements the O1 and the O1/VES interface. The former is used for configuration and management of RAN Network Functions (NF) while the latter collects all the events that are reported by different RAN NFs.

More detailed function documentation can be found as follow:

* :doc:`SMO-TEIV <smo-teiv:index>`
* :doc:`SMO-VES <smo-ves:index>`
* :doc:`SMO O1 <smo-o1:index>`
* :doc:`SMO O2 <smo-o2:index>`


AI/ML Framework
---------------
the  AI/ML Framework is stand alone installation (separated from existing platform deployment) and initial AIML workflow modules.

More detailed function documentation can be found as follow:

* :doc:`AIMLFW Training Manager <aiml-fw-awmf-tm:index>`
* :doc:`AIMLFW Dashboard <portal-aiml-dashboard:index>`
* :doc:`AIMLFW Data Extraction <aiml-fw-athp-data-extraction:index>`
* :doc:`AIMLFW Feature Store SDK <aiml-fw-athp-sdk-feature-store:index>`
* :doc:`AIMLFW Model Storage SDK <aiml-fw-athp-sdk-model-storage:index>`
* :doc:`AIMLFW Kubeflow adapter <aiml-fw-athp-tps-kubeflow-adapter:index>`
* :doc:`AIMLFW dep <aiml-fw-aimlfw-dep:index>`
* :doc:`AIMLFW QoE Prediction assist xApp <ric-app-qp-aimlfw:index>`

