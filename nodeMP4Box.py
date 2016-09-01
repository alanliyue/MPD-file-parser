from mpd.utils import *

class XMLNode(object):
    def parse(self, xmlnode):
	    raise NotImplementedError('Should have implemented this')
	
    def write(self, xmlnode):
	    raise NotImplementedError('Should have implemented this')

class MPD(XMLNode):
    def __init__(self):
        self.profiles = ''                                    #xs:string(required)
        self.typeMPD = None                                   #PresentationType
	self.min_buffer_time = None                           #xs:duration
        self.time_shift_buffer_depth = None                   #xs: string
        self.minimum_update_period = None                     #xs: string
        self.max_segment_duration = None                      #xs: string
 	
	self.periods = None                                   #PeriodType*
        self.program_information = None                       #ProgramInformationType*
	
    def parse(self, xmlnode):
	self.profiles = parse_attr_value(xmlnode, 'profiles', str)
	self.typeMPD = parse_attr_value(xmlnode, 'type', str)
	self.min_buffer_time = parse_attr_value(xmlnode, 'minBufferTime', str)
	self.time_shift_buffer_depth = parse_attr_value(xmlnode, 'timeShiftBufferDepth', str)
	self.minimum_update_period = parse_attr_value(xmlnode, 'minimumUpdatePeriod', str)
	self.max_segment_duration = parse_attr_value(xmlnode, 'maxSegmentDuration', str)
	     
        self.periods = parse_child_nodes(xmlnode, 'Period', Period)
        self.program_information = parse_child_nodes(xmlnode, 'ProgramInformation', ProgramInformation)		
    def write(self, xmlnode):
	write_attr_value(xmlnode, 'profiles', self.profiles)
        write_attr_value(xmlnode, 'type', self.typeMPD)
	write_attr_value(xmlnode, 'minBufferTime', self.min_buffer_time)
	write_attr_value(xmlnode, 'timeShiftBufferDepth', self.time_shift_buffer_depth)
        write_attr_value(xmlnode, 'minimumUpdatePeriod', self.minimum_update_period)
	write_attr_value(xmlnode, 'maxSegmentDuration', self.max_segment_duration)
		
	write_child_node(xmlnode, 'Period', self.periods)
	write_child_node(xmlnode, 'ProgramInformation', self.program_information)
		
class ProgramInformation(XMLNode):
    def __init__(self):
        self.more_informationURL = None             #xs:string
 
        self.title = None                           #TitleType*

    def parse(self, xmlnode):
        self.more_informationURL = parse_attr_value(xmlnode, 'moreInformationURL', str)
       
        self.title = parse_child_nodes(xmlnode, 'Title', Title)

    def write(self, xmlnode):
        write_attr_value(xmlnode, 'moreInformationURL', self.more_informationURL)
        
        write_child_node(xmlnode, 'Title', self.title)

class Title(XMLNode):
    def __init__(self):
        self.title = None  #xs:string

    def parse(self, xmlnode):
        self.title = parse_attr_value(xmlnode, 'title', str)

    def write(self, xmlnode):
        write_attr_value(xmlnode, 'title', self.title)
class Period(XMLNode):
    def __init__(self):
        self.period_id = None                 #xs
        self.start = None                     #xs

        self.adaptation_sets = None              #AdaptationSetType*
		
    def parse(self, xmlnode):
        self.period_id = parse_attr_value(xmlnode, 'id', str)
        self.start = parse_attr_value(xmlnode, 'start', str)
		
        self.adaptation_sets = parse_child_nodes(xmlnode, 'AdaptationSet', AdaptationSet)
		
    def write(self, xmlnode):
        write_attr_value(xmlnode, 'id', self.period_id)
        write_attr_value(xmlnode, 'start', self.start)
		
        write_child_node(xmlnode, 'AdaptationSet', self.adaptation_sets)
		
