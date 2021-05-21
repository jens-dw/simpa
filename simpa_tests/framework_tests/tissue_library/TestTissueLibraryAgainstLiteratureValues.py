# The MIT License (MIT)
#
# Copyright (c) 2021 Computer Assisted Medical Interventions Group, DKFZ
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated simpa_documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest
from simpa.utils import TISSUE_LIBRARY
from simpa_tests.test_utils.tissue_composition_tests import compare_molecular_composition_against_expected_values, \
    get_epidermis_reference_dictionary, get_dermis_reference_dictionary, get_muscle_reference_dictionary, \
    get_fully_oxygenated_blood_reference_dictionary, get_fully_deoxygenated_blood_reference_dictionary


class TestEpidermis(unittest.TestCase):

    def setUp(self) -> None:
        print("set_up")

    def tearDown(self) -> None:
        print("tear_down")

    def test_epidermis_parameters(self):
        compare_molecular_composition_against_expected_values(
            molecular_composition=TISSUE_LIBRARY.epidermis(),
            expected_values=get_epidermis_reference_dictionary(),
            visualise_values=False
        )

    def test_dermis_parameters(self):
        compare_molecular_composition_against_expected_values(
            molecular_composition=TISSUE_LIBRARY.epidermis(),
            expected_values=get_dermis_reference_dictionary(),
            visualise_values=False
        )

    def test_muscle_parameters(self):
        compare_molecular_composition_against_expected_values(
            molecular_composition=TISSUE_LIBRARY.epidermis(),
            expected_values=get_muscle_reference_dictionary(),
            visualise_values=False
        )

    def test_blood_oxy_parameters(self):
        compare_molecular_composition_against_expected_values(
            molecular_composition=TISSUE_LIBRARY.blood_generic(1.0),
            expected_values=get_fully_oxygenated_blood_reference_dictionary(),
            visualise_values=False
        )

    def test_blood_deoxy_parameters(self):
        compare_molecular_composition_against_expected_values(
            molecular_composition=TISSUE_LIBRARY.blood_generic(0.0),
            expected_values=get_fully_deoxygenated_blood_reference_dictionary(),
            visualise_values=False
        )
