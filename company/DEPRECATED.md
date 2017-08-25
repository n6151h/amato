_Company_ Deprecated -- Why?
============================

I originally wanted a _Company_ model so that one site could manage multiple companies.   This necessarily leads to the problem of how to restrict access in such a way that artists and other people associated with a given company only have access to that company's library, roster, and schedule.  I could have used the django **auth** models to do this by creating groups and assigning permisions, even dynmaically, when _Company_ is created, say.  The more I thought about it, the more it seemed there was an easier way.

I decided that each site will manage just one company.  With cloud computing or other inexpensive hosting options, it is easier to set up and manage multiple sites than to try to manage the whole thing in one big ball of was.  Databases and all other company-related resources are more naturally kept separate and compartmented from one another, and it should be easy enough for a sysadmin to spin up a new server or site.

Company configuration information thus goes where it really belongs: in the ``settins.py`` file, in the COMPANY settings.  I propose to make this a dictionary for now so that I can include in it things like database settings which can, perhaps, be referenced from the DATAbSE settings area.

At this point, there is very little impact.  Aside from the _Comapny_ app (and constituent compnents) going away, the _Season_ model no longer has a ``company`` attribute.

NLS  25 Aug 2017