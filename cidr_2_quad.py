#!/usr/bin/env python

def cidr_to_quad(cidr_str):
    ''' return the dotted quad of a /XX notation netmask.'''
    _tmp=cidr_str.strip('/')
    cidr = int(_tmp)
    try:
        if cidr <= 32 and cidr > 0 :
            maskstr = '1'*cidr + '0'*(32-cidr)
                      
            return "%s.%s.%s.%s"%(str(int(maskstr[0:8],2)),
                                  str(int(maskstr[8:16],2)),
                                  str(int(maskstr[16:24],2)),
                                  str(int(maskstr[24:32],2)))
        else:
            raise ValueError()
        
    except ValueError:
            print "mask must be between 0 and 32"

if __name__ == "__main__":
    print cidr_to_quad('/23')
    
