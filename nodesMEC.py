from mpd.utils import *

class XMLNode(object):
    def parse(self, xmlnode):
	    raise NotImplementedError('Should have implemented this')
	
    def write(self, xmlnode):
	    raise NotImplementedError('Should have implemented this')

class MPD(XMLNode):
    def __init__(self):
        self.xsi = None                                       #xsi:schemaLocation
        self.profiles = ''                                    #xs:string(required)
        self.type = None                                      #PresentationType
        self.media_presentation_duration = None               #xs:duration
	self.min_buffer_time = None                           #xs:duration
	self.schema_location = None                           #xs: anyURI
	self.xmlns = None                                     #xmlns
		
	self.periods = None                                   #PeriodType*
	
    def parse(self, xmlnode):
        self.xsi = parse_attr_value(xmlnode, 'xmlns:xsi', str)
	self.profiles = parse_attr_value(xmlnode, 'profiles', str)
	self.type = parse_attr_value(xmlnode, 'type', str)
	self.media_presentation_duration = parse_attr_value(xmlnode, 'mediaPresentationDuration', str)
	self.min_buffer_time = parse_attr_value(xmlnode, 'minBufferTime', str)
	self.schema_location = parse_attr_value(xmlnode, 'xsi:schemaLocation', str)
	self.xmlns = parse_attr_value(xmlnode, 'xmlns', str)
	     
        self.periods = parse_child_nodes(xmlnode, 'Period', Period)
		
    def write(self, xmlnode):
	write_attr_value(xmlnode, 'xmlns:xsi', self.xsi)
	write_attr_value(xmlnode, 'profiles', self.profiles)
        write_attr_value(xmlnode, 'type', self.type)
        write_attr_value(xmlnode, 'mediaPresentationDuration', self.media_presentation_duration)
	write_attr_value(xmlnode, 'minBufferTime', self.min_buffer_time)
	write_attr_value(xmlnode, 'xsi:schemaLocation', self.schema_location)
	write_attr_value(xmlnode, 'xmlns', self.xmlns)
		
	write_child_node(xmlnode, 'Period', self.periods)

		
class Period(XMLNode):
    def __init__(self):
        self.duration = None                        #xs:duration
		
        self.groups = None                          #groupType*
		
    def parse(self, xmlnode):
        self.duration = parse_attr_value(xmlnode, 'duration', str)
		
        self.groups = parse_child_nodes(xmlnode, 'Group', Group)
		
    def write(self, xmlnode):
        write_attr_value(xmlnode, 'duration', self.duration)
		
        write_child_node(xmlnode, 'Group', self.groups)
		
class Group(XMLNode):
    def __init__(self):
        self.segment_alignment_flag = None         #xs:string
        self.mime_time = None                      #xs:string
		
        self.representations = None                #RepresentationType*
		
    def parse(self, xmlnode):
        self.segment_alignment_flag = parse_attr_value(xmlnode, 'segmentAlignmentFlag', str)  
        self.mime_type = parse_attr_value(xmlnode, 'mimeType', str) 

        self.representations = parse_child_nodes(xmlnode, 'Representation', Representation)		
		
    def write(self, xmlnode):
	write_attr_value(xmlnode, 'segmentAlignmentFlag', self.segment_alignment_flag)
	write_attr_value(xmlnode, 'mimeType', self.mime_time)
		
        write_child_node(xmlnode, 'Representation', self.representations)


class Representation(XMLNode):
    def __init__(self):
	self.mime_type = None                     #xs:string
	self.width = None                         #xs:unsignedInt
        self.height = None                        #xs:unsignedInt
	self.start_with_rap = None                #RAPtype
	self.bandwidth = 0                        #xs:unsignedInt (required)
	self.min_buffer_time = None               #xs:duration
		
	self.segment_info = None                  #SegmentInfoType*
		
    def parse(self, xmlnode):
	self.mime_type = parse_attr_value(xmlnode, 'mimeType', str) 
        self.width = parse_attr_value(xmlnode, 'width', int)
        self.height = parse_attr_value(xmlnode, 'height', int)  
        self.start_with_rap = parse_attr_value(xmlnode, 'startWithRAP', str)  
        self.bandwidth = parse_attr_value(xmlnode, 'bandwidth', int)  
        self.min_buffer_time = parse_attr_value(xmlnode, 'minBufferTime', str)  
		
	self.segment_info = parse_child_nodes(xmlnode, 'SegmentInfo', SegmentInfo)
		
    def write(self, xmlnode):
	write_attr_value(xmlnode, 'mimeType', self.mime_type)
	write_attr_value(xmlnode, 'width', self.width)
	write_attr_value(xmlnode, 'height', self.height)
	write_attr_value(xmlnode, 'startWithRAP', self.start_with_rap)
	write_attr_value(xmlnode, 'bandwidth', self.bandwidth)
	write_attr_value(xmlnode, 'minBufferTime', self.min_buffer_time)
		
	write_child_node(xmlnode, 'SegmentInfo', self.segment_info)
		
class SegmentInfo(XMLNode):
    def __init__(self):
        self.duration = None                     #xs: duration
		
        self.initialisation_segment_url = None   #InitialisationSegmentURLType*
        self.url = None                          #URLType*
		
    def parse(self, xmlnode):
        self.duration = parse_attr_value(xmlnode, 'duration', str)
		
        self.initialisation_segment_url = parse_child_nodes(xmlnode, 'InitialisationSegmentURL', InitialisationSegmentURL)
        self.url = parse_child_nodes(xmlnode, 'Url', URL)
		
    def write(self, xmlnode):
        write_attr_value(xmlnode, 'duration', self.duration)
		
        write_child_node(xmlnode, 'InitialisationSegmentURL', self.initialisation_segment_url)
        write_child_node(xmlnode, 'Url', self.url)
		
	    
class InitialisationSegmentURL(XMLNode):
    def __init__(self): 
        self.sourceURL = None                  #xs: string
    
    def parse(self, xmlnode):
        self.sourceURL = parse_attr_value(xmlnode, 'sourceURL', str)
		
    def write(self, xmlnode):
        write_attr_value(xmlnode, 'sourceURL', self.sourceURL)
		
class URL(XMLNode):
    def __init__(self):
        self.sourceURL = None                  #xs: string
		
    def parse(self, xmlnode):
        self.sourceURL = parse_attr_value(xmlnode, 'sourceURL', str)
		
    def write(self, xmlnode):
        write_attr_value(xmlnode, 'sourceURL', self.sourceURL)
		
		
