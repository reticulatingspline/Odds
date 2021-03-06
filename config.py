###
# Copyright (c) 2013-2014, spline
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('Odds')

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Odds', True)


Odds = conf.registerPlugin('Odds')
# This is where your configuration variables (if any) should go.  For example:
conf.registerGlobalValue(Odds, 'displayTZ', registry.String("US/Eastern", _("""What TZ to display odds in? (Don't change unless you know a valid TZ.)""")))
conf.registerChannelValue(Odds, 'disableANSI', registry.Boolean(False, _("""Disable ANSI in output for channel?""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=250:
