.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC F Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New featuresin F release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP F Release Feature Scope:

1) New xApps
	KPIMON-GO by HCL
2) Improved xApps:
	RC (RAN Control) by Mavenir - implements subset of E2 SM RC Ver2.0
	AD (Anomaly Detection) by HCL: Will identify a new anomaly type (area anomaly), use geo-location as a feature. Dependency on Data Stream from KPIMON to influxDB. (Currently AD is working on Static data).
        QP (QoE Predictor) by HCL: Include prediction for current serving cell, incorporate predicted load as a feature, provide sequence of predictions.
        TS (Traffic Steering) by UTFPR (University, Parana, Brazil): Call RC xApp to trigger UE handover, improvements in traffic steering logic.
        Bouncer by HCL: Increase performance and functional testing capabilities; continue identifying RIC platform bottlenecks.
        HW (HelloWorld) demo xApps in C++, go and python by AT&T and Samsung: Add usage of more platform features, update usage of platform features that are evolving.
3) VIAVI RIC test tool is used to test Traffic Steering use case.



Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT F Release Feature Scope:
1) Updated from E2APv1.1 to E2APv2.0 for the existing supported E2 procedures.

2) Additionally E2 configuration transfer procedures (in E2 setup and via explicit E2 Node Configuration Update) are now supported.
3) Enhancements in the handling of E2 disconnect+connect cycles and in SCTP stream handling
4) xApps can now query the list of RAN functions by E2SM OID (and nodeb ID)
5) The reimplementation of the A1 mediator in golang has proceeded, but is not yet ready and not yet replacing the existing python implementation
6) Switch from Redis 5 to Redis 6 - primarily due to Redis 5 EOL
7) The ric deployment is now possible without the it/dep repo
8) More information in the debug interface of the subscription manager (which had some small adaptations for E2APv2.0, but these changes are not visible to xApps using the E2 subscription manager REST interface)
9) A new influxdb wrapper as component stslgo (shared time-series layer "golang")
10) Bug fixes as per link. Bugs relevant to production (i.e., not test) code: RIC-903 DefaultUser setup fails when authentication is enabled for InfluxDB; RIC-895 missing static route entries for service update messages (from E2T to E2M and back); RIC-889 Subscription Manager Swagger YAML file is wrong; RIC-872 RMR routing statistic data printout crash; RIC-885 sdlgo multi-namespace SDL event namespace filter issue; RIC-880 Wrong date in sdl (C++) rpm spec file; RIC-873 SDLCLI get - writes wrongly results to stderr in success case; RIC-862 xapp-frame-py caching of error code data not happening (was: Python RMR Memory Leak); RIC-869 SDLCLI healthcheck - Redis sentinel status is wrong



Non-Real-time RIC (A1 Interface) (NONRTRIC)
-------------------------------------------

NONRTRIC F Release Functions:

1) Study & prototype Coordinated Service Exposure (SE)
        Continue SE contribution building on the manual approaches already studied/completed.
        Create/apply K8S configurations to isolate platform services and rApp microservices, then configure controlled secure access between service
        Prototype CAPIF compliant API for Service/rApp registration/discovery, and service provider/consumer registration/configuration
2) Data Management & Exposure (DME):
        Pre-spec O1 PM via pre-spec R1 DME demo
        Configure & connect to PM data - collected by SMO (ONAP)
        Collect, Filter & Coordinate Delivery of PM data from DMaaP/Kafka to rApps over R1 (ICS)
3) General activities
        Continue to provide spec-compliant implementation of A1-Policy & A1-EI functions
        NONRTRIC repo re-org
        Continue to integrate and deploy SMO/NONRTRIC platform/rApps in OSC integration env.
        Continue to expand NONRTRIC test platform & testsets
        Show various versions rApps implemented/deployed as holistic “Automation Compositions” (ref ONAP ACM)
        Continue to provide & integrate strawman rApps to comply with OSC RSAC integration usecases.





OAM (O1 Interface)
------------------

OAM F Release Feature Scope:

1) Providing an abstract topology for rApp and CNF deployment
	Topology links are related to the following Interfaces: A1, E1, E2, F1, N1, N2, N3, O1, O2, OFH-CUSM
        Topology Node are related to the following components:
		1. SMO: Non-RT-RIC, O1-Controller, VES-Collector, File-Client, O2-Controller
		2. 5G Core: UPF, AMF
		3. RAN: Near-RT-RIC, O-CU-UP, O-CU-CP, O-DU, O-RU
		4. Transport: Fronthaul Gateway
		5. User Equipment
2) Topology Generator, Topology Reader
3) Enhancing automated test cases validating the end-to-end message flows related to OAM interfaces (O1, OpenFronthaul M-Plane)
        Adding Wireshark for traffic flow analysis
    


O-RAN Central Unit (OCU)
------------------------

OCU F Release Feature Scope:

1) Radisys Commercial CU is being used as a test fixture for E2E testing
2) This is containerized CU image with following
        Release version 2.5.3
        NG interface with SOCKET mode and veth type
        F1 interface with SOCKET mode and veth type
        E2 interface support
        Software Crypto


O-DU High
---------

O-DU High F Release Feature Scope:

1) HARQ framework support
2) Scheduler enhancement
3) Mobility (Inter-DU handover) support
4) Idle mode paging support
5) E2AP upgrade to v2.0
6) End to end integration support



O-DU Low
--------

O-DU Low F Release Feature Scope:

The O-DU Low F release adds support for Massive MIMO, URLLC and it is based on the commercial FlexRan 21.11 release. This release is an incremental improvement over the E-maintenance release code released on March of this year and that still needs to be integrated with the RSYS O-DU High code.

The F release can be used for end to end testing and it is based on the E maintenance release that was used for the 2021 November US O-RAN Plugfest and tested in conjuction with 2 stack partners and 2 different Test equipment vendors. The Front Haul Interface was also tested for compliance using Keysight's Front Haul Test equipment.

Container images and deployment instructions TBD



Simulators (SIM)
----------------

SIM F Release Feature Scope:

1) Provide topology-service image that exposes a topology
2) Provide a tool that generates a docker-compose file to start a simulated topology based on a topology file provided by the OAM project
3) Keep alignment with latest O-RAN specifications for O1 and E2
4) Preparations for code-coverage for the C/C++ code, will spill to G release because important code modifications are needed for Sonar integration



Infrastructure (INF)
--------------------

INF F Release Feature Scope:  

1) Enable the 2 AIO severs with additional worker nodes deployment scenario
2) Major components upgrade
3) Implement the O2 interface as the MVP



Integration and Test (INT)
--------------------------

INT F Release Feature Scope: 

1) To set up test automation that can run at release time to verify features and integration (initial efforts to make use of the Open Test Framework were incomplete due to resource issue)
2) To add CI/CD Jenkins job against the it/dep repository to start regular validation of OSC components installation/deployment and corresponding health check, which also lay the foundation for future test cases implementation (across OSC components, end-to-end use cases, etc.)
3) Work with OSC open labs (US east coast, US west coast, Asia Pacific) to facilitate community testing.
4) Explore the POWDER testbed for OSC integration test needs.


Service Management and Orchestration  (SMO)
-------------------------------------------

SMO F Release Feature Scope: 

1) O1/VES interface
        Add support for StdDefined messages.
        Expand on the list of PM counters supported
2) O2 interface
        Tacker project will commit VNF support



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
