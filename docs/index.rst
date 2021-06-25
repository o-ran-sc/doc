.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC D Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New featuresin D release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP D Release Feature Scope:

New xApps:
1) Bouncer xApp (HCL, C++): RIC performance measurement xApp - in conjunction with the appropriate E2 Sim, can test E2 control loop latency (INSERT-CONTROL) as well as the scalability of the RIC with regard to the number of E2 Nodes supported.
2) LP (Load Prediction, ChinaMobile, python): Initial version of a cell load predictor.
3) HW-P (Hello World - Python, Samsung): A python based demo xApp that demonstrates how an xApp can use the RIC platform features in python.
4) HW-G (Hello World - go, Samsung): A go-based demo xApp that demonstrates how an xApp can use the RIC platform features in go.

Improved xApps:
1) AD (Anomaly Detection, HCL, python): A ML-based real-time anomaly detection using KPI data populated in inFlux DB.
2) KPIMON (Samsung, go): Improved version implements E2 SM KPM 2.0.3 version and stored collected data in time series DB (inFlux)
3) QP (QuE Predictor, HCL, python): A ML-based predictor of UE's throughput if it was handed over to a neighboring cell. The D release version finally uses a ML-trained prediction model and includes the functionality previously provided as a separate QP-driver xApp.
4) TS (Traffic Steering, UTFPR, C++): Extended version of the TS xApp that now receives anomaly detection messages, requests QoE prediction, and issue control operation to request a UE handover. 

Together, AD, QP, and TS xApps and Viavi E2 Tester, implement a use case where anomaly detection is combined with QoE prediction and traffic steering action to move the affected UEs to a different cell. 


Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT D Release Feature Scope:

1) Some of the features are demoed here: 2021-06-08 Dawn
2) REST interface for xApps towards E2 subscription manager. No need to encode E2AP subscription messages in the xApps anymore. The Xapp framework for Go already supports/uses this.
3) Support for A1-EI (Enhancement information) to xApps
4) A lot of extra load/scalability testing (using a new bouncer xApp) and functionality testing (E2, ...) was done under RIC-150 using a "bouncer xApp".
5) Wider scope of the xapp framework for python (RIC-778, RIC-773).
6) We added InfluxDB as optional platform service time series database (RIC-734)
7) Support for O2 as per WG6 use case "Deploy xAPP in Near-RT RIC" in O-RAN Orchestration Use Cases v2.0. This also includes a change in how xApps register as part of their startup.
8) libe2ap (asn1c-based) can be re-used by components to encode/decode E2AP ASN.1 PDUs (Protocol Data Unit)
9) E2 statistics are now visible as VES metrics events
10) RMR raises alarms using the RIC alarm system in temporary overload situations
11) The Near-RT RIC can be deployed on Kubernetes 1.18 and helm 3. For the first time, this and all robot framework based "end-to-end" tests have also been verified in the O-RAN SC lab.
12) The Near-RT RIC project now achieved the CII (Core Infrastructure Initiative) badge "passing": (link).


Non-Real-time RIC (A1 Interface) (NONRTRIC)
-------------------------------------------

NONRTRIC D Release Functions:

1) Integrated A1 Adapter from ONAP (controller – mediation)
2) Integrated A1 Policy Management Service from ONAP (controller – A1 policies)
3) OSC A1 Enrichment Information Coordinator (controller – A1 EI Job management)
4) OSC Non-RT-RIC Control Panel (GUI – for A1-P & A1-EI Job management)
5) OSC A1 Simulator (a stateful test stub to simulate near-RT-RIC end of A1 interface – A1-P & A1-EI)
6) OSC (initial) APP catalog (for registering/querying APPs)
7) Initial K8S Helm Chart LCM Manager - for APP µServices etc. (ONAP & OSC) (new)
8) Initial Service Exposure Function (new)

