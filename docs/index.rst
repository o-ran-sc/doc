.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 CMCC

.. _oran_master_doc:

The O-RAN Software Community (SC) Documentation.


Welcome to O-RAN SC M Release Documentation Home
================================================

O-RAN Alliance (https://www.o-ran.org/) members and contributors have committed to evolving Radio Access Networks (RAN) around the world. Future RANs will be built on a foundation of virtualized network elements, white-box hardware and standardized interfaces that fully embrace O-RAN’s core principles of intelligence and openness. An ecosystem of innovative new products is already emerging that will form the underpinnings of the multi-vendor, interoperable, autonomous RAN, envisioned by many in the past, but only now enabled by the global industry-wide vision, commitment and leadership of O-RAN Alliance members and contributors.

O-RAN SC is partnering with the O-RAN Alliance and Linux Foundation to support the software development for an open RAN solution that is available to everyone. The community will align with the architecture and specifications that are created in the O-RAN Alliance working groups to create a working software solution to enable an open and intelligent 5G RAN.


New features in M release:

Near-Real-time RIC X-APPs (RICAPP)
----------------------------------

RICAPP M Release Feature Scope:

Maintain existing xApp's to the M Release



Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT)
--------------------------------------------------------------------------

RICPLT M Release Feature Scope:

Near RealTime RIC container images are using ubuntu 22.04 as the base OS. The golang version also upgraded to 1.22.x. 



Non-Real-time RIC  (NONRTRIC)
-----------------------------

NONRTRIC M Release Highlights:

Continue push to improve SMO integration - with updated version of a fully integrated SMO deployment blueprint (See Integration & Test project below) 

Pre-built/tested version of SMO Integration Charts & Scripts available

Improved Topology Exposure & Inventory (TEIV) functions, models & APIs. Expand TEIV data ingestion adapters (See SMO project below) 

Maintained/Supported existing NONRTRIC/SMO platform functions 

Continued development & improvement of SMO/NONRTRIC/rApp use cases

Improved robustness and specification compliance.

Improved Testing & End-to-end Integration

Assisted in Jenkins → GHA migration



Operation and Maintenance(OAM)
------------------------------

O-DU High L Release Feature Scope:

update of OAM-Controller to OpenDaylight version Scandium-SR2

moving OAM-controller to JDK21 (OpenJDK 64-Bit Server VM version 21.0.5+11-LTS)

change CD/CI pipeline (build, test, deploy, publish) from Jenkins to GithubActions (thanks also the @Matt Watkins for outstanding support)




O-DU High
---------

O-DU High M Release Feature Scope:

Integration of ODU-High with intel L1

        Status: Spread over multiple releases

        Epic: https://jira.o-ran-sc.org/browse/ODUHIGH-475

OSC-OAI Collaboration

        Status: Spread over multiple releases

        Epic: https://jira.o-ran-sc.org/browse/ODUHIGH-557

        


Simulators (SIM)
----------------

O-DU Low M Release Feature Scope:

Stabilized the new Python version for the simulated O-RU and simulated O-DU

Minor bug fixes

Kept alignment for O1 and OpenFronahaul M-Plane YANG models with November 2024 train (O-RAN.WG4.MP.0-R004-v16.01)




Infrastructure (INF)
--------------------

INF M Release Feature Scope:  

Update INF StarlingX O-Cloud to aligned with StarlingX 11.0

Update O2 implementation to aligned with new Spec

Update the support for OKD O-Cloud



Service Management and Orchestration  (SMO)
-------------------------------------------

SMO M Release Feature Scope: 

Improve O2 DMS ETSi profile.

improve the NFO K8s profile integration with OSC-INF.




Integration(INT)
----------------

O-DU Low M Release Feature Scope:


Integration of SMOs + NON-RT RIC + OAM + AIMLFW

        Goal: Deployment of projects in a single cluster

        Epic: INT-183: Integration of SMOs + NON-RT RIC + OAM + AIMLFW in a single k8s cluster
 

CICD  deployment on COSMOS Lab

        Goal: Automate deployment testing for SMOs + NON-RT RIC + OAM + AIMLFW

        Epic: INT-182: Implement Parallel Platform Deployment to COSMOS Lab via GitHub Actions

Version control of ODU Integration code

        Goal: Manage ODU Integration code changes to be more efficient

        Epic: TBD



AI/ML Framework
---------------

AI/ML Framework M Release Feature Scope:

Kubernetes upgrade to v1.32.8 successfully completed, establishing a stable foundation for the upcoming M-release. (AIMLFW-298)

Container runtime and networking stack modernized with upgrades to Containerd, Nerdctl, Buildkit, and Calico, ensuring full compatibility with the new Kubernetes version. (AIMLFW-300, AIMLFW-299)

Critical installation issues resolved for components such as InfluxDB, Cassandra, PostgreSQL, and Helm charts, significantly improving system reliability. (AIMLFW-279, 278, 248, 245


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
