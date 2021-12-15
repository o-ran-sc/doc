.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC E Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New featuresin E release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP E Release Feature Scope:

1) New xApps: RC (RAN Control) by Mavenir - implements subset of E2 SM RC
2) Improved xApps:
    a) LP (Load Prediction) by ChinaMobile: Include trained ML model, will populate predictions in inFlux DB
    b) AD (Anomaly Detection) by HCL: Will identify a new anomaly type (area anomaly), use geo-location as a feature.
    c) QP (QoE Predictor) by HCL: Include prediction for current serving cell, incorporate predicted load as a feature, provide sequence of predictions.
    d) TS (Traffic Steering) by UTFPR (University, Parana, Brazil): Call RC xApp to trigger UE handover, improvements in traffic steering logic.
    e) Bouncer by HCL: Increase performance and functional testing capabilities; continue identifying RIC platform bottlenecks.
    f) HW (HelloWorld) demo xApps in C++, go and python by AT&T and Samsung: Add usage of more platform features, update usage of platform features that are evolving.
3) Integration of AD, QP, TS, LP, RC, and KPIMON with Viavi simulator.
4) Extensive performance benchmarking of the RIC platform using Bouncer and E2 Simulator (HCL)
5) Design for xApps to support network slicing use case.



Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT E Release Feature Scope:

1) We updated from E2APv1.0 to E2APv1.1. The platform now stores OIDs (introduced in E2APv1.1) for the E2SM of E2 function definitions in RNIB. Since E2APv1.1 is backwards compatible with 1.0, you can still connect E2 nodes that support E2APv1.0. Note that for the next release we plan to switch to E2APv2.0 only.
2) The E2 subscription manager now automatically deletes its stored subscriptions if it gets notified (by the E2 manager) of E2 nodes having disconnected. xApps are expected to do the same and need to re-issue their subscriptions once the E2 node is reconnected. This behavior is different to earlier behavior where the subscription manager kept the subscriptions in such situations. Note that the standard requires the E2 node to delete its subscriptions if there's the E2 interface is disconnected.
3) The E2 subscription manager now handles various error scenarios that previously were not handled.
4) We will continue the re-implementation of the A1 mediator in golang in release F. The first parts are already implemented, but in the E release we stay with the "old" python-implementation of the A1 mediator.
5) On SDL side we now have a SDL CLI that can be used in testing (instead of direct usage of the Redis CLI). The SDL API for findkeys/getkeys now supports glob-style patterns.
6) The golang SDL API/library now handles namespaces as part of its function signatures instead of this being a global parameter. This eases usage of multiple namespaces from the same application.



Non-Real-time RIC (A1 Interface) (NONRTRIC)
-------------------------------------------

NONRTRIC E Release Functions:

1) Integrated A1 Adapter from ONAP (A1 Policy (A1-P) controller – mediation)
2) Integrated A1 Policy Management Service from ONAP (A1 Policy (A1-P) controller)
3) rApp/Control Loop Manager (ONAP & OSC)
4) OSC Information Coordinator (controller – Data Management & Exposure & A1 Enrichment Information (A1-EI) Job management)
5) OSC Non-RT-RIC Control Panel (GUI – for A1-P & A1-EI Job management)
6) OSC A1 Simulator (a stateful test stub to simulate near-RT-RIC end of A1 interface – A1-P & A1-EI)
7) Initial OSC APP catalog (for registering/querying APPs)
8) K8S Helm Chart LCM Manager - for APP µServices etc. (ONAP & OSC)
9) Exposure Gateway Functions
10) Coordinated service exposure for R1 interface
11) DMaaP → Information Producer Mediator/Adapter (multiple)



OAM (O1 Interface)
------------------

OAM E Release Feature Scope:

1) Switch to Opendaylight version Silicon-SR2
2) Standard-defined VES for
     NotifyNewAlarm
     NotifyAlarmCleared
     NotifyHeartbeat
     NotifyMoiChanges
    


O-RAN Central Unit (OCU)
------------------------

OCU E Release Feature Scope:

not applicable


O-DU High
---------

O-DU High E Release Feature Scope:

1) Support for Multi UE (Connected = 16, Active =4, Per Slot = 1)
2) Only slot based round robin scheduling support for multi UE scheduling
3) Support for Multi Bearer
4) Basic RAN slicing support
5) Support for HARQ
6) End to End Integration Support (TDD and FDD stack validation)
7) Closed Loop Automation Feature Verification



O-DU Low
--------

O-DU Low E Release Feature Scope:

not applicable



Simulators (SIM)
----------------

SIM E Release Feature Scope:

1) Support of O-RAN-SC E-Release Network Slicing use case by Radisys - support of O-DU projects for end-to-end closed loop use cases for RAN network slicing (implement any message flows in the O-DU Simulator, if needed)
2) Align O1 Simulator with the latest specifications released by O-RAN Alliance.
3) Support of NETCONF CallHome via TLS, for the O1 simulator
4) VES stdnDefined implementation



Infrastructure (INF)
--------------------

INF E Release Feature Scope:  

1) Enable the 2 AIO severs with additional worker nodes deployment scenario
2) Major components upgrade
3) Implement the O2 interface as the MVP



Integration and Test (INT)
--------------------------

INT E Release Feature Scope: 

1) Automated CLM and SonarQube Scanning CI Jobs
2) Improve CI for OSC projects
3) Validate and and Test platform and use case


Service Management and Orchestration  (SMO)
-------------------------------------------

SMO E Release Feature Scope: 

1) SMO was extended to support network slicing. In particular, RSAC has come up with closed loop automation use case for network slicing which involves the SMO collecting PM counters related to network slicing, and based on them breaching some thresholds will cause a change in the configuration of the network slice. That means the SMO had to have support for PM counters related to network slicing, and an ability to reconfigure the O-DU for the network slice.
2) Separately, SMO now implements a disaggregated VES solution that separates the collection of VES events from how it is presented to any application that wants to view them. In particular, all events now get posted on the Kafka bus, and different "connectors" are provided to make the data available in different formats. For example, the "DMaaP Connector" provides an ability for a application to read the message in DMaaP format. Alternatively, if the data needs to be synced to a dB, the "InfluxdB Connector" sinks the data to an InfluxdB.



Please find some guidance here on the content of O-RAN SC documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   architecture/architecture.rst
   license.rst
   release-notes.rst
   projects.rst
   api-docs.rst


Indices
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
