genpxe
======

generate cluster pxe files from a flat config file

Usage
-----
Running genpxe will parse the /etc/nodes.conf file and generate a corresponding pxe configuration file for each.  genpxe will use /etc/pxe-template.conf as a template for the generated files.  Generic changes can be made to the template to result in modifications to all of the pxe configs.
