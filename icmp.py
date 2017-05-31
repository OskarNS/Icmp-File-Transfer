#!/usr/bin/env python
#-*- coding: utf-8 -*-

#    Copyright (C) 2012-2014 Daniel Vidal de la Rubia
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation version 2.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import time

from ICMP.IcmpApp import IcmpSender, IcmpReceiver


def show_usage ():
    print """
      USAGE:
        icmp.py recv <destination file>
        icmp.py send <file to transfer> <remote address>
    """
    exit()


if __name__ == '__main__':
    try:
        action = sys.argv[1]
        name = sys.argv[2]
    except IndexError:
        show_usage()

    if action == 'send': 
        try:
            dst_addr = sys.argv[3]
        except:
            show_usage()

        try:
            demo = sys.argv[4]
            print "Demo mode..."
        except:
            demo = 0
            pass


        msgs = ["Hejsa", "Svaret til opgave 17 er b"]
        i = 0
        while True:
            if demo:
                if len(msgs) == i:
                    print "Done with demo"
                    break
                msg = msgs[i]
                i+=1
                time.sleep(5)
            else:
                msg = raw_input()
            with IcmpSender(name + ": " + msg) as sender:
                #print "Sending message..."
                sender.send(dst_addr)

    elif action == 'recv': 
        while True:
            with IcmpReceiver() as receiver:
                receiver.receive()


