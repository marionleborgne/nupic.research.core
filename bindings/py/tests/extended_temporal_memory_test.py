# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""Tests for ExtendedTemporalMemory."""

import os
import shutil
import tempfile
import unittest

import capnp

from nupic.bindings.experimental import ExtendedTemporalMemory
from nupic.proto.ExtendedTemporalMemoryProto_capnp import ExtendedTemporalMemoryProto



class ETMTest(unittest.TestCase):


  def testSerialization(self):
    etm = ExtendedTemporalMemory(columnDimensions=(512,))
    proto = ExtendedTemporalMemoryProto.new_message()
    etm.write(proto)

    tempdir = tempfile.mkdtemp()
    try:
      outPath = os.path.join(tempdir, "out.bin")
      with open(outPath, "w+b") as f:
        proto.write(f)
        f.seek(0)
        proto = ExtendedTemporalMemoryProto.read(f)
        newEtm = ExtendedTemporalMemory.read(proto)
    finally:
      shutil.rmtree(tempdir)
    self.assertEqual(etm.getColumnDimensions(), newEtm.getColumnDimensions())
