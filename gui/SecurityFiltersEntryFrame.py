
"""
Copyright 2020 Sergio Espinoza Lopez sergio.espinoza.lopez@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


Frame subclass with labels and text entries for several security
screening parameterss

"""

import tkinter as tk
from tkinter import ttk
from SecurityFilters import SecurityFilters
from StrategyFilters import StrategyFilters
from ParameterTextEntry import ParameterTextEntry


class SecurityFiltersEntryFrame( ttk.Frame ):
    """
    'Screner parameter section with screener parameter entries:
            * min_market_cap: minimum market capital in USD Millions Dollars
            * constituents_slice: After minimum markgetParameterStringVaret cap
                ordering / filtering scan up to to this number of securities
            * min_option_volume: minimum average daily option volume
            * min_iv_rank: min 52 weeks Implied Volatility Rank (%)
            * min_days_to_earnings: minimum days to next earnings report
    """

    def __init__( self, container,
                securityFilters : TypeVar[ SecurityFilters]  = None, **kargs ):

        super().__init__( container, **kargs )


        ttk.Label( self, text='Underlying filters' ).pack( fill='x', pady= ( 10, 10 ) )


        if securityFilters is None:
            #give it default values
            self.m_securityFilters = SecurityFilters()

        else:
            #store given parameters
            self.m_securityFilters = securityFilters

            #create filter entry fields
        for ( parameterName, shortDesc ) in SecurityFilters.shortDesc :
            #TODO add callback for update on m_securityFilter
            parameterEntry = ParameterTextEntry( self, parameterName, shortDesc )
            parameterEntry.pack( fill='x', expand=True )
            self.m_parameterEntryList.append( parameterEntry )

    def _updateSecurityFiltersObject( self ):
        """
            Update m_securityFilter member with parameter entry values
        """
        for entry in self.m_parameterEntryList
            value = entry.getParameterStringVar().get()
            name = entry.m_paramName
            setattribute( self.m_securityFilters, name, value )



    def getSecurityFiltersObject( self ) -> SecurityFilters:
        self._updateSecurityFiltersObject()
        return self.m_securityFilters
