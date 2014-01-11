###
# Copyright (c) 2013, raviteja
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import urllib2
from BeautifulSoup import BeautifulSoup

class Score(callbacks.Plugin):
    """Add the help for "@plugin help Score" here
    This should describe *how* to use this plugin."""
    def score(self, irc, msg, args):
        xml_link = 'http://synd.cricbuzz.com/j2me/1.0/livematches.xml'
        xml = urllib2.urlopen(xml_link)
        data = xml.read()
        xml.close()
        code = BeautifulSoup(data)
        matchs = code.mchdata.findAll("match")
        for i in matchs:
            j = str(i)
            if "IND" in j:
                content = BeautifulSoup(j)
        mchDesc = content.match.get('mchdesc')
        vcity = content.match.get('vcity') 
        vcountry = content.match.get('vcountry')
        grnd = content.match.get('grnd')
        status = content.state.get('mchstate')
        str1 = str(mchDesc)+" - " +str(grnd)+ " - "+ str(vcity) + " - " + str(vcountry) +" - "+ str(status)
        irc.reply(str1)
        btTm = content.mscr.inngsdetail.bttm.get('sname')
        runs = content.mscr.inngsdetail.bttm.inngs.get('r')
        overs = content.mscr.inngsdetail.bttm.inngs.get('ovrs')
        wkts = content.mscr.inngsdetail.bttm.inngs.get('wkts')
        str2 = str(btTm) + ": " + str(runs) + "/" +str(wkts) +" Overs: " + str(overs)
        irc.reply(str2)
        blgTm = content.mscr.inngsdetail.blgtm.get('sname')
        if content.mscr.inngsdetail.blgtm.inngs:
            runs2 = content.mscr.inngsdetail.blgtm.inngs.get('r')
            overs2 = content.mscr.inngsdetail.blgtm.inngs.get('ovrs')
            wkts2 = content.mscr.inngsdetail.blgtm.inngs.get('wkts')
            str3 = str(blgTm) + ": " + str(runs2) + "/" +str(wkts) +" Overs: " + str(overs2)
            irc.reply(str3)
        
Class = Score


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
