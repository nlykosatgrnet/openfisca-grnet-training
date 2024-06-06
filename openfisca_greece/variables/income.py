"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

# Import from openfisca-core the Python objects used to code the legislation in OpenFisca
from openfisca_core.holders import set_input_divide_by_period
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.variables import Variable

# Import the Entities specifically defined for this tax and benefit system
from openfisca_greece.entities import Person, Family
import numpy as np

# This variable is a pure input: it doesn't have a formula
class salary(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salary"
    reference = "https://law.gov.example/salary"  # Always use the most official source

class family_income(Variable):
    value_type = float
    entity = Family
    definition_period = YEAR
    label = "Total income of a family in a year"
    reference = "https://law.gov.example/total_income"  # Always use the most official source

class disposable_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Actual amount available to the person at the end of the month"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definitions.

    def formula(person, period, _parameters):
        """Disposable income."""
        return (
            + person("salary", period)
            + person("basic_income", period)
            - person("income_tax", period)
            - person("social_security_contribution", period)
            )

class eq_scale(Variable):
    value_type = float
    entity = Family
    definition_period = YEAR
    label = "isodinami klimaka"
    reference = "https://stats.gov.example/disposable_income"

    def formula(family, period, parameters):

        # cond1 = (family.nb_persons(Family.PARENT) == 0)
        # cond2 = (family.nb_persons(Family.PARENT) == 1)
        # cond3 = (family.nb_persons(Family.PARENT) == 2)

        # eq_scales = np.zeros_like(family("family_income", period), dtype=float)
        # eq_scales[cond1] = family.nb_persons(Family.CHILD)[cond1] * 0.25
        # eq_scales[cond2] = 1.5 + ((family.nb_persons(Family.CHILD)[cond2] - 1 ) * 0.25)
        # eq_scales[cond3] = 1.5 + family.nb_persons(Family.CHILD)[cond3] * 0.25

        parent_eq = parameters(period).benefits.children_benefit.parents_equivalent_scale
        eq_scales = parent_eq.calc(family.nb_persons(Family.PARENT)) + family.nb_persons(Family.CHILD) * parameters(period).benefits.children_benefit.per_child_scale_benefit + (family.nb_persons(Family.PARENT) == 1) * parameters(period).benefits.children_benefit.extra_scale_benefit
        return eq_scales

class eq_income(Variable):
    value_type = float
    entity = Family
    definition_period = YEAR
    label = "isodinamo eisodima"
    reference = "https://stats.gov.example/disposable_income"

    def formula(family, period):
        return family("family_income", period) / family("eq_scale", period)