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
| 2019-11-31         | Amber              | CMCC               | Amber Release      |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| 2020-06-21         | Bronze             | CMCC               | Bronze Release     |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| 2020-12-21         | Cherry             | CMCC               | Cherry Release     |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| 2021-07-15         | D	          | CMCC               | D Release          |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| 2021-12-15         | E 	          | CMCC               | E Release          |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+


Release Summary
---------------

RAN Intelligent Controller Applications (RICAPP) features 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. * :doc:`Alarm Go Library Release-notes <ric-plt-alarm-go:release-notes>`

.. The AC xAPP, which supports full closed loop control as well as report mode operation for admission control of SgNB Addition requests, reporting of metrics over VES, and configuration of single instance policies via the A1-Interface.

.. * :doc:`Admission Control xAPP Release-notes <ric-app-admin:release-notes>`

GS-lite, which is an open-source, real-time, low-latency, high-throughput stream processing engine.
It is a fork of cask/tigon (https://github.com/cdapio/tigon) maintained to serve the needs of RIC applications (currently MC xApp).

* :doc:`GS-lite Stream Processing Engine Release-notes <com-gs-lite:release-notes>`


The HelloWorld(HW) xAPP repository contains open-source code for a prototype xAPP for near real-time RAN Intelligent Controller. 

* :doc:`HelloWorld xAPP Release-notes <ric-app-hw:release-notes>`


The KPI Mon xAPP, which supports full closed loop control for CuCpResourceStatusReport from multiple gNBs and stores the metrics in Redis DB.

* :doc:`KPI monitoring Release-notes <ric-app-kpimon:release-notes>`


QoE Predictor (QP) is an Xapp in the Traffic Steering O-RAN use case.

* :doc:`QoE Predictor xApp Release-notes <ric-app-qp:release-notes>`


The Acumos xAPP adapter, which contains the code needed to use an existing Acumos microservice as an O-RAN xAPP, by providing “glue” that listens and speaks RMR protocol and translates these into calls to the Acumos microservice, which is co-deployed in the same pod as the adapter.

* :doc:`RIC APP ML Release-notes <ric-app-ml:release-notes>`


The MC xAPP, which supports calculation of a number of metrics and KPIs based on X2 messages received from UEEC.

* :doc:`RIC Measurement Campaign (MC) xApp Release-notes <ric-app-mc:release-notes>`


Anomaly Detection (AD) is an xApp in the Traffic Steering O-RAN use case.

* :doc:`Anomaly Detection xApp Release-notes <ric-app-ad:release-notes>`


This repository contains open-source code for a prototype HW-go xAPP for near real-time RAN Intelligent Controller which makes use of go Xapp Framework. 

* :doc:`HW-go xAPP Release-notes <ric-app-hw-go:release-notes>`



Near Realtime RAN Intelligent Controller (RIC) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The RAN Intelligent Controller (RIC) Platform’s A1 Mediator component listens for policy type and policy instance requests sent via HTTP (the “northbound” interface), and publishes those requests to running xApps via RMR messages (the “southbound” interface).

* :doc:`A1 Release-notes <ric-plt-a1:release-notes>`


Asn1-documents, which contains a description of the E2 used in the near-RT RIC implementation under O-RAN-SC.

* :doc:`ASN.1 Documents Release-notes <ric-plt-asn1-documents:release-notes>`


DBAAS, which is the needed elements to deploy database as a service (Dbaas) to kubernetes. Dbaas service is realized with a single container running Redis database. The database is configured to be non-persistent and non-redundant.

* :doc:`DBAAS Release-notes <ric-plt-dbaas:release-notes>`

.. * :doc:`E2 Release-notes <ric-plt-e2:release-notes>`
.. * :doc:`E2MGR Release-notes <ric-plt-e2mgr:release-notes>`

Golang, which is an implementation of a structured logging library with Mapped Diagnostics Context (MDC) support.

* :doc:`GOLOG Release-notes <com-golog:release-notes>`


Jaegeradapter, which contains jaeger configuration files. This first version only supports configuration for a jaeger-all-in-one deployment.

* :doc:`Jaegeradapter Release-notes <ric-plt-jaegeradapter:release-notes>`


LOG, which is a thread-safe logging C API library with Mapped Diagnostics Context (MDC) support.

* :doc:`LOG Release-notes <com-log:release-notes>`

.. * :doc:`nodeb-rnib Release-notes <ric-plt-nodeb-rnib:release-notes>`

PYLOG, which implements a structured logging library with Mapped Diagnostic Context (MDC).

* :doc:`PYLOG Release-notes <com-pylog:release-notes>`

.. * :doc:`Resource Status Manager Release-notes <ric-plt-resouce-status-manager:release-notes>`
.. * :doc:`RIC Message Router Release-notes <ric-plt-lib-rmr:release-notes>`
.. * :doc:`Routing Manager Release-notes <ric-plt-rtmgr:release-notes>`

Shared Data Layer, which provides a lightweight, high-speed interface for accessing shared data storage. The purpose is to enable utilizing clients to become stateless, conforming with, e.g., the requirements of the fifth generation mobile networks.

* :doc:`Shared Data Layer (SDL) in C++ Release-notes <ric-plt-sdl:release-notes>`


Shared Data Layer, which provides a lightweight, high-speed interface for accessing shared data storage. The purpose is to enable utilizing clients to become stateless, conforming with, e.g., the requirements of the fifth generation mobile networks.

* :doc:`Shared Data Layer (SDL) in Go Release-notes <ric-plt-sdlgo:release-notes>`


Streaming Protobufs, which provides a Protobuf schema for selected set of X2 Application Protocol messages.

* :doc:`Streaming Protobufs Release-notes <ric-plt-streaming-protobufs:release-notes>`

.. * :doc:`Subscription Manager Release-notes <ric-plt-submgr:release-notes>`

Tracelibcpp library, which implements a function for creating a configured tracer instance. It hides the underlaying tracer implementation from the application. The library currently supports only Jaeger (https://www.jaegertracing.io/) C++ client (https://github.com/jaegertracing/jaeger-client-cpp) tracer implementation.

* :doc:`Tracelibcpp Release-notes <ric-plt-tracelibcpp:release-notes>`


Tracelibgo library, which implements a function for creating a configured tracer instance. It hides the underlaying tracer implementation from the application. The trace library currently supports only Jaeger (https://www.jaegertracing.io/) golang client (https://github.com/jaegertracing/jaeger-client-go) tracer implementation.

* :doc:`Tracelibgo Release-notes <ric-plt-tracelibgo:release-notes>`


The VESPA manager ,which uses the VES Agent (https://github.com/nokia/ONAP-VESPA) to adapt near-RT RIC internal statistics’ collection using Prometheus (xApps and platform containers) to ONAP’s VES (VNF event streaming).

* :doc:`Vespamgr Release-notes <ric-plt-vespamgr:release-notes>`


xapp-frame is a simple framework for rapid development of RIC xapps, and supports various services essential for RIC xapps such as RESTful APIs, RMR (RIC Message Routing), database backend services and watching and populating config-map changes in K8S environment

* :doc:`xapp-frame Release-notes <ric-plt-xapp-frame:release-notes>`

.. * :doc:`xAPP C++ Release-notes <ric-plt-xapp-frame-cpp:release-notes>`
.. * :doc:`xApp Python Release-notes<ric-plt-xapp-frame-py:release-notes>`



Non-RealTime RAN Intelligent Controller (NONRTRIC) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Bronze release, Non-RT RIC containes Policy Agent, Control Panel and A1 Simulator. 

* :doc:`Non-RT RIC Release-notes <nonrtric:release-notes>`



Operations and Maintenance (OAM) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OAM which provides reference implementation according to the O-RAN OAM (WG1) documents.

* :doc:`OAM Operation and Maintenance Release-notes <oam:release-notes>`
* :doc:`TR069 Adapter Release-notes <oam-tr069-adapter:release-notes>`
* :doc:`NF OAM Adopter Release-notes <oam-nf-oam-adopter:release-notes>`


The O-RAN SC RIC Dashboard provides administrative and operator functions for a radio access network (RAN) controller. The web app is built as a single-page app using an Angular (version 8) front end and a Java (version 11) Spring-Boot (version 2.1) back end.

* :doc:`RIC Dashboard Release-notes <portal-ric-dashboard:release-notes>`



O-RAN Central Unit (OCU) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5G NR which is a RAN Software Reference Design for a 5G protocol stack

.. * :doc:`Open LTE Release-notes <scp-ocu-openlte:release-notes>`


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

RTP O2 repository implements a reference O2 IMS and DMS service to expose O2 interface to SMO.

* :doc:`RTP O2 Release-notes <pti-o2:release-notes>`


Realtime Platform, which implements a real time platform to deploy the O-CU and O-DU components.

* :doc:`Realtime Platform Release-notes <pti-rtp:release-notes>`



Integration and Testing (INT) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IT-DEP hosts deployment and integration artifacts such as scripts, Helm charts, and other files used for deploying O-RAN SC software.

* :doc:`IT-DEP Release-notes <it-dep:release-notes>`


IT-DEV which integrates artifacts for developing Near Realtime RAN Intelligent Controller applications (xApps).

* :doc:`IT-DEV Release-notes <it-dev:release-notes>`


IT-TEST, which  contains:
Test automation scripts written using the robot frameworkDeployment scripts for a dev-test 1-node Kubernetes cluster.
A functional simulator for the E2 protocol that acts as gNB used to test the RIC.
A workload generator that is used to benchmark the RIC

* :doc:`IT-TEST Release-notes <it-test:release-notes>`


IT-DEV includes the initial commit of the OTF platform code. Applications include otf-frontend, otf-service-api, otf-camunda, and several virtual test head microservices (ping, ssh, robot, ric). In addition setup documentation and installation guides are included to build docker containers and helm charts for deployment.

* :doc:`IT-Otf Release-notes <it-otf:release-notes>`

Service Management and Orchestration (SMO) features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SMO O1 repository is for the implementation, installation, and use of the O1 interface of SMO. It uses the Software Defined Netowrk (SDN) Controller for Radio (SDNR) to implement the O1 interface. The software comes in the form of Docker containers that are setup using docker-compose.

* :doc:`SMO O1 Release-notes <smo-o1:release-notes>`

The O1/VES interface supports the monitoring side of SMO. The diagram below shows how the Network Elements interact with the O1/VES interface in the SMO.

* :doc:`SMO-VES Release-notes <smo-ves:release-notes>`
