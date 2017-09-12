#!/bin/python2
# coding=UTF-8
import dialogs.block, dialogs.repair, dialogs.parts

routes = {
    'unblock': dialogs.block.unblock,
    'repair': dialogs.repair.repair_answer,
    'repair_type': dialogs.repair.repair_type,
    'repair_ok': dialogs.repair.repair_ok,
    'parts': dialogs.parts.parts_answer,
    'parts_check': dialogs.parts.parts_check,
    'parts_bosch': dialogs.parts.parts_bosch,
}