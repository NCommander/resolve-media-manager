
# MIT License
#
# Copyright (c) 2022 Michael Casadevall
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest

from tests import XCONFIG_TEST_VIDEO

from media_manager import MediaFile

class TestMediaFile(unittest.TestCase):
    '''Tests parsing a media files headers'''

    def testOpeningMediaFile(self):
        '''Can we load a media file successfully?'''
        mf = MediaFile()
        mf.load_file(XCONFIG_TEST_VIDEO)

        self.assertEqual(len(mf.streams), 2)

    def testStreamTypeLoading(self):
        '''split streams into components'''
        mf = MediaFile()
        mf.load_file(XCONFIG_TEST_VIDEO)

        streams = mf.get_streams_by_type("video")
        self.assertEqual(len(streams), 1)

        streams = mf.get_streams_by_type("audio")
        self.assertEqual(len(streams), 1)

        streams = mf.get_streams_by_type("doesnt-exist")
        self.assertEqual(len(streams), 0)