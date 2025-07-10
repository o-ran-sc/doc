.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC L Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New features in L release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP L Release Feature Scope:

Expand & maintain the community on open source xApps for O-RAN SC. 

Update and maintain the existing xApps to latest releases (currently L Release).

Enhance the set of open source xApps in support of the RSAC use cases and add new xApps. 



Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT L Release Feature Scope:

Couple of bugs needs to  be fixed at xApp side that was found during the e2 testing while supporting the comparison of different RIC in the open source - Moved to next release.

Conflict Manager Phase1 is not yet released. Integration with CI is pending - Moved to Next release.



Non-Real-time RIC  (NONRTRIC)
-----------------------------

NONRTRIC L Release Highlights:

Big push to improve SMO integration - with updated version of a fully integrated SMO deployment blueprint

Small functional improvement in component functions to rectify issues and support integration activities

Good improvement in Service Manager & RANPM functions to improve robustness and specification compliance.



Operation and Maintenance(OAM)
------------------------------

O-DU High L Release Feature Scope:

Simplification of deployment by removing ONAP DMaaP

Integration of fail based PM in docker compose deployment.

Integration of grafana into user management solution by keycloak

Status information within topology

updates of images used in docker-compose deployments to reduce CVEs in deployments




O-DU High
---------

O-DU High L Release Feature Scope:

End-to-end integration

	SIb1 parameter testing on going post Test mac synchronization with TM500 in NTUST lab

OSC-OAI Collaboration

	OAI L1 communication with ODU-High is now active.

	OAI-CU can also be executed with ODU-High.

	ODU-High with OAI-L1 works till MSG2. There are few known issues to be resolved after ODU-High sends MSG2 to OAI-L1.

Adapting to New ASN.1 encoder decoder

	New ASN.1 encoder decoder generated codec_utils merged in the main branch



O-DU Low
--------

O-DU Low L Release Feature Scope:

Improve O2 DMS ETSi profile



Simulators (SIM)
----------------

O-DU Low L Release Feature Scope:

Implemented a new Python version for the simulated O-RU and simulated O-DU.

Aligned YANG models for O1 and OpenFronthaul M-Plane with November 2024 train (O-RAN.WG4.MP.0-R004-v16.01)

Implemented hybrid and hierarchical O-RU simulators. Simulated O-DUs can accept connections from O-RUs.



Infrastructure (INF)
--------------------

INF L Release Feature Scope:  

Update INF StarlingX O-Cloud to aligned with StarlingX 10.0

Update O2 implementation to aligned with new Spec

Add multi-node support for OKD O-Cloud



Service Management and Orchestration  (SMO)
-------------------------------------------

SMO L Release Feature Scope: 

Improve Topology Exposure & Inventory (TEIV) models & functionality. 

Improve O2 DMS ETSi profile.

improve the NFO K8s profile integration with OSC-INF.



Integration(INT)
----------------

O-DU Low L Release Feature Scope:

Standardize Kubernetes Test Environment Script for Integration Projects

SMO + Non-RT RIC + OAM deployment

AIMLFW Deployment




AI/ML Framework
---------------

AI/ML Framework L Release Feature Scope:

New repository has been added to provide SDK for pipeline preparation

Four reusable component has been introduced:

	feature extraction

	model training

	model storage

	model metrics storage

Model storage SDK enhanced to exchange data between components

Error Handling for responses as per the specification

Fix APIs for fetching and storing model metrics

Fix external model upload

Model storage SDK could be executed in standalone mode (without kubernetes)

Abstraction for different storage mechanism has been added to model storage SDK 



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
