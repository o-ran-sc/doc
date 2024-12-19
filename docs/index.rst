.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC K Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New featuresin K release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP K Release Feature Scope:

The architecture of an xApp consists of the code implementing the xApp's logic and the RIC libraries that allow the xApp to

Send and receive messages.
Read from, write to, and get notifications from the SDL layer.
Write log messages.
Additional libraries will be available in future versions including libraries for setting and resetting alarms and sending statistics.

Furthermore, xApps can use access libraries to access specific name-spaces in the SDL layer. For example, the R-NIB that provides information about which E2 nodes (e.g., CU/DU) the RIC is connected to and which SMs are supported by each E2 node, can be read by using the R-NIB access library.

The O-RAN standard interfaces (O1, A1, and E2) are exposed to the xApps as follows:

xApp will receive its configuration via K8s ConfigMap - the configuration can be updated while the xApp is running and the xApp can be notified of this modification by using inotify().
xApp can send statistics (PM) either by (a)  sending it directly to VES collector in VES format, (b ) by exposing statistics via a REST interface for Prometheus to collect
xApp will receive A1 policy guidance via an RMR message of a specific kind (policy instance creation and deletion operations)
xApp can subscribe to E2 events by constructing the E2 subscription ASN.1 payload and sending it as a message (RMR), xApp will receive E2 messages (e.g., E2 INDICATION) as RMR messages with the ASN.1 payload. Similarly xApp can issue E2 control messages.
In addition to A1 and E2 related messages, xApps can send messages that are processes by other xApps and can receive messages produced by other xApps. Communication inside the RIC is policy driven, that is, an xApp cannot specify the target of a message. It simply sends a message of a specific type and the routing policies specified for the RIC instance will determine to which destinations this message will be delivered (logical pub/sub).


Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT K Release Feature Scope:

No new features implemented or bugs addressed.
Conflict manager testing and demo.


Non-Real-time RIC  (NONRTRIC)
-----------------------------

NONRTRIC K Release Highlights:

The Non-RealTime RIC (RAN Intelligent Controller) is an Orchestration and Automation function described by the O-RAN Alliance for non-real-time intelligent management of RAN (Radio Access Network) functions. The primary goal of the Non-RealTime RIC is to support non-real-time radio resource management, higher layer procedure optimization, policy optimization in RAN, and providing guidance, parameters, policies and AI/ML models to support the operation of near-RealTime RIC functions in the RAN to achieve higher-level non-real-time objectives. NONRTRIC functions include service and policy management, RAN analytics and model-training for the near-RealTime RICs. The Non-RealTime RIC project provides concepts, specifications, architecture and reference implementations as defined and described by the O-RAN Alliance architecture.

The OSC NONRTRIC implementation will communicate with near-RealTime RIC elements in the RAN via the A1 interface. Using the A1 interface the OSC NONRTRIC will facilitate the provision of A1 Policies; monitor and provide basic feedback on policy state from near-RealTime RICs; provide A1 Enrichment Information as required by near-RealTime RICs; act as a hosting platform for rApps (Non-RealTime RIC applications); host the R1 interface between rApps and the underlying SMO and Non-RT-RIC platforms; and manage the exposure towards rApps of SMO platform functions, Non-RT-RIC platform functions, and the capabilities of other rApps.

The NONRTRIC functions partly leverage and extend some existing infrastructure from ONAP to support non-realtime control of the RAN (Radio Access Network).

All implementations will be demonstrated in open community labs to prove functionalities and to give feedback to the O-RAN working groups.


Operation and Maintenance(OAM)
------------------------------

O-DU High K Release Feature Scope:

Update on the topology generator of O-RAN components
        using the topology to generate day0 data for the deployments
        generating a topology data model which is inline with discussions at O-RAN WG10 TE&IV

Support of hybrid and hierarchical OAM architecture

OAM specific K8S helm  


O-DU High
---------

O-DU High K Release Feature Scope:

1. End-to-end integration 

2. OSC-OAI Collaboration

3. nFapi interface development

4. Containerization of ODU, CU stub & RIC stub


O-DU Low
--------

O-DU Low K Release Feature Scope:

1. End-to-end integration 

2. OSC-OAI Collaboration

3. nFapi interface development

4. Containerization of ODU, CU stub & RIC stub


Simulators (SIM)
----------------

O-DU Low K Release Feature Scope:

Implemented a new Python version for the simulated O-RU and simulated O-DU

Aligned YANG models for O1 and OpenFronthaul M-Plane with June 2024 train

Implemented hybrid and hierarchical O-RU simulators. Simulated O-DUs can accept connections from O-RUs.



Infrastructure (INF)
--------------------

INF K Release Feature Scope:  

Update INF StarlingX O-Cloud for ARM64 to aligned with StarlingX 9.0

Update O2 implementation to aligned with new Spec

Add Bare metal support for OKD O-Cloud

Add O2 operator integration for OKD O-Cloud.


Service Management and Orchestration  (SMO)
-------------------------------------------

SMO K Release Feature Scope: 

Improve O2 DMS ETSi profile.

improve the NFO K8s profile integration with OSC-INF.




AI/ML Framework
---------------

AI/ML Framework K Release Feature Scope:

aiml-fw/awmf/tm:  Training Manager : Training job and model management

aiml-fw/athp/tps/kubeflow-adapter: Adapter for Kubeflow

aiml-fw/athp/sdk/model-storage: Sdk for accessing Model storage

aiml-fw/athp/sdk/feature-store: Sdk for accessing Feature store

aiml-fw/athp/data-extraction: Retrieving features for training from Data lake

aiml-fw/aimlfw-dep: Deployment scripts aiml workflow 

portal/aiml-dashboard: GUI for AIML Workflow

ric-app/qp-aimlfw: Sample ML Assist xApp for QoE prediction

aiml-fw/aihp/ips/kserve-adapter: kserve adapter for near-RT RIC

aiml-fw/awmf/modelmgmtservice: Model Management services



Please find some guidance here on the content of O-RAN SC documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   architecture/architecture.rst
   license.rst
   release-notes.rst
   projects.rst
   api-docs.rst


User experience
===============
Here are some O-RAN SC user experience  

.. toctree::
   :maxdepth: 1

   user-experience/index.rst



Indices
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
