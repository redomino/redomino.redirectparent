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

from zope.interface import alsoProvides
from redomino.redirectparent.interface import IRedirectToParent

def addRedirectInterface(obj, event):
    """ Checks if the current object is a NonIndexedFolder
        If so, then the object must provides IRedirectToParent
    """
    if obj.portal_type == 'NonIndexedFolder':
        alsoProvides(obj, IRedirectToParent)


