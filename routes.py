#!/bin/python2
# coding=UTF-8
import dialogs.block, dialogs.repair

routes = {
    'unblock': dialogs.block.unblock,
    'repair': dialogs.repair.repair_answer,
    'repair_type': dialogs.repair.repair_type,
    'repair_ok': dialogs.repair.repair_ok,
}