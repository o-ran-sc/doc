.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC F Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New featuresin H release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP H Release Feature Scope:

1) New HW-Rust xApp to support RUST framework.
2) New ad-cell xApp to detect cell level anomaly.
3) RC xApp - GRPC interface support on RC xApp
4) Bouncer xApp - RIC Benchmarking new features addition.
5) KPIMON-GO xApp – New Version


Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT H Release Feature Scope:

1) E2 reset (from E2 node to RIC), E2 subscription delete required, A1 policy status notifications
2) Preparation of feature for I release, e.g., include xApps in subscription delete required decision

For the H release of the near-RT RIC we do only limited integration testing: only the use cases: deploy RIC, deploy xApp, make E2 connection, get list of A1 policies has been tested.



Non-Real-time RIC (A1 Interface) (NONRTRIC)
-------------------------------------------

NONRTRIC H Release Functions:

1) Consolidated & Improved RAN PM data exposure in new repo for RAN PM functions
        Adds 4 new services for RAN PM processing
        Lots of work on deployment scripts/charts, testing, CI, and documentation
2) (R1) Service Exposure & Management (SME)
        CAPIF Aligned Service Registry & Discovery
        Continued work of Service execution platform extensions (K8s, Istio, Keycloak, OPA, Gateway) to enable and enforce service isolation & exposure
        Controlled access & exposure of service to/from rApps
3) (R1) Data Management & Exposure (DME)
        Small updates to Information Coordination Service – studying alignment with R1 proposals
        File-based PM data → Kafka/InfluxDB/Minio
        Including parsing, filtering & delivery
        ref. PM Data exposure above
4) rApp Management
        Started work on a new rApp Manager functions – more in next release
        LCM for rApps: Building on ONAP "Automation Composition" model & platform to implement rApp use cases
                Added a 'KServe Participant'
                        Inference Services in rApps
                        Now supports KServe-based AI/ML rApps
                Added an 'A1 Policy Participant'
        Overlap with Service Exposure work to examine role of an rApp Manager to support controlled access to and exposure of Services
        Overlap with Data Exposure work to examine role of an rApp Manager to support controlled access to and exposure of Data types
5) Continued A1-Policy & A1-Enrichment-Information evolution (& R1-A1)
        A1-Policy work in ONAP (continues in ONAP London) - candidate for R1-A1(P)
                Numerous updates to improve security
                Improved support fine-grained policy-based access control
                Removed DMaaP NBI
        A1-EI management as part of DME - candidate for how to include A1-EI in R1-DME
        ref. DME work above
6) Demonstrated ASD-based CNF LCM
        ONAP SO CNFM in standalone mode
7) Sample use cases (rApps)
        Requirements Drivers for rApp/R1 development
8) Testing, Maintenance & Housekeeping
        3PP update – esp. Springboot 3 & JDK 17
        Function Test & Integration Test environment,
                Lots of new test cases, and new ONAP L & OSC H test profiles
        Continue integration, deployment & configuration of SMO/Non-RT-RIC related functions & usecases in OSC Integration environment.
        Project coordination, Documentation, Delivery, Reporting, Cross-project alignment, Community demos, O-RAN Standardization support, etc.


OAM (O1 Interface)
------------------

OAM H Release Feature Scope:

1) Updates according to O-RAN Operations and Maintenance Interface Specification 8.0 (O-RAN.WG10.O1-Interface.0-v08.00)    October 2022
        Please see H-Release for further details
2) Hardening the solution by introducing a "SMO-gateway".
3) Add a FlowManagement Component.



O-RAN Central Unit (OCU)
------------------------

OCU H Release Feature Scope:

1) Radisys Commercial CU is being used as a test fixture for E2E testing
2) This is containerized CU image with following
	Release version 2.5.3
	NG interface with SOCKET mode and veth type
	F1 interface with SOCKET mode and veth type
	E2 interface support
	Software Crypto


