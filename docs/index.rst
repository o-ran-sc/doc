.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC G Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New featuresin G release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP G Release Feature Scope:

1) New HW-Rust xApp to support RUST framework
2) HW(python) - RIC Subscription using python xApp framework 
3) RC xApp - GRPC interface support on RC xApp
4) ouncer xApp - RIC Benchmarking new features addition
5) KPIMON-GO xApp – Version 2.0
6) AD & QP xApp – InfluxDB database integration to fetch data.



Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT G Release Feature Scope:

1) For the G release of the near-RT RIC we do only limited integration testing: only the use cases: deploy RIC, deploy xApp and make E2 connection are to be tested.
2) Filled in end-of-release checklist : Release criteria checklist - TODO


Non-Real-time RIC (A1 Interface) (NONRTRIC)
-------------------------------------------

NONRTRIC G Release Functions:

Count of Epics (20 issues), User Stories, Tasks, and Issues:  (455 issues)

1) R1 Service Exposure & Management
	Continue work of Service execution platform extensions (K8s, Istio, Keycloak, OPA, Gateway) to enable service isolation & exposure
	Extend Release F prototyping of 3GPP CAPIF-aligned Service Exposure Manager function (& API)

2) R1 Data Management & Exposure
	Align with emerging proposals for R1-DME where possible
	R1 DME Data Catalog support in NONRTRIC ICS 
	R1 Data delivery & filtering (kafka & REST)

3) rApp Manager

	Build on ONAP “Automation Composition” model & platform to implement rApp use cases
	Demonstrate controlled on-boarding & LCM rApps with & without µService
	Overlap with Service Exposure work to examine role of an rApp Manager to support controlled exposure & LCM of µService and non-µService parts of an rApp
	Investigate where parts of rApp executes in KNative environment (e.g. ML model part of an rApp)

4) Continue A1-Policy & A1-Enrichment-Information evolution (& R1-A1)
	A1 Spec evolution
	Southbound: A1 Interface
	Northbound: R1-A1(P) & R1-DME Interfaces


5) Sample use cases (rApps)
	Requirements Drivers for rApp/R1 development
	High degree of cross-project integration activity


6) Testing, Maintenance & Housekeeping
	Function Test & Integration Test environment,
	Support integration, deployment & configuration of SMO/Non-RT-RIC related functions & usecases in OSC Integration env.
	Project coordination, Documentation, Delivery, Reporting, Cross-project alignment, Community demos, O-RAN Standardization support, etc.



OAM (O1 Interface)
------------------

OAM G Release Feature Scope:

1) support of O-RAN WG10 VES message bodies
2) update of OAM-Controller to ODL version Sulfur
3) Note: team decided to go with Java11 - Java 17 would be possible but is pushed out to next release.
4) update to keycloak version 18
5) even more secure keycloak configuration
6) there is a request for a "bare-metal" deployment which is not in scope of O-RAN, but still useful - also for development and module test
7) support of AI/ML based on RSAC and other input.
8) support of Tacker team



O-RAN Central Unit (OCU)
------------------------

OCU G Release Feature Scope:

1) Radisys Commercial CU is being used as a test fixture for E2E testing
2) This is containerized CU image with following
	Release version 2.5.3
	NG interface with SOCKET mode and veth type
	F1 interface with SOCKET mode and veth type
	E2 interface support
	Software Crypto


O-DU High
---------

O-DU High G Release Feature Scope:

1) DRX support
2) Mobility (Inter-CU handover) support
3) code clean-up and coverage
4) latest specification support for all modules and interfaces (AAD WG8)
5) End to end integration support



Simulators (SIM)
----------------

SIM G Release Feature Scope:

1) keep alignment of the O1 Simulator with latest YANG models
2) E2 Simulator improvements (especially to the deployment/build procedures)
3) NS3-E2 Simulator integration in Gerrit



Infrastructure (INF)
--------------------

INF F Release Feature Scope:  

1) Enable the 2 AIO severs with additional worker nodes deployment scenario
2) Major components upgrade
3) Implement the O2 interface as the MVP



Integration and Test (INT)
--------------------------

INT G Release Feature Scope: 

1) Extend MultiOS support: add Debian as the base OS
2) Enable the multiple deployment scenarios for Debian based image:
	AIO-SX, AIO-DX, AIO-DX + workers,  standard, Distributed Cloud
3) Align INF O2 implementation to the latest O2 spec.


Service Management and Orchestration  (SMO)
-------------------------------------------

SMO G Release Feature Scope: 

1) The focus for the G release in SMO is interoperability. Every sub-project within SMO has at least one item that focuses on interoperating with one other entity outside of SMO. For example,
	On the O1 interface, the focus is on trying to bring-up O-DU using NETCONF and YANG models defined for O-DU.
	On the O1/VES interface, it is ability to generate network slicing PM events in the O-DU, and the ability to receive them in SMO dashboard, and store them in InfluxdB.
	On the O2 interface, it will be the ability to instantiate an instance of a Network Function (NF) like the O-DU in the O-Cloud.
2) Separate from this, each sub-project within SMO has other features/capabilities it will address as part of the G-release. For details please refer to the minutes of the SMO meeting here.


AI/ML Framework
---------------

AI/ML Framework G Feature Scope:

1) Stand alone installation with Kubeflow as a Training host backend and Kserve as a Inference host backend
2) Initial Training Job Management ( Data extraction / feature management)
3) Sample ML pipeline and ML xApp : QoE Prediction model using LSTM with data from ricapp/qp




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
