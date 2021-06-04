PySpek
======

PySpek is an acoustic spectrum analyzer written in Python, inspired by
Spek (https://github.com/alexkay/spek/) created by Alexander Kojevnikov.

------------------------------------------------------------------------

|CodeQL| |CodeFactor|

------------------------------------------------------------------------

Compatibility check table
-------------------------

+------------------------+-----------------------------------+
|                        |              Python               |
|    Operating system    +-----------+-----------+-----------+
|                        |    3.7    |    3.8    |    3.9    |
+------------------------+-----------+-----------+-----------+
| Linux Ubuntu 18.04     | |01| |02| | |03| |04| | |05| |06| |
+------------------------+-----------+-----------+-----------+
| Linux Ubuntu 20.04     | |07| |08| | |09| |10| | |11| |12| |
+------------------------+-----------+-----------+-----------+
| Windows Server 2016    | |13| |14| | |15| |16| | |17| |18| |
+------------------------+-----------+-----------+-----------+
| Windows Server 2019    | |19| |20| | |21| |22| | |23| |24| |
+------------------------+-----------+-----------+-----------+
| macOS Catalina 10.15   | |25| |26| | |27| |28| | |29| |30| |
+------------------------+-----------+-----------+-----------+




.. |CodeFactor| image:: https://www.codefactor.io/repository/github/federicogarcia/pyspek/badge
   :target: https://www.codefactor.io/repository/github/federicogarcia/pyspek
.. |CodeQL| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/codeql-analysis.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/codeql-analysis.yml



.. |01| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_7_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_7_test.yml
.. |02| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_7_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_7_build.yml

.. |03| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_8_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_8_test.yml
.. |04| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_8_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_8_build.yml

.. |05| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_9_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_9_test.yml
.. |06| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_9_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_18_04_python_3_9_build.yml


.. |07| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_7_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_7_test.yml
.. |08| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_7_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_7_build.yml

.. |09| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_8_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_8_test.yml
.. |10| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_8_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_8_build.yml

.. |11| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_9_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_9_test.yml
.. |12| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_9_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/linux_ubuntu_20_04_python_3_9_build.yml


.. |13| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_7_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_7_test.yml
.. |14| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_7_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_7_build.yml

.. |15| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_8_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_8_test.yml
.. |16| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_8_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_8_build.yml

.. |17| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_9_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_9_test.yml
.. |18| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_9_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2016_python_3_9_build.yml


.. |19| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_7_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_7_test.yml
.. |20| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_7_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_7_build.yml

.. |21| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_8_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_8_test.yml
.. |22| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_8_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_8_build.yml

.. |23| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_9_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_9_test.yml
.. |24| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_9_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/windows_server_2019_python_3_9_build.yml


.. |25| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_7_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_7_test.yml
.. |26| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_7_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_7_build.yml

.. |27| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_8_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_8_test.yml
.. |28| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_8_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_8_build.yml

.. |29| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_9_test.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_9_test.yml
.. |30| image:: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_9_build.yml/badge.svg
   :target: https://github.com/FedericoGarcia/PySpek/actions/workflows/macos_catalina_10_15_python_3_9_build.yml
