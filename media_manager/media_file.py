# The representation of a media file managed by this project

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

from media_manager.streams import Stream

import ffmpeg

class MediaFile(object):
    '''
    Media files represent an actual file on a filesystem, and have various bits
    of media information and more available for making transcoding decisions
    '''

    def __init__(self):
        self.streams = []

    def load_file(self, filename):
        '''Loads a file into the media manager'''
        mf = MediaFile()

        file_probe = ffmpeg.probe(filename)

        # Create a stream for each part of this file
        for stream in file_probe['streams']:
            ms = Stream()
            ms.media_type = stream['codec_type']
            ms.codec = stream['codec_name']
            self.streams.append(ms)

    def get_streams_by_type(self, media_type):
        '''Returns all streams in this media file that match a given type'''
        matching_streams = []

        for stream in self.streams:
            if stream.media_type == media_type:
                matching_streams.append(stream)

        return matching_streams