O-DU High
---------

O-DU High H Release Feature Scope:

1) Odu High interfaces alignment to the latest specification & New design with multi-scheduler algorithm support
        Status: Completed
        Epic: https://jira.o-ran-sc.org/browse/ODUHIGH-488
2) Integration of ODU-High with intel L1
        Status: Spread over multiple releases, to be continued in the next release
        Epic: https://jira.o-ran-sc.org/browse/ODUHIGH-475
3) Inter CU Handover
        Status: Completed
        Epic: https://jira.o-ran-sc.org/browse/ODUHIGH-463
4) E2 interface enhancement
        Status: Completed
        Epic: https://jira.o-ran-sc.org/browse/ODUHIGH-510



O-DU Low
--------

O-DU Low H Release Feature Scope:

The O-DU Low H release is the same as the F Release and G Release that added support for Massive MIMO, URLLC and it is based on the commercial FlexRan 21.11 release.  

The O-DU Low H, G and F Release code is an Intel contribution in collaboration with Tieto Poland for the source code releases in the O-RAN gerrit and for the binary blobs contributed via GitHub.

For the documentation preparation of the H, F and G release Intel worked with collaboration from Fransiscus Bimo and Professor Ray-Guang Cheng from National Taiwan University of Science and Technology (NTUST).  

The H, G and F release are being used for end to end testing and it is based on the E maintenance release that was used for the 2021 November US O-RAN Plugfest and tested in conjuction with 2 stack partners and 2 different Test equipment vendors. The Front Haul Interface was also tested for compliance using Keysight's Front Haul Test equipment.

Container images and deployment instructions are to be provided later



Simulators (SIM)
----------------

SIM H Release Feature Scope:

1) Updated simulated O-RU YANG models according to latest release (March 2023) OpenFronthaul Management Plane specification
2) Implement the Monitoring NETCONF connectivity feature for the O-RUs, according to chapter 6.7 (Monitoring NETCONF connectivity) in O-RAN.WG4.MP.0-R003-v11.00
3) Created a mechanism to locally build simulated O-DU with 3GPP YANG models
4) No new contributions for the E2 Simulator



Infrastructure (INF)
--------------------

INF H Release Feature Scope:  

1) Enable the 2 AIO severs with additional worker nodes deployment scenario
2) Major components upgrade
3) Implement the O2 interface as the MVP



Integration and Test (INT)
--------------------------

INT H Release Feature Scope: 

1) Convert existing RICPLT/RICAPP Robot test cases in it/test repo to be executed with XTesting, which should automate the deployment of RIC platform, onboarding an xApp, and execute test cases all together.
2) Wind River may contribute XTesting test cases on the o2 repo
3) Specific to the Asia Pacific Open Lab:
        Completing E2 setup procedure between OSC Near-RT RIC and OAI gNb.
        Incorporate E2AP v2 in OAI CU for connection between OAI CU and OSC Near-RT RIC.
        Verify data exchange between netconf and ves between OAI CU and OSC SMO.
        Testing C-plane in F1 interface connection between OAI CU and OSC DU.



Service Management and Orchestration  (SMO)
-------------------------------------------

SMO H Release Feature Scope: 

1) Automated API Conformance testing
2) Alignment with O-RAN O2 DMS ETSI NFV Profile.
3) Refresh SDNR image to the latest on SMO O1 project.



AI/ML Framework
---------------

AI/ML Framework H Feature Scope:

1) Diversify training data source for Training host
        Obtaining training data from DME in Non-RT RIC 
        Creating Feature groups with data source and feature information

2) Kserve adapter
        Deploy and manage AI models in Near-RT RIC/Non-RT RIC
        Integrate Inference host with O-Cloud( RICDMS ) and Management Functions of RIC. 

3) Training pipeline Enhancement
        Provide sample pipelines by default

4) AIMLFW feature enhancements
        Options for edit, retrain and delete training jobs 




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
