from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # ✅ Data Structure
    path('numbers/', lambda r: views.topic_page(r, 'data_structure/numbers.html', 'numbers'), name='numbers'),

    path('variable-assignment/', lambda r: views.topic_page(r, 'data_structure/variable_assignment.html', 'variable_assignment'), name='variable_assignment'),
    path('strings/', lambda r: views.topic_page(r, 'data_structure/strings.html', 'strings'), name='strings'),
    path('lists/', lambda r: views.topic_page(r, 'data_structure/lists.html', 'lists'), name='lists'),
    path('tuples/', lambda r: views.topic_page(r, 'data_structure/tuples.html', 'tuples'), name='tuples'),
    path('sets-booleans/', lambda r: views.topic_page(r, 'data_structure/sets_booleans.html', 'sets_booleans'), name='sets_booleans'),
    path('files/', lambda r: views.topic_page(r, 'data_structure/files.html', 'files'), name='files'),
    path('dictionaries/', lambda r: views.topic_page(r, 'data_structure/dictionaries.html', 'dictionaries'), name='dictionaries'),
    path('assessment-test/', lambda r: views.topic_page(r, 'data_structure/assessment_test.html', 'assessment_test'), name='assessment_test'),
    path('assessment-solution/', lambda r: views.topic_page(r, 'data_structure/assessment_solution.html', 'assessment_solution'), name='assessment_solution'),
    path('comparison-operators/', lambda r: views.topic_page(r, 'data_structure/comparison_operators.html', 'comparison_operators'), name='comparison_operators'),
    path('chained-comparisons/', lambda r: views.topic_page(r, 'data_structure/chained_comparisons.html', 'chained_comparisons'), name='chained_comparisons'),

    # ✅ Python Statements
    path('python-statement/', lambda r: views.topic_page(r, 'python_statement/python_statements.html', 'python_statement'), name='python_statement'),
    path('if-elif-else/', lambda r: views.topic_page(r, 'python_statement/if_elif_else.html', 'if_elif_else'), name='if_elif_else'),
    path('for-while-loops/', lambda r: views.topic_page(r, 'python_statement/for_while_loops.html', 'for_while_loops'), name='for_while_loops'),
    path('useful-list/', lambda r: views.topic_page(r, 'python_statement/useful_list.html', 'useful_list'), name='useful_list'),
    path('test-solutions/', lambda r: views.topic_page(r, 'python_statement/test_solutions.html', 'test_solutions'), name='test_solutions'),
    path('guess-challenge-solution/', lambda r: views.topic_page(r, 'python_statement/guess_challenge_solution.html', 'guess_challenge_solution'), name='guess_challenge_solution'),

    # ✅ Methods & Functions
    path('methods/', lambda r: views.topic_page(r, 'methods_functions/methods.html', 'methods'), name='methods'),
    path('fun-practice-solution/', lambda r: views.topic_page(r, 'methods_functions/fun_practice_solution.html', 'fun_practice_solution'), name='fun_practice_solution'),
    path('lambda/', lambda r: views.topic_page(r, 'methods_functions/lambda.html', 'lambda'), name='lambda'),
    path('nested-scope/', lambda r: views.topic_page(r, 'methods_functions/nested_scope.html', 'nested_scope'), name='nested_scope'),
    path('args-kwargs/', lambda r: views.topic_page(r, 'methods_functions/args_kwargs.html', 'args_kwargs'), name='args_kwargs'),
    path('fun-methods-homeworks/', lambda r: views.topic_page(r, 'methods_functions/fun_methods_homeworks.html', 'fun_methods_homeworks'), name='fun_methods_homeworks'),
    path('all-in-one/', lambda r: views.topic_page(r, 'methods_functions/all_in_one.html', 'all_in_one'), name='all_in_one'),

    # ✅ Milestone Projects
    path('warm-project/', lambda r: views.topic_page(r, 'milestone_project/warm_project.html', 'warm_project'), name='warm_project'),
    path('assignment-walkthrough-complete/', lambda r: views.topic_page(r, 'milestone_project/assignment_walkthrough_complete.html', 'assignment_walkthrough_complete'), name='assignment_walkthrough_complete'),
    path('tic-tac-toe/', lambda r: views.topic_page(r, 'milestone_project/tic_tac_toe.html', 'tic_tac_toe'), name='tic_tac_toe'),
    path('play-game/', lambda r: views.topic_page(r, 'milestone_project/play_game.html', 'play_game'), name='play_game'),
    path('ready-play/', lambda r: views.topic_page(r, 'milestone_project/ready_play.html', 'ready_play'), name='ready_play'),

    # ✅ OOP
    path('object/', lambda r: views.topic_page(r, 'ob_ori_prog/object.html', 'object'), name='object'),
    path('obj-homework/', lambda r: views.topic_page(r, 'ob_ori_prog/obj_homework.html', 'obj_homework'), name='obj_homework'),
    path('oop-che-sol/', lambda r: views.topic_page(r, 'ob_ori_prog/oop_che_sol.html', 'oop_che_sol'), name='oop_che_sol'),

    # ✅ Modules
    path('mod-pack/', lambda r: views.topic_page(r, 'modules_packages/mod_pack.html', 'mod_pack'), name='mod_pack'),
    path('modules-all-in-one/', lambda r: views.topic_page(r, 'modules_packages/all_in_one_all.html', 'all_in_one_modules'), name='all_in_one_modules'),

    # ✅ Error Handling
    path('error-solution/', lambda r: views.topic_page(r, 'error_home_solution/error_hand_unit.html', 'error_hand_unit'), name='error_hand_unit'),
    path('simple-python/', lambda r: views.topic_page(r, 'error_home_solution/simple_py.html', 'simple_python'), name='simple_python'),

    # ✅ Milestone Intro
    path('warmup-intro/', lambda r: views.topic_page(r, 'milestone_intro/warmup_intro_project.html', 'warmup_intro'), name='warmup_intro'),

    # ✅ Milestone Blackjack
    path('blackjack-walkthrough/', lambda r: views.topic_page(r, 'milestone_blackjack/walkthrough_steps.html', 'blackjack_walkthrough'), name='blackjack_walkthrough'),
    path('blackjack-solution/', lambda r: views.topic_page(r, 'milestone_blackjack/blackjack_solution.html', 'blackjack_solution'), name='blackjack_solution'),

    # ✅ Empty Section
    path('empty-section-all/', lambda r: views.topic_page(r, 'empty_section_all/all_empty_all.html', 'all_empty_all'), name='all_empty_all'),
    path('build-in-solution/', lambda r: views.topic_page(r, 'empty_section_all/build_in_solution.html', 'build_in_solution'), name='build_in_solution'),

    # ✅ Decorators
    path('home-decorator/', lambda r: views.topic_page(r, 'decorator_home/home_decorator.html', 'home_decorator'), name='home_decorator'),

    # ✅ Generators
    path('generators-iterator/', lambda r: views.topic_page(r, 'iterators_generator/generators_iterator.html', 'generators_iterator'), name='generators_iterator'),

    # ✅ Collect + Datetime + Math
    path('math-datetime-open-collect/', lambda r: views.topic_page(r, 'collect_open_datetime_math/math_datetime_open_collect.html', 'math_datetime_open_collect'), name='math_datetime_open_collect'),
    path('deb-regular-timing-code/', lambda r: views.topic_page(r, 'collect_open_datetime_math/deb_regular_timing_code.html', 'deb_regular_timing_code'), name='deb_regular_timing_code'),

    # ✅ Web Scraping
    path('scraping-web/', lambda r: views.topic_page(r, 'web_scraping/scraping_web.html', 'scraping_web'), name='scraping_web'),

    # ✅ Images
    path('image-working/', lambda r: views.topic_page(r, 'working_image/image_working.html', 'image_working'), name='image_working'),

    # ✅ CSV & With
    path('csv-with/', lambda r: views.topic_page(r, 'with_csv/csv_with.html', 'csv_with'), name='csv_with'),
    path('some-practice/', lambda r: views.topic_page(r, 'with_csv/some_practice.html', 'some_practice'), name='some_practice'),

    # ✅ Email
    path('emailing-python/', lambda r: views.topic_page(r, 'emailing/emailing_python.html', 'emailing_python'), name='emailing_python'),

    # ✅ Advanced Python
    path('advanced-solution/', lambda r: views.topic_page(r, 'advanced_pods/advanced_solution.html', 'advanced_solution'), name='advanced_solution'),
    path('pods-advanced-all/', lambda r: views.topic_page(r, 'advanced_pods/pods_advanced_all_in_one.html', 'pods_advanced_all_in_one'), name='pods_advanced_all_in_one'),

    # ✅ Milestone 3
    path('project-three/', lambda r: views.topic_page(r, 'milestone_project_three/project_three.html', 'project_three'), name='project_three'),

    # ✅ Bonus
    path('widget-bonus/', lambda r: views.topic_page(r, 'bonus_widget/widget_bonus.html', 'widget_bonus'), name='widget_bonus'),
]
