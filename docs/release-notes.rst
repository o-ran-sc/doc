.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC 

Release-Notes
=============


This document provides the release notes for O-RAN SC.

.. contents::
   :depth: 3
   :local:


Version history
---------------

+--------------------+--------------------+--------------------+--------------------+
| **Date**           | **Ver.**           | **Author**         | **Comment**        |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| 2019-11-12         | 0.1.0              | Weichen Ni(CMCC)   | A Release draft    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
|                    |                    |                    |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
|                    | 1.0                |                    |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+


Amber Release Summary
---------------------

RAN Intelligent Controller Applications (RICAPP) features 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The MC xAPP, which supports calculation of a number of metrics and KPIs based on X2 messages received from UEEC.

* :doc:`RIC Measurement Campaign (MC) xApp Release-notes <ric-app-mc:release-notes>`


The Acumos xAPP adapter, which contains the code needed to use an existing Acumos microservice as an O-RAN xAPP, by providing “glue” that listens and speaks RMR protocol and translates these into calls to the Acumos microservice, which is co-deployed in the same pod as the adapter.

* :doc:`RIC APP ML Release-notes <ric-app-ml:release-notes>`


GS-lite, which is an open-source, real-time, low-latency, high-throughput stream processing engine.
It is a fork of cask/tigon (https://github.com/cdapio/tigon) maintained to serve the needs of RIC applications (currently MC xApp).

* :doc:`GS-lite Stream Processing Engine Release-notes <com-gs-lite:release-notes>`


The AC xAPP, which supports full closed loop control as well as report mode operation for admission control of SgNB Addition requests, reporting of metrics over VES, and configuration of single instance policies via the A1-Interface.

* :doc:`Admission Control xAPP Release-notes <ric-app-admin:release-notes>`


The KPI Mon xAPP, which supports full closed loop control for CuCpResourceStatusReport from multiple gNBs and stores the metrics in Redis DB.

* :doc:`KPI monitoring Release-notes <ric-app-kpimon:release-notes>`



Near Realtime RAN Intelligent Controller (RIC) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

LOG, which is a thread-safe logging C API library with Mapped Diagnostics Context (MDC) support.

* :doc:`LOG Release-notes <com-log:release-notes>`


Golang, which is an implementation of a structured logging library with Mapped Diagnostics Context (MDC) support.

* :doc:`GOLOG Release-notes <com-golog:release-notes>`


PYLOG, which implements a structured logging library with Mapped Diagnostic Context (MDC).

* :doc:`PYLOG Release-notes <com-pylog:release-notes>`

..
.. * :doc:`A1 Release-notes <ric-plt-a1:release-notes>`

DBAAS, which is the needed elements to deploy database as a service (Dbaas) to kubernetes. Dbaas service is realized with a single container running Redis database. The database is configured to be non-persistent and non-redundant.

* :doc:`DBAAS Release-notes <ric-plt-dbaas:release-notes>`

..
.. * :doc:`RIC Message Router Release-notes <ric-plt-lib-rmr:rel-notes>`
..
..
.. * :doc:`Routing Manager Release-notes <ric-plt-rtmgr:release-notes>`

Shared Data Layer, which provides a lightweight, high-speed interface for accessing shared data storage. The purpose is to enable utilizing clients to become stateless, conforming with, e.g., the requirements of the fifth generation mobile networks.

* :doc:`Shared Data Layer (SDL) in C++ Release-notes <ric-plt-sdl:release-notes>`


Shared Data Layer, which provides a lightweight, high-speed interface for accessing shared data storage. The purpose is to enable utilizing clients to become stateless, conforming with, e.g., the requirements of the fifth generation mobile networks.

* :doc:`Shared Data Layer (SDL) in Go Release-notes <ric-plt-sdlgo:release-notes>`

..
.. * :doc:`Subscription Manager Release-notes <ric-plt-submgr:release-notes>`

Jaegeradapter, which contains jaeger configuration files. This first version only supports configuration for a jaeger-all-in-one deployment.

* :doc:`Jaegeradapter Release-notes <ric-plt-jaegeradapter:release-notes>`


Tracelibcpp library, which implements a function for creating a configured tracer instance. It hides the underlaying tracer implementation from the application. The library currently supports only Jaeger (https://www.jaegertracing.io/) C++ client (https://github.com/jaegertracing/jaeger-client-cpp) tracer implementation.

* :doc:`Tracelibcpp Release-notes <ric-plt-tracelibcpp:release-notes>`


Tracelibgo library, which implements a function for creating a configured tracer instance. It hides the underlaying tracer implementation from the application. The trace library currently supports only Jaeger (https://www.jaegertracing.io/) golang client (https://github.com/jaegertracing/jaeger-client-go) tracer implementation.

* :doc:`Tracelibgo Release-notes <ric-plt-tracelibgo:release-notes>`


The VESPA manager ,which uses the VES Agent (https://github.com/nokia/ONAP-VESPA) to adapt near-RT RIC internal statistics’ collection using Prometheus (xApps and platform containers) to ONAP’s VES (VNF event streaming).

* :doc:`Vespamgr Release-notes <ric-plt-vespamgr:release-notes>`


Asn1-documents, which contains a description of the E2 used in the near-RT RIC implementation under O-RAN-SC.

* :doc:`ASN.1 Documents Release-notes <ric-plt-asn1-documents:release-notes>`


Streaming Protobufs, which provides a Protobuf schema for selected set of X2 Application Protocol messages.

* :doc:`Streaming Protobufs Release-notes <ric-plt-streaming-protobufs:release-notes>`



Non-RealTime RAN Intelligent Controller (NONRTRIC) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A dashboard is available. Non-RT RIC does not support R-apps yet. The Non-RT RIC is not yet fully compliant with the A1 specifications for this release. 

* :doc:`Non-RT RIC Release-notes <nonrtric:release-notes>`



Operations and Maintenance (OAM) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OAM which provides reference implementation according to the O-RAN OAM (WG1) documents.

* :doc:`OAM Operation and Maintenance Release-notes <oam:release-notes>`


The O-RAN SC RIC Dashboard provides administrative and operator functions for a radio access network (RAN) controller. The web app is built as a single-page app using an Angular (version 8) front end and a Java (version 11) Spring-Boot (version 2.1) back end.

* :doc:`RIC Dashboard Release-notes <portal-ric-dashboard:release-notes>`


O-RAN Central Unit (OCU) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenLTE, which is a RAN Software Reference Design for a 4G TDD

* :doc:`Open LTE Release-notes <scp-ocu-openlte:release-notes>`


O-RAN Distributed Unit High Layers (ODUHIGH) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O-DU Layer 2, which is O-DU layer intilaizations and exchange of F1 Setup Request, F1 Setup Response, GNB DU Config Update and GNB DU Config Update ACK between the ODU and CU STUB.

* :doc:`O-DU Layer 2 Release-notes <o-du-l2:release-notes>`


O-RAN Distributed Unit Low Layers (ODULOW) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O-DU Layer 1, which is the O-RAN FHI Lib built on top of DPDK to perform U-plane and C-plane functions according to the ORAN Fronthaul Interface specification between O-DU and O-RU. S-Plane support requires PTP for Linux version 2.0 or later The management plane is outside of the scope of this library implementation.

* :doc:`O-DU Layer 1 Release-notes <o-du-phy:release-notes>`


Infrastructure (INF) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Realtime Platform, which implements a real time platform to deploy the O-CU and O-DU components.

* :doc:`Realtime Platform Release-notes <pti-rtp:release-notes>`


.. Simulations(SIM) Amber release features contain:

.. * :doc:`SIM/O1-Interface Release-notes <sim-o1-interface:release-notes>`


Integration and Testing (INT) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IT-DEP hosts deployment and integration artifacts such as scripts, Helm charts, and other files used for deploying O-RAN SC software.

* :doc:`IT-DEP Release-notes <it-dep:release-notes>`



* :doc:`IT-TEST Release-notes <it-test:release-notes>`


IT-DEV which integrates artifacts for developing Near Realtime RAN Intelligent Controller applications (xApps).

* :doc:`IT-DEV Release-notes <it-dev:release-notes>`


IT-DEV includes the initial commit of the OTF platform code. Applications include otf-frontend, otf-service-api, otf-camunda, and several virtual test head microservices (ping, ssh, robot, ric). In addition setup documentation and installation guides are included to build docker containers and helm charts for deployment.

* :doc:`IT-Otf Release-notes <it-otf:release-notes>`





