In D Release: (NONRTRIC Release D Wiki) (NONRTRIC Release D Documentation)
1) Improved A1-PMS NBI (REST & DMaaP) (Rest style alignment)
2) Runtime configuration API (REST) for A1 Policy Management Service (e.g. add/remove adapters, near-rt-rics, security certs, etc)
3) Deployment – Continued improvements for Docker & Kubernetes
4) Extended/Easier deployment options with OSC IT/DEP project (SMO/NONRTRIC deployment)
5) Improving CI/CD to support include A1 Policy controller dependencies from ONAP
6) Multi-version support ( O-RAN A1-AP v1.1, v2.0, v2.1,v3.0 & OSC pre-spec A1)
7) Improved status monitoring/notification of A1-EI Jobs
8) Further improvement in security cert management (All interfaces can now be secured using TLS)
9) Re-architect & improve usability of Non-RT-RIC Control Panel (GUI)
10) Extend NONRTRIC Control Panel to edit/create A1 Enrichment Types/Jobs
11) Extend NONRTRIC Control Panel to configure A1 Policy Management Service
12) Configurable Service Exposure function – Extends/Replaces static exposure gateway in OSC Cherry
13) K8S Helm Chart LCM function for App µServices
14) Update NONRTRIC demo/test environment (one-click tests/use-cases, docker & single/multi-node K8s env)
15) OSC e2e integration use case – O-RU-FH-HelloWorld recovery
16) App to instigate O-RU-FH connection recovery after failure – via O-DU
17) Multiple implementation options – standalone µService and/or deployable ONAP-PF policy script
18) CII badging – Already achieved Bronze/Passing Grade


OAM (O1 Interface)
------------------

OAM D Release Feature Scope:

1) Update to OpenDaylight Silicon
2) Support of Callhome via TLS
3) CallHome to VES:pnfRegistration 
4) o-ran-fm.yang/alarm-notif to VES:fault


O-RAN Central Unit (OCU)
------------------------

O-RAN Central Unit (OCU) D release Feature Scope:
1) Radisys Commercial CU being used as a test fixture for E2E testing


O-DU High
---------

O-DU High D Release Feature Scope:

1. Achieve UL and DL data flow using FDD mode on 20 MHz Bandwidth, Numerology = 0

2.Support for static TDD mode with pattern “DDDDDDDSUU” on 100 MHz Bandwidth, Numerology = 1

    Evolve scheduler to support UL and DL scheduling of signaling and data messages on single spectrum in TDD mode
    Expand scheduler to support Frame structure according to numerology = 1
    Updates to cell broadcast for TDD and numerology = 1

3.Development activity for Closed Loop Automation use-case

    Support for cell stop and restart within O-DU High layers
    Support for cell stop and restart towards O-DU Low
    F1AP Enhancements towards O-CU indicating cell stop and restart

4.Integration

    Integration with O-DU Low in Radio mode
    Integration with CU

5.End to end testing support (O-RU<->O-DU-LOW<->O-DU-HIGH<->RSYS CU<->Viavi 5G Core )

6.O1 enhancements - by HCL

    Re-structure O1 module to run as a thread in ODU-High
    CM Support - IP and Port configuration for DU, CU stub and RIC stub via Netconf interface
    Support for Closed Loop Automation use-case


O-DU Low
--------

O-DU Low D Release Feature Scope:

Continue O-DU low and O-DU high pairwise test.
FAPI P7 massage integration -> Ongoing
Continue O-DU Low and O-RU emulator test.
Further CU plane testing -> Ongoing
Continue E2E test with UE simulator.
Support the UE attachment test
Development activity for Closed Loop Automation use-case
Support and test for cell stop and restart within O-DU High layers


Simulators (SIM)
----------------

SIM D Release Feature Scope:

1) Enable "Closed Loop Use Case" demonstration by providing O1 interface Simulators for:
      O-DU (containing o-du-hello-world YANG model)
      O-RU (containing O-RAN-RU-FH November 2020 train YANG models)
2) O1 Simulator improvements:
      "Blank" simulator, which allows dynamically loading any YANG models of interest, for simulating a NETCONF/YANG interface 



Infrastructure (INF)
--------------------

INF D Release Feature Scope:  

    Enabe the 2 AIO severs with additional worker nodes deployment scenario
    Major components upgrade
    Implement the O2 interface as the MVP (will defer to next release)


Integration and Test (INT)
--------------------------

Automated CLM and SonarQube Scanning CI Jobs
Improve CI for OSC projects
Validate and and Test platform and use cases


Service Management and Orchestration  (SMO)
-------------------------------------------

SMO D Release Feature Scope: 

1) Support for O1 interface
      Implementation of NETCONF client in SMO
      Reference implementation of a NETCONF server that O-RAN Network Functions, e.g. Near-RT RIC, CU, DU and RU can use. The code can be found at https://github.com/CESNET/netopeer2
      A minimal set of YANG models that demonstrate the capability of the O1 interface while satisfying the closed-loop automation use-case.
2) Support for O1/VES interface
      Demonstrate the capability to receive VES events, collect them in a dB, and display them in a dashboard.



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
