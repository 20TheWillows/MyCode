def anomalies_overlap_axially(box1_log_distance, box1_length, box2_log_distance, box2_length):
    '''
    Returns a boolean to determine if two anomalies overlap axially.

            Parameters:
                    box1_log_distance (float): log distance of anomaly 1
                    box1_length       (float): axial length of anomaly 1
                    box2_log_distance (float): log distance of anomaly 2
                    box2_length       (float): axial length of anomaly 2

            Returns:
                    If there are any invalid inputs then None will be returned
                    overlap (boolean) : True if they overlap, False if they do not.
    '''   
    # Error check
    if any([box1_log_distance==None,box1_length==None,box2_log_distance==None,box2_length==None]):
        return None
    # Main function body
    box1_entirely_before_box2 = (box1_log_distance + box1_length < box2_log_distance)
    box2_entirely_before_box1 = (box2_log_distance + box2_length < box1_log_distance)

    if box1_entirely_before_box2 or box2_entirely_before_box1:
        return False
    else:
        return True

def anomalies_overlap_circumferentially(box1_start_orientation, 
                                        box1_end_orientation, 
                                        box2_start_orientation, 
                                        box2_end_orientation):
    '''
    Returns a boolean to determine if two anomalies overlap circumferentially.

            Parameters:
                    box1_start_orientation     (float): start orientation in degrees 0-360 of anomaly 1
                    box1_end_orientation       (float): end orientation in degrees 0-360 of anomaly 1
                    box2_start_orientation     (float): start orientation in degrees 0-360 of anomaly 2
                    box2_end_orientation       (float): end orientation in degrees 0-360 of anomaly 2

            Returns:
                    If there are any invalid inputs then None will be returned
                    overlap (boolean): True if they overlap, False if they do not.
    '''
    # Error check
    if any([box1_start_orientation==None,box1_end_orientation==None,box2_start_orientation==None,box2_end_orientation==None]):
        return None
    # Order boxes: box 1 will always be the one with smallest start orientation
    if box2_start_orientation < box1_start_orientation:
        box1_start_orientation, box2_start_orientation = box2_start_orientation, box1_start_orientation
        box1_end_orientation, box2_end_orientation = box2_end_orientation, box1_end_orientation
    # Determine if anomalies wrap
    anomaly1_wraps = box1_start_orientation > box1_end_orientation
    anomaly2_wraps = box2_start_orientation > box2_end_orientation
    # If they both wrap then they must overlap
    if anomaly1_wraps and anomaly2_wraps:
        return True
    # Case where neither wraps
    if not anomaly1_wraps and not anomaly2_wraps:
       overlap = box2_start_orientation <= box1_end_orientation
    # Case where one wraps and two doesn't - must always overlap
    elif anomaly1_wraps and not anomaly2_wraps:
        overlap = True
    # Case where two wraps and one doesn't
    elif not anomaly1_wraps and anomaly2_wraps:
       overlap = box2_start_orientation <= box1_end_orientation or box2_end_orientation >= box1_start_orientation
    
    return overlap

def get_roman_year(year):
    '''
    Returns a string representation of the supplied decimal year in Roman numerals.

            Parameters:
                    year     (int): Decimal year e.g. 1987
            Returns:
                    String Roman year
    '''
    centuries_lookup = {0:"", 1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC",8:"DCCC",9:"CM"}
    units_lookup = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII",8:"VIII",9:"IX"}
    tens_lookup = {0:"", 1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX",8:"LXXX",9:"XC"}
    out = ""
    # 1000s
    thousands = int(year/1000)
    # 100s
    centuries = int((year - thousands*1000)/100)
    # 10s
    tens = int((year - thousands*1000 - centuries*100)/10)
    # Units
    units = year - thousands*1000 - centuries*100  - tens*10
    # Return string construction
    out = "M"*thousands
    out += centuries_lookup[centuries]
    out += tens_lookup[tens]
    out += units_lookup[units]
 
    return out