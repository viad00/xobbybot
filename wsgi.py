#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from wsgiref.handlers import CGIHandler
from bot import app

CGIHandler().run(app)
