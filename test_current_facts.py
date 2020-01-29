# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import current_facts

class TestCurrentFacts(unittest.TestCase):

    def test_shold_search_tuple_inside_list(self):
        result = current_facts.search_tuple(current_facts.schema, current_facts.facts[0][1])
        self.assertEqual(result,('endereço', 'cardinality', 'one'))
    
    def test_shold_return_false_if_card_is_many(self):
        result = current_facts.is_card_one(current_facts.facts[3][1], current_facts.schema)
        self.assertFalse(result)

    def test_shold_return_true_if_card_is_one(self):
        result = current_facts.is_card_one(current_facts.facts[1][1], current_facts.schema)
        self.assertTrue(result)

    def test_should_return_true_if_item_is_valid(self):
        result = current_facts.item_is_valid(current_facts.facts[0])
        self.assertTrue(result)

    def test_should_return_false_if_item_is_not_valid(self):
        result = current_facts.item_is_valid(current_facts.facts[5])
        self.assertFalse(result)

    def test_should_return_true_if_item_is_in_map(self):
        item = current_facts.facts[0]
        dict_test = {}
        dict_test[item[0]] = {item[1]: item[2]}
        result = current_facts.item_in_map(current_facts.facts[0], 1, dict_test)
        self.assertTrue(result)

    def test_should_convert_dict_to_list_tuple(self):
        item = current_facts.facts[0]
        dict_test = {}
        dict_test[item[0]] = {item[1]: item[2]}
        result = current_facts.dict_to_tuples(dict_test)
        self.assertEqual(result, [('gabriel', 'endereço', 'av rio branco, 109', True)])

    def test_should_return_only_current_facts(self):
        result = current_facts.return_current_facts(current_facts.schema, current_facts.facts)
        self.assertEqual(result, current_facts.expected_result)

if __name__ == '__main__':
    unittest.main()