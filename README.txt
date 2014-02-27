Introduction
============

This package provides a mechanism to easily have clients set to
work with readonly.

This is mostly useful for preventing ReadOnlyError from cropping up
from write on read operations for a public read only site.


Warning
-------

Also make sure to set your zeo client zope.conf `read-only true` setting::

    <zodb_db main>
        <zeoclient>
        ...
        read-only true
        ...
        </zeoclient>
    </zodb_db>


To make this work along with buildout, use the `read-only` recipe config option.
Also, make sure to disable product installation in your client configuration,
otherwise you'll get errors on startup. Make sure to use
plone.app.zeoclient >= 4.2.12 as it includes the read-only config option::

    [client1]
    recipe = plone.recipe.zope2instance
    ...
    read-only = true
    enable-product-installation = off
    ...


Usage
-----

Abort all transactions
~~~~~~~~~~~~~~~~~~~~~~

Aborts transaction on IPubBeforeCommit event.

Add this to the zcml-additional option for your client::

    [client1]
    recipe = plone.recipe.zope2instance
    ...
    zcml-additional =
        <include package="wildcard.readonly" file="readonly.zcml" />
    ...


Doom all transactions
~~~~~~~~~~~~~~~~~~~~~

Dooms the transaction on the IPubAfterTraversal event.

Add this to the zcml-additional option for your client::

    [client1]
    recipe = plone.recipe.zope2instance
    ...
    zcml-additional =
        <include package="wildcard.readonly" file="readonly-doom.zcml" />
    ...


Conditionally abort transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful when aborting all transactions prevents emails from getting sent out.
For instance, if you're using PloneFormGen in your setup, dooming and aborting
will prevent mail from getting sent.

Add this to the zcml-additional option for your client::

    [client1]
    recipe = plone.recipe.zope2instance
    ...
    zcml-additional =
        <include package="wildcard.readonly" file="readonly-conditional.zcml" />
    ...


Handling sending mail
~~~~~~~~~~~~~~~~~~~~~

Since mail is tied to transaction management, aborting all transactions will
also prevent sending mail on the site.

Add this to the zcml-additional option for your client::

    [client1]
    recipe = plone.recipe.zope2instance
    ...
    zcml-additional =
        <include package="wildcard.readonly" file="mail.zcml" />
    ...
