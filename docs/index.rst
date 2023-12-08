.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC I Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New featuresin I release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP I Release Feature Scope:

1) New HW-Rust xApp to support RUST framework.
2) New ad-cell xApp to detect cell level anomaly.
3) New ccc xApp to support E2SM CCC.


Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT I Release Feature Scope:
Contributions related to E2 interfaces
1) RIC-993 (CG): Near-RT RIC conflict management
2) RIC-933 (CG) : Adding support for DU in E2T/E2M/RNIB
3) RIC-967 (CG) xApp-facing interface for subscription delete required (added on 2023-08-23)
4) RIC-994 (S): Support for E2APv3.0
5) RIC-995 (S): Support for RIC Query
6) RIC-996 (S) Support for Subscription modifications (dhiraj interested as reviewer)
7) RIC-387 = ~RIC-383 (S): Support for E2 reset from RIC to RAN (completes also RIC-383) (prio1) (Dhiraj interested as reviewer, but we had earlier discussion on this) -
8) RIC-997 (N): Handling of RIC Error indication _during_ E2 setup
9) RIC-963 (GS) modify src code to be more lenient in ordering of IEs in ASN.1

Other contributions
1) RIC-998 (S): K8S operators for deploying/undeploying xApps
2) RIC-999=~RIC-972 (S): A1 alignment with A1AP (still under investigation. Minimum is using correct URL)
3) RIC-954 (S): DMS Rest API support for deleting/undeploy xApps (DMS REST is 2nd ifc addressing same space as dmscli)
4) Already in H: RIC-985 (UTFPR) IPv6 support for RMR 
5) task: RIC-987 (UTFPR) interface binding in RMR
6) RIC-705 (H) update xappframework for c++ to change in xApp registration
7) RIC-1000 (R): Support for only-IPv6 in RIC-internal interfaces
8) RIC-1004 (AG): Xapp Rust Framework enhancement after initial basic Xapp Framework Support
9) RIC-1027 (S) K8S operators for deploying/undeploying Near-RT RIC
10) RIC-950 implement test cases for xapp-frame-cpp
11) RIC-853 Implement subscription delete in Bouncer and E2Sim

Support for Integration project's pairwise-testing goals
1) ODU-high with near-RT RIC: moving from RIC stub to E2 messages with actual RIC
2) RIC xApp and near-RT RIC: using KPIMon/bouncer xApp or maybe CCC xApp. Maybe xApps can also be used to demonstrate conflict detection
3) non-RT RIC and near-RT RIC: providing standalone A1 mediator for CI testing of non-RT RIC.



Non-Real-time RIC  (NONRTRIC)
-----------------------------

NONRTRIC I Release Functions:

The Non-RealTime RIC (RAN Intelligent Controller) is an Orchestration and Automation function described by the O-RAN Alliance for non-real-time intelligent management of RAN (Radio Access Network) functions. The primary goal of the Non-RealTime RIC is to support non-real-time radio resource management, higher layer procedure optimization, policy optimization in RAN, and providing guidance, parameters, policies and AI/ML models to support the operation of near-RealTime RIC functions in the RAN to achieve higher-level non-real-time objectives. NONRTRIC functions include service and policy management, RAN analytics and model-training for the near-RealTime RICs. The Non-RealTime RIC project provides concepts, specifications, architecture and reference implementations as defined and described by the O-RAN Alliance architecture.



OAM (O1 Interface)
------------------

OAM I Release Feature Scope:

1) support of O-RAN WG10 VES message bodies
2) support of O-RAN WG4 optional VES bodies
3) update of OAM-Controller to ODL version Argon-SR1
4) support of other O-rAN-SC projects (e.g. SMO, Non-RT-Ric, O-DU, INT) based on RSAC and other input.
5) intergration of wireshark for api analysis
6) integration of jenkins for test-automation



O-DU High
---------

O-DU High I Release Feature Scope:

1) Alignment to latest ORAN WG8 AAD specification O-RAN.WG8.AAD.0-R003-v09.00
2) Alignment to E2 interface specifications O-RAN.WG3.E2AP-R003-v03.00
3) Multi UE (max=2) scheduling per TTI in scheduler
4) Integration of ODU-High with intel L1
5) XML based input configuration



O-DU Low
------------

O-DU Low I Release Feature Scope:

H release includes a patch to our previous F & G Releases with a fix for a PRACH detection bug found by LNT.



Infrastructure (INF)
--------------------

INF I Release Feature Scope:  

1) Support integration between INF as O-Cloud with other o-ran-sc components.
2) Support deploy ETSI-DMS (tacker) on INF O-Cloud.
3) Extend multi arch support: add support for ARM64 on Debian based OS.
4) Aligned INF O2 implementation to the O-RAN Spec 4.0



Service Management and Orchestration  (SMO)
-------------------------------------------

SMO I Release Feature Scope: 


The container images for SMO can be found on the Nexus server, where applicable.
The container images for OpenStack Tacker can be found in OpenStack Kolla repository.
The OpenStack Tacker container can be started with the steps in the following documentation.
The installation instructions for SMO can be found in the documentation page



AI/ML Framework
---------------

AI/ML Framework I Feature Scope:

1) Model management services aligning with O-RAN alliance WG2.
2) Dynamic selection of multiple data sources for training.
3) Automatically recover AIMLFW after VM restart without need for reinstall. 




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
