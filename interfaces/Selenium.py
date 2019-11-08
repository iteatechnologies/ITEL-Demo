# -*- coding: utf-8 -*-
from TDSL.TDSLType import *


@api
class Selenium(Base):
    def __init__(self, *args, **kv):
        super().__init__(*args, **kv)
        pass

    class SearchType(Enum):
        id = 'id'
        name = 'name'
        className = 'className'
        cssSelector = 'cssSelector'
        xpath = 'xpath'

    def click(self, elementId: str, searchType: Enum = ''):
        """
        clicks {{elementId}}
        @param:elementId
        @param:searchType
        """

        pass

    def check(self, timeout: int, count: int, searchType: Enum = '', elementId: str = ''):
        """
        should see the {{elementId}} within {{timeout}} seconds
        @param:timeout
        @param:count
        @param:searchType
        @param:elementId
        """

        pass

    def sendKeys(self, elementId: str, searchType: Enum = '', content: str = ''):
        """
        input \"{{content}}\" to {{elementId}}
        @param:elementId
        @param:searchType
        @param:content
        """

        pass

    def clear(self, elementId: str, searchType: Enum = ''):
        """
        web element clear text
        @param:elementId
        @param:searchType
        """

        pass

    def get(self, elementId: str):
        """
        navigates to web page {{elementId}}
        @param:elementId
        """

        pass

    def setWindowSize(self, width: int, height: int):
        """
        set window size to {{width}}x{{height}}
        @param:width
        @param:height
        """

        pass
