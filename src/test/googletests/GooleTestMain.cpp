/* ---------------------------------------------------------------------
 * Numenta Platform for Intelligent Computing (NuPIC)
 * Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
 * with Numenta, Inc., for a separate license for this software code, the
 * following terms and conditions apply:
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 3 as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see http://www.gnu.org/licenses.
 *
 * http://numenta.org/licenses/
 * ---------------------------------------------------------------------
 */

/** @file 
Google test main program
*/

#ifdef WIN32
// Exclude rarely-used stuff from Windows headers
#define WIN32_LEAN_AND_MEAN
#endif

#include "gtest/gtest.h"
// APR must be explicit initialized
#include <apr-1/apr_general.h>

#include "sample1.h"

#include <nta/test/Tester.hpp>

#include "AddTestHeaders.hpp"

using namespace std;
using namespace nta;

#include "AddTests.hpp"

int main(int argc, char** argv) {
  // initialize APR
  apr_status_t    result;
  result = apr_app_initialize(&argc, &argv, 0 /*env*/);
  if (result) 
    NTA_THROW << "error initializing APR. Err code: " << result;

  Tester::init();

  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}