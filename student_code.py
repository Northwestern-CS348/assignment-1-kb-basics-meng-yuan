import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))


        for a in self.facts:
            if fact == a:
                print("Warning: Fact is already in the KB")
        self.facts.append(fact)
        # else:
        #     print("Invalid fact")



    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        binding_list = ListOfBindings()
        for f in self.facts:
            result = match(fact.statement, f.statement)
            if result != False:
                binding_list.add_bindings(result)
        # print(binding_list)
        if len(binding_list.list_of_bindings) == 0:
            return False
        else:
            return binding_list





