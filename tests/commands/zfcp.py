#
# Chris Lumens <clumens@redhat.com>
#
# Copyright 2009 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.  Any Red Hat
# trademarks that are incorporated in the source code or documentation are not
# subject to the GNU General Public License and may only be used or replicated
# with the express permission of Red Hat, Inc.
#

import unittest
from tests.baseclass import *

class FC3_TestCase(CommandTest):
    command = "zfcp"

    def runTest(self):
        # pass
        self.assert_parse("zfcp --devnum=1 --wwpn=2 --fcplun=3 --scsiid=4 --scsilun=5",
                          "zfcp --devnum=1 --wwpn=2 --fcplun=3 --scsiid=4 --scsilun=5\n")

        # fail
        self.assert_parse_error("zfcp --devnum=1 --wwpn=2 --fcplun=3 --scsiid=4",
                                KickstartValueError)
        self.assert_parse_error("zfcp --devnum=1 --wwpn=2 --fcplun=3 --scsilun=4",
                                KickstartValueError)
        self.assert_parse_error("zfcp --devnum=1 --wwpn=2 --fcplun=3",
                                KickstartValueError)
        self.assert_parse_error("zfcp --devnum --wwpn --fcplun --scsiid --scsilun",
                                KickstartParseError)

class F12_TestCase(FC3_TestCase):
    def runTest(self):
        # pass
        self.assert_parse("zfcp --devnum=1 --wwpn=2 --fcplun=3",
                          "zfcp --devnum=1 --wwpn=2 --fcplun=3\n")

        # deprecated
        self.assert_deprecated("zfcp", "--scsiid")
        self.assert_deprecated("zfcp", "--scsilun")

class F14_TestCase(F12_TestCase):
    def runTest(self):
        F12_TestCase.runTest(self)

        self.assert_removed("zfcp", "--scsiid")
        self.assert_removed("zfcp", "--scsilun")

if __name__ == "__main__":
    unittest.main()
