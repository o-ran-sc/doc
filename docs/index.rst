.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC J Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New featuresin J release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP J Release Feature Scope:

Expand the community on open source xApps for O-RAN SC. 
        Update and maintain the existing xApps to latest releases (currently J Release).
        Enhance the set of open source xApps in support of the RSAC use cases (traffic steering, network slicing) and add new xApps.
        New RUST framework based xApp hw-rust will be added in J release. 
        New xApp to support E2SM CCC will be added in this release  


Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT J Release Feature Scope:
Make the platform more robust in handling E2AP, conflicts and A1

Original primary goals based on contributions from Nokia, Samsung, Capgemini, HCL Alexandre Huff (UTFPR), GS Lab and Abhijit G:
        Additional messages: modify src code to be more lenient in ordering of IEs in ASN.1 (RIC-1030, GS)
        tests with mock replies for subscriptions, registrations and alarms in xapp framework for Rust (RIC-1028, AG)
        Handling of E2 Error Indication from E2 node at E2M and Sub manager (RIC-1024, N)
        Graceful Handling of Unsupported E2AP Procedure at E2T (RIC-1023, N)
        Handling of SCTP Abort message from E2 Node (RIC-1022, N)  
        remove leading zeros in gnb, cu, du ID , MCC and MNC (RIC-1021, N)
        Abnormal signaling process cause E2Term crash (Bug RIC-1002, N)
        Handling of RIC Error indication _during_ E2 setup (RIC-997, N)
        E2 Conflict management between xApps (RIC-993, CG)
        implement test cases for xapp-frame-cpp (RIC-950, H)
        Support Startup/Health script demonstrating release capabilities (RIC-926, H)
        A1 mediator testing in nanobot (RIC-926, H)
        xapp testing nanobot enhancements: wider coverage of functionality, e.g., Subscription deletion (RIC-860, H)
        scale-in and scale out using K8S operators (details still open) (RIC-1048, S)


Non-Real-time RIC  (NONRTRIC)
-----------------------------

NONRTRIC J Release Highlights:

Major improvements in new rApp Manager
        Includes several sample/starter rApps
Major improvements in new Service Manager
        Fully functional rApp repository & life-cycle manager
Improvements in Function Test environments
        Supports latest releases, and expand set of use cases tested
Continued improvements for A1-Policy functions (ONAP CCSDK)
        Added new O-RAN R1-compliant A1-Policy-Management northbound API (A1-PMS-v3)
        Added tracing support for all northbound (R1) and southbound (A1) interfaces.
Maintained and support existing NONRTRIC functions and service best effort.
Updates to OSC Integrated SMO deployment scripts & charts.
Improvements in stability, 3PP vulnerability, test coverage and quality.
Continued engagement with O-RAN Alliance working groups for standardization alignment.


Operation and Maintenance(OAM)
------------------------------

O-DU High J Release Feature Scope:

update of O-RAN WG10 VES message bodies
update of O-RAN WG4 optional VES bodies
update of OAM-Controller to OpenDaylight version Potassium-SR1
support of other O-RAN-SC projects (e.g. SMO, Non-RT-Ric, O-DU, INT) based on RSAC and other input.
support of OAI and nephio integration with O-RAN-SC related to OAM


O-DU High
---------

O-DU High J Release Feature Scope:

1. Multi UE (max=2) scheduling per TTI in scheduler UL part
2. End-to-end integration 
3. OSC-OAI Collaboration
4. XML based input configuration enhancement



O-DU Low
--------

O-DU Low J Release Feature Scope:

Review code release strategy with XFAPI
New code base moving to next release


Infrastructure (INF)
--------------------

INF J Release Feature Scope:  

Update INF Platform to aligned with StarlingX 9.0
Update O2 implementation to aligned with new Spec Ver 5.0
Develop OKD as alternative O-Cloud platform


Service Management and Orchestration  (SMO)
-------------------------------------------

SMO J Release Feature Scope: 

Improve O2 DMS ETSi profile.
        Fault management
Develop O2 interfaces and integrate with OSC INF:
        FOCOM interfaces to create cluster.
        NFO K8s profile to Deploy a CNF on top of the cluster created through OSC-INF
Develop a Topology & Inventory (TEIV) registry & exposure capability



AI/ML Framework
---------------

AI/ML Framework J Feature Scope:

Platform upgraded to latest supported dependencies of kubernetes and kubeflow.
Platform dependency from docker is removed (it directly depends on containerd).
Study has been initiated to study generic pipeline and model retraining.
Remove influx info from Training Job Creation.



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
