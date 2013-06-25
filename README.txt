Introduction
============

This utility product contains a lot of tools to allow out-of-context navigation.

Introduction
============
Plone provides a strongly opinionated way to navigate your contents. Everything is based on how objects contains each others.
For example navigation portlet and breadcrumbs show contents using that criteria.
Sometimes can be useful using a different way to navigate your content.

Example 1:
A certain content is intended to be just a part of a bigger content. For example an image that doesn't make sense alone but is used inside a slideshow (redomino.tabsandslides).
In this case the product allows to redirect to the parent (for non editors).

Example 2:
You use a link to jump to a different part of the web site but the user should be able to get back to the previous content.
In this case, marking the link with an hash parameter, a link to the previous page would appear.

Redirect to parent
==================
This product adds a special interface "redomino.redirectparent.interface.IRedirectToParent". Object with this interface will redirect to the parent when accessed by non editor users.
You can add the interface using the "manage_interfaces" view.

Hidden folder
=============
This is a new content type intended to be hidden. It can be useful if we don't want users navigate directly on a certain folder leaving the contained objects accesible.
This folder is not searchable, navigable and will redirect to the parent when accessed directly.

Link with backreference
=======================
When the relatesToUID class is used on an internal link the target view will contain a link to the previous content.

