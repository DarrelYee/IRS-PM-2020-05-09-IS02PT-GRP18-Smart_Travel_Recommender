# category_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def ordered_rule0(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule0: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule0: got unexpected plan from when clause 2"
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(4),
                                   rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule0: got unexpected plan from when clause 3"
                    with engine.prove('answer', 'question', context,
                                      (rule.pattern(5),
                                       rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "category_rules.ordered_rule0: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule1: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule1: got unexpected plan from when clause 2"
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule1: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule2: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule2: got unexpected plan from when clause 2"
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule2: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule3: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule4: got unexpected plan from when clause 1"
            for python_ans in \
                 ('a', 'b', 'c'):
              mark2 = context.mark(True)
              if rule.pattern(1).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(2),
                                   rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule4: got unexpected plan from when clause 3"
                    with engine.prove('answer', 'question', context,
                                      (rule.pattern(4),
                                       rule.pattern(5),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "category_rules.ordered_rule4: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule5: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule5: got unexpected plan from when clause 2"
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(4),
                                   rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule5: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule6: got unexpected plan from when clause 1"
            for python_ans in \
                 ('b', 'c', 'd'):
              mark2 = context.mark(True)
              if rule.pattern(1).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(2),
                                   rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule6: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule7(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule7: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule7: got unexpected plan from when clause 2"
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(3),
                                   rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule7: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule8: got unexpected plan from when clause 1"
            for python_ans in \
                 ('b', 'c', 'd'):
              mark2 = context.mark(True)
              if rule.pattern(1).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(2),
                                   rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule8: got unexpected plan from when clause 3"
                    with engine.prove('answer', 'question', context,
                                      (rule.pattern(4),
                                       rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "category_rules.ordered_rule8: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule9: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule9: got unexpected plan from when clause 2"
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(4),
                                   rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule9: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule10: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule11: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule11: got unexpected plan from when clause 2"
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(3),
                                   rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule11: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule12: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule13(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule13: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule14: got unexpected plan from when clause 1"
            for python_ans in \
                 ('a', 'c', 'd'):
              mark2 = context.mark(True)
              if rule.pattern(1).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(2),
                                   rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule14: got unexpected plan from when clause 3"
                    with engine.prove('answer', 'question', context,
                                      (rule.pattern(4),
                                       rule.pattern(5),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "category_rules.ordered_rule14: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule15(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule15: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule15: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule16(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule16: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule16: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule17(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule17: got unexpected plan from when clause 1"
            for python_ans in \
                 ('a', 'b', 'c'):
              mark2 = context.mark(True)
              if rule.pattern(1).match_data(context, context, python_ans):
                context.end_save_all_undo()
                with engine.prove('answer', 'question', context,
                                  (rule.pattern(2),
                                   rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "category_rules.ordered_rule17: got unexpected plan from when clause 3"
                    with engine.prove('answer', 'question', context,
                                      (rule.pattern(4),
                                       rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "category_rules.ordered_rule17: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule18(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule18: got unexpected plan from when clause 1"
            with engine.prove('answer', 'question', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "category_rules.ordered_rule18: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule19(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule19: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule20(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('answer', 'question', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "category_rules.ordered_rule20: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ordered_rule21(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('category_rules')
  
  bc_rule.bc_rule('ordered_rule0', This_rule_base, 'top2',
                  ordered_rule0, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(1),
                   pattern.pattern_literal('d'),
                   pattern.pattern_literal(2),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal(11),))
  
  bc_rule.bc_rule('ordered_rule1', This_rule_base, 'top2',
                  ordered_rule1, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(1),
                   pattern.pattern_literal('d'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(6),
                   pattern.pattern_literal('b'),))
  
  bc_rule.bc_rule('ordered_rule2', This_rule_base, 'top2',
                  ordered_rule2, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('dining'),),
                  (),
                  (pattern.pattern_literal(1),
                   pattern.pattern_literal('d'),
                   pattern.pattern_literal(5),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('a'),))
  
  bc_rule.bc_rule('ordered_rule3', This_rule_base, 'top2',
                  ordered_rule3, None,
                  (pattern.pattern_literal('relaxation'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(1),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(6),))
  
  bc_rule.bc_rule('ordered_rule4', This_rule_base, 'top2',
                  ordered_rule4, None,
                  (pattern.pattern_literal('outdoor'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(1),
                   contexts.variable('num'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('b'),))
  
  bc_rule.bc_rule('ordered_rule5', This_rule_base, 'top2',
                  ordered_rule5, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('dining'),),
                  (),
                  (pattern.pattern_literal(1),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(11),))
  
  bc_rule.bc_rule('ordered_rule6', This_rule_base, 'top2',
                  ordered_rule6, None,
                  (pattern.pattern_literal('relaxation'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(1),
                   contexts.variable('num'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('b'),))
  
  bc_rule.bc_rule('ordered_rule7', This_rule_base, 'top2',
                  ordered_rule7, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('dining'),),
                  (),
                  (pattern.pattern_literal(6),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(7),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('a'),))
  
  bc_rule.bc_rule('ordered_rule8', This_rule_base, 'top2',
                  ordered_rule8, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('cultural'),),
                  (),
                  (pattern.pattern_literal(1),
                   contexts.variable('num'),
                   pattern.pattern_literal(2),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('ordered_rule9', This_rule_base, 'top2',
                  ordered_rule9, None,
                  (pattern.pattern_literal('outdoor'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(2),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(6),))
  
  bc_rule.bc_rule('ordered_rule10', This_rule_base, 'top2',
                  ordered_rule10, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(7),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(13),))
  
  bc_rule.bc_rule('ordered_rule11', This_rule_base, 'top2',
                  ordered_rule11, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('relaxation'),),
                  (),
                  (pattern.pattern_literal(4),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(6),
                   pattern.pattern_literal(12),))
  
  bc_rule.bc_rule('ordered_rule12', This_rule_base, 'top2',
                  ordered_rule12, None,
                  (pattern.pattern_literal('dining'),
                   pattern.pattern_literal('relaxation'),),
                  (),
                  (pattern.pattern_literal(5),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(10),))
  
  bc_rule.bc_rule('ordered_rule13', This_rule_base, 'top2',
                  ordered_rule13, None,
                  (pattern.pattern_literal('outdoor'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(6),
                   pattern.pattern_literal('b'),))
  
  bc_rule.bc_rule('ordered_rule14', This_rule_base, 'top2',
                  ordered_rule14, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(1),
                   contexts.variable('num'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(7),
                   pattern.pattern_literal('a'),))
  
  bc_rule.bc_rule('ordered_rule15', This_rule_base, 'top2',
                  ordered_rule15, None,
                  (pattern.pattern_literal('dining'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(7),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(10),))
  
  bc_rule.bc_rule('ordered_rule16', This_rule_base, 'top2',
                  ordered_rule16, None,
                  (pattern.pattern_literal('relaxation'),
                   pattern.pattern_literal('nature'),),
                  (),
                  (pattern.pattern_literal(4),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('b'),))
  
  bc_rule.bc_rule('ordered_rule17', This_rule_base, 'top2',
                  ordered_rule17, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('relaxation'),),
                  (),
                  (pattern.pattern_literal(1),
                   contexts.variable('num'),
                   pattern.pattern_literal(7),
                   pattern.pattern_literal('b'),
                   pattern.pattern_literal(13),))
  
  bc_rule.bc_rule('ordered_rule18', This_rule_base, 'top2',
                  ordered_rule18, None,
                  (pattern.pattern_literal('dining'),
                   pattern.pattern_literal('relaxation'),),
                  (),
                  (pattern.pattern_literal(2),
                   pattern.pattern_literal('a'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('b'),))
  
  bc_rule.bc_rule('ordered_rule19', This_rule_base, 'top2',
                  ordered_rule19, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('outdoor'),),
                  (),
                  (pattern.pattern_literal(2),
                   pattern.pattern_literal('b'),))
  
  bc_rule.bc_rule('ordered_rule20', This_rule_base, 'top2',
                  ordered_rule20, None,
                  (pattern.pattern_literal('dining'),
                   pattern.pattern_literal('relaxation'),),
                  (),
                  (pattern.pattern_literal(1),
                   pattern.pattern_literal('a'),))
  
  bc_rule.bc_rule('ordered_rule21', This_rule_base, 'top2',
                  ordered_rule21, None,
                  (pattern.pattern_literal('sights'),
                   pattern.pattern_literal('nature'),),
                  (),
                  ())


Krb_filename = '..\\category_rules.krb'
Krb_lineno_map = (
    ((14, 18), (32, 32)),
    ((20, 26), (34, 34)),
    ((27, 33), (35, 35)),
    ((34, 40), (36, 36)),
    ((41, 47), (37, 37)),
    ((60, 64), (41, 41)),
    ((66, 72), (43, 43)),
    ((73, 79), (44, 44)),
    ((80, 86), (45, 45)),
    ((99, 103), (49, 49)),
    ((105, 111), (51, 51)),
    ((112, 118), (52, 52)),
    ((119, 125), (53, 53)),
    ((138, 142), (57, 57)),
    ((144, 150), (59, 59)),
    ((151, 157), (60, 60)),
    ((170, 174), (64, 64)),
    ((176, 182), (66, 66)),
    ((184, 184), (67, 67)),
    ((188, 194), (68, 68)),
    ((195, 201), (69, 69)),
    ((216, 220), (73, 73)),
    ((222, 228), (75, 75)),
    ((229, 235), (76, 76)),
    ((236, 242), (77, 77)),
    ((255, 259), (81, 81)),
    ((261, 267), (83, 83)),
    ((269, 269), (84, 84)),
    ((273, 279), (85, 85)),
    ((294, 298), (89, 89)),
    ((300, 306), (91, 91)),
    ((307, 313), (92, 92)),
    ((314, 320), (93, 93)),
    ((333, 337), (97, 97)),
    ((339, 345), (99, 99)),
    ((347, 347), (100, 100)),
    ((351, 357), (101, 101)),
    ((358, 364), (102, 102)),
    ((379, 383), (106, 106)),
    ((385, 391), (108, 108)),
    ((392, 398), (109, 109)),
    ((399, 405), (110, 110)),
    ((418, 422), (114, 114)),
    ((424, 430), (116, 116)),
    ((431, 437), (117, 117)),
    ((450, 454), (121, 121)),
    ((456, 462), (123, 123)),
    ((463, 469), (124, 124)),
    ((470, 476), (125, 125)),
    ((489, 493), (129, 129)),
    ((495, 501), (131, 131)),
    ((502, 508), (132, 132)),
    ((521, 525), (136, 136)),
    ((527, 533), (138, 138)),
    ((546, 550), (142, 142)),
    ((552, 558), (144, 144)),
    ((560, 560), (145, 145)),
    ((564, 570), (146, 146)),
    ((571, 577), (147, 147)),
    ((592, 596), (151, 151)),
    ((598, 604), (153, 153)),
    ((605, 611), (154, 154)),
    ((624, 628), (158, 158)),
    ((630, 636), (160, 160)),
    ((637, 643), (161, 161)),
    ((656, 660), (165, 165)),
    ((662, 668), (167, 167)),
    ((670, 670), (168, 168)),
    ((674, 680), (169, 169)),
    ((681, 687), (170, 170)),
    ((702, 706), (174, 174)),
    ((708, 714), (176, 176)),
    ((715, 721), (177, 177)),
    ((734, 738), (181, 181)),
    ((740, 746), (183, 183)),
    ((759, 763), (187, 187)),
    ((765, 771), (189, 189)),
    ((784, 788), (193, 193)),
)
