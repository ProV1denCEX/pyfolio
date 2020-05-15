#
# Copyright 2016 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generates a list of historical event dates that may have had
significant impact on markets.  See extract_interesting_date_ranges."""

import pandas as pd

from collections import OrderedDict

PERIODS = OrderedDict()

PERIODS['2015 Bull-Crash'] = (pd.Timestamp('20150209'), pd.Timestamp('20151231'))

PERIODS['Circuit Break'] = (pd.Timestamp('20151101'), pd.Timestamp('20160222'))

PERIODS['50 Crash'] = (pd.Timestamp('20180101'), pd.Timestamp('20180401'))

PERIODS['Covid-19'] = (pd.Timestamp('20200101'), pd.Timestamp('20200501'))

PERIODS['2015'] = (pd.Timestamp('20150101'), pd.Timestamp('20151231'))
PERIODS['2016'] = (pd.Timestamp('20160101'), pd.Timestamp('20161231'))
PERIODS['2017'] = (pd.Timestamp('20170101'), pd.Timestamp('20171231'))
PERIODS['2018'] = (pd.Timestamp('20180101'), pd.Timestamp('20181231'))
PERIODS['2019'] = (pd.Timestamp('20190101'), pd.Timestamp('20191231'))
PERIODS['2020'] = (pd.Timestamp('20200101'), pd.Timestamp('20201231'))
PERIODS['2021'] = (pd.Timestamp('20210101'), pd.Timestamp('20211231'))