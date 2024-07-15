"""Simulation files describe situations and their expected outcomes"""

from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_greece import CountryTaxBenefitSystem

# all children minors
# all children depepdent
# citizenship boolean


TEST_CASE_1 = {
    'persons': {
        'parent_1': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_2': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 15}
            },
        'parent_3': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_4': {
            'categ_of_citizenship': {'2019': 'Πολίτης κράτους-μέλους της ΕΕ'},
            'tax_years': {'2019': 7}
            },
        'parent_5': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_6': {
            'categ_of_citizenship': {'2019': 'Πολίτης κράτους-μέλους της ΕΕ'},
            'tax_years': {'2019': 7}
            },
        'parent_7': {
            'categ_of_citizenship': {'2019': 'Δικαιούχος του ανθρωπιστικού καθεστώτος'},
            'tax_years': {'2019': 5}
            },
        'parent_8': {
            'categ_of_citizenship': {'2019': 'Δικαιούχος του ανθρωπιστικού καθεστώτος'},
            'tax_years': {'2019': 5}
            },
        'parent_9': {
            'categ_of_citizenship': {'2019': 'Δικαιούχος του ανθρωπιστικού καθεστώτος'},
            'tax_years': {'2019': 4}
            },
        'parent_10': {
            'categ_of_citizenship': {'2019': 'Δικαιούχος του ανθρωπιστικού καθεστώτος'},
            'tax_years': {'2019': 4}
            },
        'parent_11': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_12': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 15}
            },
        'parent_13': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 9}
            },
        'parent_14': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 9}
            },
        'parent_15': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_16': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 15}
            },
        'parent_17': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_18': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 15}
            },
        'child_1': {
            'birth': {'ETERNITY': '2004-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_2': {
            'birth': {'ETERNITY': '1999-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Φοιτητής'}
            },
        'child_3': {
            'birth': {'ETERNITY': '2007-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_4': {
            'birth': {'ETERNITY': '1996-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': True},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_5': {
            'birth': {'ETERNITY': '1994-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
             },
        'child_6': {
            'birth': {'ETERNITY': '2004-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_7': {
            'birth': {'ETERNITY': '1997-01-15'},
            'marital_status_child': {'2019': True},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Φοιτητής'}
            },
        'child_8': {
            'birth': {'ETERNITY': '2016-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False}
            },
        'child_9': {
            'birth': {'ETERNITY': '2015-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': ''}
            },
        'child_10': {
            'birth': {'ETERNITY': '2014-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_11': {
            'birth': {'ETERNITY': '2013-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_12': {
            'birth': {'ETERNITY': '2016-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False}
            },
        'child_13': {
            'birth': {'ETERNITY': '2015-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False}
            },
        'child_14': {
            'birth': {'ETERNITY': '2014-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_15': {
            'birth': {'ETERNITY': '2013-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_16': {
            'birth': {'ETERNITY': '1999-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': True}
            },
        'child_17': {
            'birth': {'ETERNITY': '1996-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': True}
            },
        'child_18': {
            'birth': {'ETERNITY': '2016-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False}
            },
        'child_19': {
            'birth': {'ETERNITY': '2015-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False}
            },
        'child_20': {
            'birth': {'ETERNITY': '2014-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_21': {
            'birth': {'ETERNITY': '2017-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            },
        'child_22': {
            'birth': {'ETERNITY': '2015-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_23': {
            'birth': {'ETERNITY': '2013-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_24': {
            'birth': {'ETERNITY': '2011-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_25': {
            'birth': {'ETERNITY': '2009-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_26': {
            'birth': {'ETERNITY': '2000-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Φοιτητής'}
            },
        'child_27': {
            'birth': {'ETERNITY': '2002-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_28': {
            'birth': {'ETERNITY': '2000-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Φοιτητής'}
            },
        'child_29': {
            'birth': {'ETERNITY': '1994-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': True}
            }
        },
    'families': {
        'family_1': {
            'children': ['child_1', 'child_2'],
            'parents': ['parent_1', 'parent_2'],
            'family_income': {
                '2019': 28000,
                },
            },
        'family_2': {
            'parents': ['parent_3', 'parent_4'],
            'children': ['child_3', 'child_4', 'child_5'],
            'family_income': {
                '2019': 18800,
                },
            },
        'family_3': {
            'parents': ['parent_5', 'parent_6'],
            'children': ['child_6', 'child_7'],
            'family_income': {
                '2019': 26000,
                },
            },
        'family_4': {
            'parents': ['parent_7', 'parent_8'],
            'children': ['child_8', 'child_9', 'child_10', 'child_11'],
            'family_income': {
                '2019': 13000,
                },
            },
        'family_5': {
            'parents': ['parent_9', 'parent_10'],
            'children': ['child_12', 'child_13', 'child_14', 'child_15'],
            'family_income': {
                '2019': 13000,
                },
            },
        'family_6': {
            'parents': ['parent_11', 'parent_12'],
            'children': ['child_16', 'child_17'],
            'family_income': {
                '2019': 12000,
                },
            },
        'family_7': {
            'parents': ['parent_13', 'parent_14'],
            'children': ['child_18', 'child_19', 'child_20'],
            'family_income': {
                '2019': 13000,
                },
            },
        'family_8': {
            'parents': ['parent_15', 'parent_16'],
            'children': ['child_21', 'child_22', 'child_23', 'child_24', 'child_25'],
            'family_income': {
                '2019': 27000,
                },
            },
        'family_9': {
            'parents': ['parent_17'],
            'children': ['child_26'],
            'family_income': {
                '2019': 9000,
                },
            },
        'family_10': {
            'parents': ['parent_18'],
            'children': ['child_27', 'child_28', 'child_29'],
            'family_income': {
                '2019': 10500,
                },
            }
        }
    }

TEST_CASE = {
    'persons': {
        'parent_1': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_2': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_3': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_4': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_5': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_6': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_7': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_8': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_9': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_10': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_11': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_12': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_13': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_14': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_15': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_16': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_17': {
            'categ_of_citizenship': {'2019': 'Έλληνας πολίτης'},
            'tax_years': {'2019': 5}
            },
        'parent_18': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'parent_19': {
            'categ_of_citizenship': {'2019': 'Πολίτης άλλου κράτους'},
            'tax_years': {'2019': 15}
            },
        'child_1': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_2': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_3': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_4': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_5': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_6': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_7': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_8': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_9': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_10': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_11': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_12': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_13': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_14': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_15': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_16': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_17': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_18': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_19': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_20': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_21': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_22': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_23': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_24': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_25': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_26': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_27': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_28': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            },
        'child_29': {
            'birth': {'ETERNITY': '1992-01-15'},
            'marital_status_child': {'2019': False},
            'disability_status': {'2019': False},
            'study_status': {'2019': 'Μαθητής'}
            }
        },
    'families': {
        'family_1': {
            'children': ['child_1', 'child_2'],
            'parents': ['parent_1', 'parent_2'],
            'family_income': {
                '2019': 28000,
                },
            },
        'family_2': {
            'parents': ['parent_3', 'parent_4'],
            'children': ['child_3'],
            'family_income': {
                '2019': 26000,
                },
            },
        'family_3': {
            'parents': ['parent_5', 'parent_6'],
            'children': ['child_4','child_5'],
            'family_income': {
                '2019': 18800,
                },
            },
        'family_4': {
            'parents': ['parent_7', 'parent_8'],
            'children': ['child_6', 'child_7', 'child_8'],
            'family_income': {
                '2019': 13000,
                },
            },
        'family_5': {
            'parents': ['parent_9', 'parent_10'],
            'children': ['child_9', 'child_10'],
            'family_income': {
                '2019': 12000,
                },
            },
        'family_6': {
            'parents': ['parent_11', 'parent_12'],
            'children': ['child_11', 'child_12', 'child_13', 'child_14'],
            'family_income': {
                '2019': 14500,
                },
            },
        'family_7': {
            'parents': ['parent_13', 'parent_14'],
            'children': ['child_15', 'child_16', 'child_17', 'child_18'],
            'family_income': {
                '2019': 24500,
                },
            },
        'family_8': {
            'parents': ['parent_15', 'parent_16'],
            'children': ['child_19', 'child_20', 'child_21', 'child_22', 'child_23'],
            'family_income': {
                '2019': 27000,
                },
            },
        'family_9': {
            'parents': ['parent_17'],
            'children': ['child_24', 'child_25', 'child_26'],
            'family_income': {
                '2019': 12000,
                },
            },
        'family_10': {
            'parents': ['parent_18'],
            'children': ['child_27'],
            'family_income': {
                '2019': 9000,
                },
            },
        'family_11': {
            'parents': ['parent_19'],
            'children': ['child_28', 'child_29'],
            'family_income': {
                '2019': 10500,
                },
            },
        }
    }

tax_benefit_system = CountryTaxBenefitSystem()

simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_from_entities(tax_benefit_system, TEST_CASE_1)

children_benefit = simulation.calculate('children_benefit', '2019')
eq_income = simulation.calculate('eq_income', '2019')
eq_income_scale = simulation.calculate('eq_income_scale', '2019')
eq_scale = simulation.calculate('eq_scale', '2019')
citizenship = simulation.calculate('child_benefit_citizenship', '2019')
dependent_children = simulation.calculate('dependent_children', '2019')
age = simulation.calculate('age', '2019-12')
benefit_age = simulation.calculate('benefit_age', '2019')
dependent_child = simulation.calculate('dependent_child', '2019')

print("age", age)
print("benefit_age", benefit_age)
print("dependent_child", dependent_child)
print("child_benefit_citizenship", citizenship)
print("dependent_children", dependent_children)
print("eq_scale", eq_scale)
print("eq_income", eq_income)
print("eq_income_scale", eq_income_scale)
print("children_benefit", children_benefit)


# Οικογένεια με 2 γονείς και 2 παιδιά, με ετήσιο εισόδημα 28.000€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 + 1/4 = 2. Συνεπώς το ισοδύναμο εισόδημα είναι : 28.000€ / 2= 14.000€. Άρα η οικογένεια εντάσσεται στην Γ εισοδηματική κλίμακα και θα λάβει 28+28=56€ επίδομα το μήνα
# Οικογένεια με 2 γονείς και 1 παιδί, με ετήσιο εισόδημα 26.000€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 = 1,75. Συνεπώς το ισοδύναμο εισόδημα είναι : 26.000€ / 1,75= 14.857€. Άρα η οικογένεια εντάσσεται στην Γ εισοδηματική κλίμακα και θα λάβει 28€ επίδομα το μήνα.
# Οικογένεια με 2 γονείς και 2 παιδιά, με ετήσιο εισόδημα 18.800€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 + 1/4 = 2. Συνεπώς το ισοδύναμο εισόδημα είναι : 18.800€ / 2= 9.400€. Άρα η οικογένεια εντάσσεται στην Β εισοδηματική κλίμακα και θα λάβει 42+42=84€ επίδομα το μήνα.
# Οικογένεια με 2 γονείς και 3 παιδιά με ετήσιο εισόδημα 13.000€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 + 1/4 +1/4 = 2,25. Συνεπώς το ισοδύναμο εισόδημα είναι : 13.000€ / 2,25 = 5.777€. Άρα η οικογένεια εντάσσεται στην Α εισοδηματική κλίμακα και θα λάβει 70+70+140=280€ το μήνα.
# Οικογένεια με 2 γονείς και 2 παιδιά με ετήσιο εισόδημα 12.000€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 + 1/4 = 2. Συνεπώς το ισοδύναμο εισόδημα είναι : 12.000€ / 2= 6.000€. Άρα η οικογένεια εντάσσεται στην Α εισοδηματική κλίμακα και θα λάβει 70+70=140€ το μήνα.
# Οικογένεια με 2 γονείς και 4 παιδιά με ετήσιο εισόδημα 14.500€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 + 1/4 + 1/4 + 1/4 = 2,5. Συνεπώς το ισοδύναμο εισόδημα είναι : 14.500€ / 2,5 = 5.800€. Η οικογένεια εντάσσεται στην Α εισοδηματική κλίμακα και θα λάβει 70+70+140+140=420€ το μήνα.
# Οικογένεια με 2 γονείς και 4 παιδιά με ετήσιο εισόδημα 24.500€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 + 1/4 + 1/4 + 1/4 = 2,5. Συνεπώς το ισοδύναμο εισόδημα είναι : 24.500€ / 2,5 = 9.800€. Η οικογένεια εντάσσεται στην Β εισοδηματική κλίμακα και θα λάβει 42+42+84+84=252€ το μήνα.
# Οικογένεια με 2 γονείς και 5 παιδιά με ετήσιο εισόδημα 27.000€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 + 1/4 + 1/4 + 1/4 +1/4 = 2,75. Συνεπώς το ισοδύναμο εισόδημα είναι : 27.000€ / 2,75 = 9.818€. Η οικογένεια εντάσσεται στην Β εισοδηματική κλίμακα και θα λάβει 42+42+84+84+84=336 € το μήνα.
# Μονογονεϊκή οικογένεια με 3 παιδιά και ετήσιο εισόδημα 12.000€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 +1/4 + 1/4 = 2. Συνεπώς το ισοδύναμο εισόδημα είναι : 12.000€ / 2= 6.000€. Άρα η οικογένεια εντάσσεται στην Α εισοδηματική κλίμακα και θα λάβει 70+70+140=280€ το μήνα.
# Μονογονεϊκή οικογένεια με 1 παιδί και ετήσιο εισόδημα 9.000€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 = 1,5. Συνεπώς το ισοδύναμο εισόδημα είναι : 9.000€ / 1,5= 6.000€. Άρα η οικογένεια εντάσσεται στην Α εισοδηματική κλίμακα και θα λάβει 70€ το μήνα.
# Μονογονεϊκή οικογένεια με 2 παιδιά και ετήσιο εισόδημα 10.500€: Η κλίμακα ισοδυναμίας της οικογένειας είναι : 1 + 1/2 + 1/4 = 1,75. Συνεπώς το ισοδύναμο εισόδημα είναι : 10.500€ / 1,75= 6.000€. Άρα η οικογένεια εντάσσεται στην Α εισοδηματική κλίμακα και θα λάβει 70+70=140€ το μήνα.
