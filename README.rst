PySpek
======

|Tests| |CodeQL|

PySpek is an acoustic spectrum analyzer written in Python, inspired by
Spek (https://github.com/alexkay/spek/) created by Alexander Kojevnikov.

+----------------------+-----------------------------------------------+
|                      |                     Python                    |
|   Operative system   +-----------+-----------+-----------+-----------+
|                      |    3.6    |    3.7    |    3.8    |    3.9    |
+----------------------+-----------+-----------+-----------+-----------+
| Linux Ubuntu 18.04   | |01| |02| | |03| |04| | |05| |06| | |07| |08| |
+----------------------+-----------+-----------+-----------+-----------+
| Linux Ubuntu 20.04   | |09| |10| | |11| |12| | |13| |14| | |15| |16| |
+----------------------+-----------+-----------+-----------+-----------+
| Windows Server 2016  | |17| |18| | |19| |20| | |21| |22| | |23| |24| |
+----------------------+-----------+-----------+-----------+-----------+
| Windows Server 2019  | |25| |26| | |27| |28| | |29| |30| | |31| |32| |
+----------------------+-----------+-----------+-----------+-----------+
| macOS Catalina 10.15 | |33| |34| | |35| |36| | |37| |38| | |39| |40| |
+----------------------+-----------+-----------+-----------+-----------+

.. |Tests| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |CodeQL| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/codeql-analysis.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/codeql-analysis.yml
   
.. |01| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |02| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |03| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |04| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |05| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |06| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |07| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |08| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |09| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |10| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |11| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |12| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |13| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |14| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |15| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |16| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |17| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |18| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |19| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |20| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |21| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |22| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |23| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |24| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |25| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |26| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |27| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |28| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |29| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |30| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |31| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |32| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |33| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |34| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |35| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |36| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |37| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |38| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |39| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
.. |40| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/tests.yml
