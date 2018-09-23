#!/usr/bin/env python

from pymediainfo import MediaInfo
media_info = MediaInfo.parse('test.ts')
for track in media_info.tracks:
        if track.track_type == 'Menu':
                    print track.list + track.service_name
                    