class AdaptationSet(XMLNode):
    def __init__(self):
        self.segment_alignment = None         #xs: string
        self.bit_stream_switching = None      #xs: string
        self.max_width = None                 #xs: string
        self.max_height = None                #xs: string
        self.max_frame_rate = None            #xs: string
        self.par = None                       #xs: string
        self.lang = None                      #xs: string

        self.segment_template = None          #SegmentTemplateType*
        self.representations = None           #RepresentationType*

    def parse(self, xmlnode):
        self.segment_alignment = parse_attr_value(xmlnode, 'segmentAlignment', str)
        self.bit_stream_switching = parse_attr_value(xmlnode, 'bitstreamSwitching', str)
        self.max_width = parse_attr_value(xmlnode, 'maxWidth', str)
        self.max_height = parse_attr_value(xmlnode, 'maxHeight', str)
        self.max_frame_rate = parse_attr_value(xmlnode, 'maxFrameRate', str)
        self.par = parse_attr_value(xmlnode, 'par', str)
        self.lang = parse_attr_value(xmlnode, 'lang', str)

        self.segment_template = parse_child_nodes(xmlnode, 'SegmentTemplate', SegmentTemplate)
        self.representations = parse_child_nodes(xmlnode, 'Representation', Representation)

    def write(self,xmlnode):
        write_attr_value(xmlnode, 'segmentAlignment', self.segment_alignment)
        write_attr_value(xmlnode, 'bitstreamSwitching', self.bit_stream_switching)
        write_attr_value(xmlnode, 'maxWidth', self.max_width)
        write_attr_value(xmlnode, 'maxHeight', self.max_height)
        write_attr_value(xmlnode, 'maxFrameRate', self.max_frame_rate)
        write_attr_value(xmlnode, 'par', self.par)
        write_attr_value(xmlnode, 'lang', self.lang)

        write_child_node(xmlnode, 'SegmentTemplate', self.segment_template)
        write_child_node(xmlnode, 'Representation', self.representations)

class SegmentTemplate(XMLNode):
    def __init__(self):
        self.initialization = None                #xs:string
        self.timescale = None                     #xs:string
        self.media = None                         #xs:string
        self.start_number = None                  #xs:string
        self.duration = None                      #xs:string
    
    def parse(self, xmlnode):
        self.initialization = parse_attr_value(xmlnode, 'initialization', str)
        self.timescale = parse_attr_value(xmlnode, 'timescale', str)
        self.media = parse_attr_value(xmlnode, 'media', str)
        self.start_number = parse_attr_value(xmlnode, 'startNumber', str)
        self.duration = parse_attr_value(xmlnode, 'duration', str)

    def write(self, xmlnode):
        write_attr_value(xmlnode, 'initialization', self.initialization)
        write_attr_value(xmlnode, 'timescale', self.timescale)
        write_attr_value(xmlnode, 'media', self.media)
        write_attr_value(xmlnode, 'startNumber', self.start_number)
        write_attr_value(xmlnode, 'duration', self.duration)

class Representation(XMLNode):
    def __init__(self):
        self.representation_id = None             #xs:string
	self.mime_type = None                     #xs:string
        self.codecs = None                        #xs:string
	self.width = None                         #xs:unsignedInt
        self.height = None                        #xs:unsignedInt
        self.fram_rate = None                      #xs:unsignedIn
        self.sar = None                           #xs:string
	self.start_with_sap = None                #xs:string
	self.bandwidth = 0                        #xs:unsignedInt (required)
		
        self.segment_template = None              #SegmentTemplateType*
    def parse(self, xmlnode):
	self.representation_id = parse_attr_value(xmlnode, 'id', str) 
	self.mime_type = parse_attr_value(xmlnode, 'mimeType', str) 
	self.codec = parse_attr_value(xmlnode, 'codec', str) 
        self.width = parse_attr_value(xmlnode, 'width', int)
        self.height = parse_attr_value(xmlnode, 'height', int)  
        self.frame_rate = parse_attr_value(xmlnode, 'frameRate', int)  
        self.sar = parse_attr_value(xmlnode, 'sar', str)  
        self.start_with_sap = parse_attr_value(xmlnode, 'startWithSAP', str)  
        self.bandwidth = parse_attr_value(xmlnode, 'bandwidth', int)  
		
        self.segment_template = parse_child_nodes(xmlnode, 'SegmentTemplate', SegmentTemplate)
    def write(self, xmlnode):
	write_attr_value(xmlnode, 'id', self.representation_id)
	write_attr_value(xmlnode, 'mimeType', self.mime_type)
	write_attr_value(xmlnode, 'codec', self.codec)
	write_attr_value(xmlnode, 'width', self.width)
	write_attr_value(xmlnode, 'height', self.height)
	write_attr_value(xmlnode, 'frameRate', self.frame_rate)
	write_attr_value(xmlnode, 'sar', self.sar)
	write_attr_value(xmlnode, 'startWithSAP', self.start_with_sap)
	write_attr_value(xmlnode, 'bandwidth', self.bandwidth)
		
        write_child_node(xmlnode, 'SegmentTemplate', self.segment_template)
		
		
