# Authors: Maurizio Lupo <maurizio.lupo@redomino.com> and contributors (see docs/CONTRIBUTORS.txt)
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.

from Products.Five import BrowserView
from redomino.redirectparent.interface import IRedirectToParent
from zope.interface import alsoProvides, noLongerProvides
from zope.component import getMultiAdapter
from plone.app.layout.navigation.defaultpage import isDefaultPage
from Acquisition import aq_inner, aq_parent
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.CMFCore.interfaces import IFolderish

class ToggleRedirectToParent(BrowserView):
    """toggle redirect to parent interface"""

    @property
    def viewurl(self):
        return getMultiAdapter((self.context, self.request), name = 'plone_context_state').view_url()

    def __call__(self):

        context = aq_inner(self.context)
        container = aq_parent(context)

        if isDefaultPage(container, context):
            context = container

        if IPloneSiteRoot.providedBy(context) or INavigationRoot.providedBy(context):
            self.request.RESPONSE.redirect(self.viewurl)

        if IRedirectToParent.providedBy(context):
            noLongerProvides(context, IRedirectToParent)
        else:
            alsoProvides(context, IRedirectToParent)

        self.request.RESPONSE.redirect(self.viewurl)

class HasRedirectToParent(BrowserView):
    def __call__(self):
        context = aq_inner(self.context)
        container = aq_parent(context)

        if isDefaultPage(container, context):
            context = container

        return IRedirectToParent.providedBy(context)

class CanBeRedirectToParent(BrowserView):
    def __call__(self):

        context = aq_inner(self.context)
        container = aq_parent(context)

        if isDefaultPage(container, context):
            context = container

        if IPloneSiteRoot.providedBy(context) or INavigationRoot.providedBy(context):
            return False

        return True





